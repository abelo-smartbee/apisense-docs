# Grafiki instrukcji montażu — jak je budować

Dotyczy `docs/assembly/`. Powstało po przebiegu z sierpnia 2026, w którym cały
rozdział 03 i kroki 01–02 przeszły z rysunków grafika na hybrydę „ramka
wektorowa + realny zrzut z aplikacji" — po to, żeby następna osoba zaczynała od
metody i od listy pułapek, a nie od reverse-engineeringu cudzego SVG.

## Czym jest instrukcja montażu

`docs/assembly/index.html` to **jeden plik** — deck dwudziestu slajdów serwowany
w dwudziestu językach. Przełącznik języka nie ładuje niczego; chowa elementy
`[lang]` regułą `display: none`. Konsekwencja, która wraca w tym dokumencie
kilka razy: **wszystkie locale dostają ten sam obrazek**.

Grafiki leżą w `docs/assembly/figs/`. Z tego pliku powstają dwa artefakty:

- `tools/build_standalone.py` → jeden samowystarczalny HTML (wszystko w base64,
  wysyłany mailem jako załącznik),
- `tools/build_pdf.py` → dwadzieścia PDF-ów, po jednym na locale.

Obok decku żyje **instrukcja skrócona** — `docs/assembly/short/index.html`, ta
sama treść ściśnięta na jeden arkusz A4 poziomo, do druku jako wkładka do
pudełka. Ten sam mechanizm `[lang]` i ten sam klucz `localStorage`, więc
przycisk w nagłówku decku otwiera ją w bieżącym języku. Grafiki bierze z
`figs/` (te same `pdf-*.svg` co deck plus `qr-*.svg` i `badge-*.svg`).
`tools/build_short_pdf.py` drukuje ją do `docs/assembly/pdf/short/` — i
**odmawia**, gdy w którymś locale treść nie mieści się na stronie: arkusz ma
`overflow: hidden`, więc `Pages: 1` nic nie dowodzi, dlatego strona sama
raportuje przepełnione pudełka w `data-overflow`, a skrypt to czyta przez
`--dump-dom`. Po każdej zmianie treści odpal `--check`; jeśli locale wystaje,
zmniejsz mu `font-size` `.sheet` w ostatniej regule stylu strony (progi są tam
opisane).

Wszystko regeneruj **raz, na końcu**. Przegenerowanie w połowie migracji zapieka stan
przejściowy w dwudziestu plikach naraz.

## Zasada: ramka od grafika, ekran z suite'u

Rysunki ekranów aplikacji rozjeżdżają się z aplikacją przy każdym wydaniu i
nikt tego nie zauważa, dopóki ktoś nie porówna ręcznie. W przebiegu z sierpnia
mock kroku 03.2 wciąż pokazywał pole *Name abbreviation (max. 3 characters)*,
którego w aplikacji nie ma od dawna, oraz sklejał dwa ekrany w jeden.

Dlatego dzielimy panel na dwie warstwy:

| warstwa | skąd | dlaczego |
|---|---|---|
| obudowa telefonu, pasek stanu, dłoń, strzałki, etykieta numeru | SVG od grafika | styl instrukcji, nie zmienia się przy release'ach |
| zawartość ekranu | zrzut z suite'u `apisense-mobile` | odświeża się automatycznie, zawsze zgodny z aplikacją |

Zrzut wchodzi jako `<image>` przycięty `clipPath`em do zaokrąglonego kształtu
ekranu. Ekran przestaje być wektorem — w slajdzie renderuje się przy ~155 px,
więc nie widać, ale w PDF przy dużym powiększeniu zmięknie.

## Warsztat: jak w ogóle edytować te SVG

**Tekstu w grafikach od grafika zmienić się nie da.** W całej paczce `KROK *`
jest **zero elementów `<text>`** — litery są zamienione na krzywe. Nie ma fontu,
nie ma czego podmienić. Sprawdzenie:

```bash
grep -c '<text' docs/assembly/figs/*.svg
```

Jedyny wyjątek w `figs/` to `montaz-systemu-animated.svg` (kroku 06) — ma cztery
`<text>` i nie pochodzi z tej paczki. Tam tekst jest edytowalny normalnie.

Da się natomiast: **usuwać, przesuwać, klonować, przeszczepiać pojedyncze glify
i wstawiać obrazki**. Elementy nie mają sensownych `id`, więc jedynym pewnym
uchwytem jest **geometria**. Narzędzie: headless Chrome liczy `getBBox()`,
skrypt operuje na DOM-ie i serializuje z powrotem.

```html
<!-- szkielet: zapisz jako .html, odpal chrome --headless --dump-dom, wyłuskaj <pre> -->
<body><pre id="out"></pre><script>
const near = (a,b,t=3) => Math.abs(a-b) <= t;
fetch('ŚCIEŻKA.svg').then(r => r.text()).then(t => {
  const d = document.createElement('div'); d.innerHTML = t; document.body.appendChild(d);
  const svg = d.querySelector('svg');
  const bb = e => { try { const b = e.getBBox(); return (b.width||b.height) ? b : null } catch(_) { return null } };
  // ...operacje na elementach wyszukanych po bbox...
  document.getElementById('out').textContent = new XMLSerializer().serializeToString(svg);
});
</script></body>
```

Uruchomienie wymaga `--allow-file-access-from-files`, bo `fetch` idzie po `file://`:

```bash
google-chrome --headless=new --disable-gpu --no-sandbox \
  --allow-file-access-from-files --virtual-time-budget=9000 \
  --dump-dom "file://$PWD/skrypt.html"
```

Zanim cokolwiek zmienisz, zrób zrzut bboxów całego pliku i popatrz na liczby —
panele, ekrany i etykiety mają charakterystyczne, powtarzalne wymiary.

## Sześć pułapek

Każda kosztowała co najmniej jeden nieudany przebieg.

**1. Grupa opakowująca ekran ma dokładnie ten sam bbox co ekran.** Pętla „usuń
wszystko, co mieści się w obrysie ekranu" kasuje tę grupę razem ze świeżo
wstawionym obrazkiem. Objaw: pusty telefon. Zabezpieczenie — pomiń elementy o
bboxie równym bboxowi ekranu oraz przodków wstawionego obrazka:

```js
if (near(b.x,SCR.x) && near(b.y,SCR.y) && near(b.width,SCR.w) && near(b.height,SCR.h)) continue;
if (e.contains(img)) continue;
```

**2. `clipPath` żyje w `<defs>` i ma bbox swojego kształtu.** Ta sama pętla
wycina kształt z clipPath, clipPath robi się pusty i przycina obrazek do zera.
Objaw identyczny jak wyżej. Zabezpieczenie: `if (e.closest('defs')) continue;`.

**3. Atrybut `fill` przegrywa z klasą CSS.** Te pliki mają `<style>` z regułami
`.cls-N { fill: … }`, które biją atrybut prezentacyjny. `setAttribute('fill', …)`
nie zrobi nic. Trzeba `setAttribute('style', 'fill:#f8ecde')`.

**4. `getBBox()` ignoruje własny `transform` elementu**, ale uwzględnia
transformy dzieci. Po opakowaniu czegoś w `<g transform="translate(…)">`
zapytania po bboxie nadal zwracają współrzędne sprzed przesunięcia. Przy
zamianie paneli miejscami trzeba o tym pamiętać, inaczej drugi przebieg operuje
na złych pozycjach.

**5. Kółka-wyimki wychodzą poza swój panel.** Element wskazujący pole na
sąsiednim telefonie zaczyna się przed lewą krawędzią panelu, więc test
„zawiera się w przedziale x" go nie łapie i zostaje sierota po skasowanym
panelu. Selekcjonuj po **środku bboxa**, nie po zawieraniu — z zabezpieczeniem
na szerokość, żeby nie złapać długich strzałek:

```js
const cx = b.x + b.width/2;
if (cx >= X0 && cx <= X1 && b.width < 700) e.remove();
```

**6. Przeglądarka podaje stary SVG z cache.** Podmieniłeś plik, odświeżasz i
widzisz poprzednią wersję. Przy podglądzie lokalnym:

```js
document.querySelectorAll('img[src$=".svg"]')
  .forEach(i => { i.src = i.src.split('?')[0] + '?v=' + performance.now() });
```

## Przygotowanie zrzutu

**Ekran w mocku ma 742 × 1629 jednostek, czyli proporcję 1:2,196.** Do tej
liczby dopasowujesz zrzut.

**Odetnij ramkę, jeśli zrzut ją ma.** Klucze z `frame: phone` w manifeście
`apisense-mobile` przychodzą z narysowanym bezelem — nałożony na obudowę z SVG
daje podwójną ramkę. Bezel to 8 px przy szerokości 428 i 32 px przy 1712.
Zmierz go, skanując wiersz w poszukiwaniu koloru tła ekranu `#FFF8F3`, zamiast
zgadywać.

**Dopełniaj, nie przycinaj.** `preserveAspectRatio="slice"` przy niedopasowanej
proporcji obcina brzegi — a na brzegach jest dolna nawigacja i etykiety.
Lepiej dołożyć płótno kolorem tła aplikacji do dokładnej proporcji 2,196 i
wtedy `slice` nic nie utnie.

**Skalę odnieś do pełnego zrzutu, nie do oka.** Zrzuty bywają kadrami wyciętymi
ze scrolla — węższymi niż ekran i bez paska stanu. Wtedy rozciągnięcie na całą
szerokość telefonu daje interfejs wyraźnie większy niż w sąsiednich panelach.
Punkt odniesienia, który się sprawdził: w pełnym zrzucie `apiaries.png` górna
krawędź logotypu Apisense wypada na **14,5% wysokości ekranu**. Dopełnij kadr
u góry tak, żeby logotyp trafił w ten sam procent:

```python
frac = 0.145
P = (frac*h0 - logo_y) / (1 - frac)     # ile dołożyć u góry
H = round(h0 + P); W = round(H/2.196)   # płótno docelowe
```

**Pasek stanu dorób klonem.** Kadry bez ramki nie mają zegara ani notcha, a
sąsiednie panele mają — różnica rzuca się w oczy. Sklonuj tło paska plus zegar,
notch i ikony z sąsiedniego panelu i przesuń o różnicę pozycji paneli.

## Kolory

Aplikacja ma dwa tła i **oba są poprawne** — zależnie od ekranu
(`apisense_ui/lib/src/design_system/colors/app_colors.dart`):

```dart
static const surfaceBright    = Color(0xFFFFF8F3);   // ekran powitalny, rejestracja
static const surfaceContainer = Color(0xFFF8ECDE);   // Add apiary i pochodne
```

Grafik użył `surfaceBright` wszędzie. Jeśli wstawiasz zrzut ekranu, który
renderuje się na `surfaceContainer`, przemaluj pasek stanu tego panelu — inaczej
widać szew między paskiem a zrzutem. Patrz pułapka 3: przez `style`, nie `fill`.

## Obudowa telefonu

Rozdziały 01–03 i 05 rysują wokół każdego ekranu obudowę telefonu. Grafik
porzucił ją w rozdziale 04 i wkleił same zrzuty — deck rozjeżdżał się stylistycznie
w połowie. **Wzorzec bierzemy z rozdziału 03**, bo to trzy rozdziały przeciw
jednemu:

```
ekran 741.6 szeroki  ·  promień narożnika 50.4  ·  obudowa 14.4 grubości  ·  #d4c4ae
```

Wszystkie trzy liczby przenoś **jako proporcje szerokości panelu**, nie jako
stałe — panele mają różne skale (`scale(.68)` i `scale(.6787)` w tym samym pliku).

Obudowę rysuj jako **jedną ścieżkę-pierścień**: zewnętrzny zaokrąglony prostokąt
i wewnętrzny w tym samym `d`, z `fill-rule="evenodd"`. Kusi, żeby zamiast tego
przyciąć zrzut przez `clipPath` i obrysować go — nie rób tego. Pierścień malowany
na wierzchu **sam zakrywa kwadratowe narożniki bitmapy**, więc odpada `clipPath`
na panel (i pułapka 2 razem z nim).

Kolejność warstw jest tu jedyną rzeczą, którą łatwo zepsuć. Pierścień musi trafić
**nad zrzuty, ale pod dłonie i strzałki** — w rozdziale 04 dłonie regularnie
wychodzą poza krawędź panelu i pierścień malowany na końcu przecina je beżową
wstęgą. We wszystkich czterech plikach warstwy leżą w tej samej kolejności, więc
kotwica jest prosta: **wstaw tuż za ostatnim `<image>`**.

Geometria paneli ma dwa źródła. Zrzuty — z `transform` obrazka
(`translate(tx ty) scale(s)` → `x=tx, y=ty, w=1082·s, h=2400·s`). Wektorowe ekrany
skanera (04.6, 04.9, 04.12) — z podkładowego `<rect>`, i wypadają dokładnie
741.6 × 1629.8, czyli w module rozdziału 03.

Na koniec **rozszerz `viewBox`** o grubość obudowy z każdej strony i zaktualizuj
`width`/`height` przy `<img>` w `index.html` — inaczej skrajne panele zostaną
przycięte.

Gotowiec: `tools/svg_add_bezel.py`. Pomija pliki, które obudowę już mają, więc
można go puścić na całej paczce po każdej nowej dostawie od grafika.

## Biblioteka kształtów

Wszystko, czym generator rysuje, leży w `tools/assets/` i **nie jest czytane
z `figs/`**. To nie jest kosmetyka: generator nadpisuje pliki w `figs/`, więc
źródło kształtów wzięte stamtąd zadziałałoby dokładnie raz, a potem samo się
skasowało. Kosztowało to jeden przebieg.

| plik | co to |
|---|---|
| `hand-point.path` | dłoń wskazująca (ścieżka, obrys 18 px) |
| `arrow-flow.svg` | strzałka panel → panel, kładziona na osi przerwy |
| `arrow-point.svg` | zakręcona strzałka do kontrolki |
| `thumbs-up.path` | kciuk — znak potwierdzenia, nie wskaźnik |
| `scanner-screen.svg` | wektorowy ekran skanera QR |
| `lato-semibold-digits.ttf` | subset kroju numeracji |

**Skaner nie ma zrzutu i nie będzie miał** — suite nigdy go nie łapie, bo to
ekran kamery. Dlatego mieszka w repo jako wektor przeniesiony od grafika,
znormalizowany do modułu panelu, z klasami i identyfikatorami przedrostkowanymi
`sc-`, żeby nie zderzyły się z klasami figury.

Przy przenoszeniu takiego fragmentu **uważaj na grupowane selektory**. CSS
grafika ma reguły w rodzaju `.cls-9, .cls-12 { fill: none; stroke: … }`, a regex
w stylu `\.([\w-]+)\s*\{` łapie z takiej grupy **tylko ostatnią klasę**. Zgubione
`fill: none` daje czerń, bo to domyślne wypełnienie w SVG — u nas biały wizjer
skanera wyszedł czarnym prostokątem. Selektor rozbijaj po przecinkach.

## Gesty: dwa tryby, nie jeden próg

Dłoń ma 46% szerokości ekranu i korpus ciągnie w prawo-dół od czubka palca.
Jedna reguła nie obsłuży wszystkich celów, więc w tablicy `FIGURES` deklaruje
się wprost, o co chodzi:

- **`point`** — czubek ląduje na kontrolce. Działa tam, gdzie dłoń mieści się
  w telefonie, czyli mniej więcej w górnych 80% ekranu. Używaj wszędzie, gdzie
  sąsiednia kontrolka mogłaby zostać wzięta za właściwą.
- **`press`** — dłoń **przykrywa** kontrolkę, czubek zaparkowany na `PRESS_Y`.
  To placement samego grafika z 04.3 i 04.4 i jedyny, który działa dla przycisku
  w dolnym rogu. Bezpieczny, bo dłoń siada na ostatnim przycisku w rzędzie.
- **`mirror: True`** — korpus idzie w lewo od czubka. Potrzebne, gdy naturalna
  strona jest zajęta; na pasku nawigacji nieodbita dłoń siada na sąsiedniej
  pozycji i cały gest czyta się jako wskazanie tamtej.

Co **nie** działa, a zostało sprawdzone: zwisająca pod telefonem dłoń (przestaje
czytać się jako dotyk ekranu) i obrót o 180° (korpus zasłania to, czym kontrolka
jest podpisana). W pasek nawigacji z czterema ikonami tą dłonią po prostu nie da
się trafić — zamiast walczyć, weź zrzut z **otwartym menu**, gdzie pozycja leży
wyżej i dłoń się mieści.

**Strzałka przepływu kotwiczy się w palcu, gdy koliduje z dłonią.** Domyślnie
strzałka panel→panel siedzi na środku przerwy, w stałym paśmie wysokości. Gdy
dłoń z gestem `point` wchodzi w to pasmo (ikona QR w połowie ekranu), ogon
strzałki przecinałby grzbiet dłoni — generator wykrywa kolizję bboxów i wtedy
zaczepia **ogon strzałki tuż przy czubku palca**, skąd zamaszyście wpada w
następny panel. To rozwiązanie samego grafika (KROK 04c: dotknij ikony →
otwiera się skaner) i jest stabilne przy podmianie zrzutów per locale, bo
podąża za celem.

## Figura generowana od zera

Kiedy przepływ w aplikacji zmienia się na tyle, że panele grafika opisują inne
ekrany, taniej jest **wygenerować figurę** niż łatać wektory. Tak powstał
rozdział 05: `tools/svg_build_panels.py`, tablica `FIGURES` na górze pliku
mówi, jaki zrzut i jaki numer trafia w który panel.

Skrypt składa moduł z rozdziału 03 (741.6 × 1629, promień 50.4, obudowa 14.4,
rozstaw 854.17), dokłada obudowę, osadza font i **wypożycza dłoń oraz strzałkę
z pliku grafika**, żeby rysunek został w jego języku. Zrzut wpasowuje w moduł
przez `min(W/w, H/h)` i dopełnia kolorem pobranym z piksela (2,2) samego zrzutu
— zrzuty z suite'u mają różne proporcje (0.442 do 0.488 przy module 0.455), więc
bez dopełnienia trzeba by kadrować.

Pięć rzeczy, które kosztowały przebieg:

**Zrzut normalizuj, bo suite jest niespójny.** Ze 162 zrzutów w
`docs/manual/pictures/` **96 ma już wklejoną obudowę telefonu** (zwykle 8 px,
jeden 30 px) — i to dokładnie w kolorze `#d4c4af`, czyli naszym. Pozostałe 66 to
gołe ekrany. Wklejenie nieznormalizowanego zrzutu w naszą obudowę rysuje ramkę
**dwa razy**; w skali decku czyta się to jako gruby ciemny kontur i tak właśnie
wyglądał pierwszy podchód do rozdziału 05. Mierz obwódkę na czterech krawędziach
i przycinaj tylko wtedy, gdy jest jednakowa — `unframed()` w generatorze.

Sam crop nie wystarcza: rogi ekranu w obudowanym zrzucie są łukami o promieniu
większym niż grubość obwódki, więc po prostokątnym przycięciu w każdym rogu
zostaje ćwiartka łuku wypełnienia ramki plus przezroczysty klin za nią. Zrzut
jest letterboxowany, więc te kliny lądują głęboko wewnątrz modułu — clip bezela
ich nie zakryje — i figura wygląda jak „telefon w telefonie" (tak wyglądał
pierwszy `step03-a.pl`). `square_corners()` w generatorze zamalowuje kliny
kolorem prostej krawędzi ekranu obok; odpala się automatycznie po każdym
udanym cropie ramki.

**Dłoń nie sięga dolnej piątej części ekranu.** Ma 46% szerokości ekranu, czubek
palca w lewym górnym rogu, korpus ciągnie w prawo-dół. Położona na cel przy dolnej
krawędzi — dolna nawigacja, pasek akcji — zwisa 200 jednostek pod telefonem i
podbija figurę, a wyższa figura renderuje się **mniejsza** (patrz niżej). Obrót
o 180° mieści ją w panelu, ale wtedy korpus zasłania treść nad celem i gest
przestaje być czytelny. Próg `HAND_REACH = 0.80`: wyżej dłoń, niżej zakręcona
strzałka, która trafia grotem w cel i nie zajmuje wysokości.

Trzy pozostałe:

**Gesty idą na wierzch, osobną warstwą.** Strzałka dopisana zaraz za swoim
panelem zostaje zamalowana przez panel następny — grot znika, zostaje ogon.
Grafik trzyma wszystkie dłonie i strzałki w jednej grupie po wszystkich
obrazkach; rób tak samo.

**Czubek palca mierz, nie szacuj — i sprawdź, gdzie w ogóle jest palec.**
Anatomia tej dłoni kosztowała cały wieczór: lewy górny róg kształtu to
**grzbiet zaciśniętej dłoni**, palec wskazujący biegnie w **prawo-dół** i
kończy się aureolą dotyku (dwa łuki wokół opuszka). Punkt dotyku = środek tej
aureoli, zmierzony na rastrze jako centroid komponentów łuku (tego, co nie
jest samą dłonią): `HAND_TIP = (271.0, 254.2)` względem bboxa. Kotwiczenie
lewego górnego rogu kładło grzbiet dłoni na kontrolce, a palec wskazywał w
nic — i przez trzy iteracje wyglądało to "prawie dobrze", bo dłoń bywała
blisko. Nowego kształtu nie przyjmuj bez renderu całej dłoni i pomiaru na nim.

**Cel mierz na naszym zrzucie, nigdy nie przenoś od grafika.** Jego zrzuty
układały te same ekrany inaczej, więc jego ułamki stawiają dłoń **obok**
naszej kontrolki — to kosztowało trzy nieudane podejścia do 04.2/04.5/04.8/04.11.
Procedura: `--grid <zrzut>` nakłada siatkę 0.05 i z niej odczytujesz środek
kontrolki jako ułamek znormalizowanego obrazu; `--debug` rysuje celownik na
każdym celu — widoczny czubek palca ma go dotykać. Obie flagi są w
`tools/svg_build_panels.py`; każda zmiana celu przechodzi przez render z
`--debug` przed czystym buildem.

**Wysokość figury steruje wielkością paneli w decku.** `.plate img` ma
`max-height: min(62vh, 640px)` i `object-fit: contain`, więc figura wyższa w
proporcjach renderuje się **mniejsza**, nie większa. Dłoń grafika trzyma czubek
palca w górnym-lewym rogu, a korpus ciągnie w prawo-dół — położona na cel przy
dolnej krawędzi ekranu zwisa 200 jednostek pod telefon i podbija figurę o 11%.
Obrót o 180° robi z niej dłoń naciskającą z góry, która mieści się w panelu.
Trzymaj proporcje figur rozdziału w okolicy 1.4–1.9, tak jak sąsiednie.

## Zrzuty per locale

Zrzuty żyją w `docs/assembly/shots/<locale>/`, a generator rozwiązuje je z
fallbackiem: locale → `en` → `docs/manual/pictures/` (wspólne źródło suite'u,
dopóki jest jednojęzyczne). Figura zbuduje się więc dla każdego locale od razu i
poprawia się w miarę zapełniania katalogu. Na koniec przebiegu generator wypisuje,
których zrzutów w danym locale **nie było** — wariant złożony w całości z
fallbacku nie ma prawa wyglądać jak gotowe tłumaczenie.

```bash
python3 tools/svg_build_panels.py              # figury bazowe (fallback)
python3 tools/svg_build_panels.py --locale pl  # tylko figury z własnym zrzutem
```

Wariant locale powstaje **tylko dla figur, w których locale ma choć jeden
własny zrzut** — figura złożona w całości z fallbacku byłaby bajtowym
duplikatem bazowej, więc generator ją pomija i to wypisuje. Dzisiaj jedyny
wariant to `step03-a.pl.svg` (polski ekran powitalny).

**Panel bez zrzutu w suite dostaje wektorowy zastępnik** z `tools/assets/`:
skaner QR (`scanner-screen`, nigdy nie zrzucany) i ekran powitalny
(`welcome-screen`, wyjęty z wektora grafika — suite ma go tylko po polsku).
W tablicy `FIGURES` panel deklaruje `"shot"` **i** `"vector"`: zrzut wygrywa,
gdy się rozwiąże dla locale, inaczej wchodzi wektor. Cel gestu dla wektora to
osobny klucz `"vpoint"`, bo zastępnik układa ekran inaczej niż zrzut. Każdy
asset ma własny prefiks klas (`sc-`, `ws-`), żeby nie kolidował ze stylami
figury.

W decku `<img data-fig="step05-a">` plus tablica `FIG_LOCALES` w `index.html`:
locale dopisujesz **dopiero** gdy jego build jest zacommitowany, i wtedy
`syncLang()` zaczyna go podawać. Locale spoza listy dostaje `<stem>.svg`, czyli
angielski fallback — atrybut `src` w markupie też nim jest, więc druk i strona
bez JS działają bez zmian.

Dwie rzeczy, na które uważać przy podmianie:

**Cel dotknięcia trzymaj jako ułamek ekranu, nie piksel.** Niemiecki zrzut tego
samego ekranu ma ten sam układ, więc `(0.855, 0.965)` dalej wskazuje przycisk
zapisu, a `(348, 875)` już nie, gdy zrzut ma inny rozmiar.

**Porównuj `getAttribute('src')`, nie `img.src`.** Właściwość zwraca URL
absolutny i nigdy nie zrówna się z relatywną ścieżką, więc każde przełączenie
języka podmieniałoby atrybut i odpalało animację odsłaniania od nowa.

**Standalone i PDF-y nie mają `figs/`.** `syncFigures()` liczący ścieżki
`figs/…` podmieniał w wersji standalone wlane `data:` URI na ścieżki, których
plik offline nie rozwiąże — polski PDF wyszedł z ikoną zepsutego obrazka
zamiast rozdziału 03, a **każda** figura `data-fig` łamała się przy pierwszym
biegu synchronizacji. Dlatego `syncFigures()` zapamiętuje bazowe `src` przy
pierwszym biegu i wraca do niego, a wariant locale bierze najpierw z atrybutu
`data-src-<locale>` — `build_standalone.py` wlewa tam każdy wariant wymieniony
w `FIG_LOCALES`. Po każdej zmianie figur odpal `build_standalone.py`, potem
`build_pdf.py`, i **obejrzyj stronę z figurą** w co najmniej jednym PDF-ie
(`pdftoppm -f N -l N -png`): rozmiar PDF-a, który spadł o kilka MB, to sygnał,
że figury przestały się drukować.

## Numeracja kroków

**Stara paczka: krzywe.** Etykiety `03.4` i podobne to krzywe, a cyfry są
osobnymi ścieżkami o powtarzalnych wymiarach (`0` = 38 × 53, `3` = 35 × 53).
Zmiana numeru to **przeszczep glifu**: sklonuj potrzebną cyfrę, nadaj jej
`transform="translate(dx 0)"` na pozycję starej, starą usuń. Jeśli usuwasz panel,
którego etykieta zawiera potrzebną cyfrę — **sklonuj ją zanim skasujesz**.

**Nowa paczka: żywy `<text>`.** Renumeracja jest wtedy zwykłą podmianą treści —
ale wchodzi za to pułapka, która nie boli od razu:

```css
.cls-2 { font-family: Lato-Semibold, Lato; font-size: 72px; font-weight: 600; }
```

**SVG wczytany przez `<img>` jest dokumentem izolowanym.** Nie dziedziczy krojów
strony i nie pobierze webfontu — deklaracja `Lato-Semibold` znaczy tyle, co
„weź z systemu albo trudno". Lato nie ma ani na tej maszynie, ani w CI, więc
numery leciały na `DejaVu Sans`, podczas gdy krzywe w rozdziale 03 wyglądały
poprawnie. Efekt: **te same numery renderowały się inaczej u każdego czytelnika
i inaczej w PDF-ie**, mimo że w źródle reguła była identyczna.

Lekarstwo — **osadzić krój w SVG**. Numery używają jedenastu znaków, więc subset
waży tyle co nic:

```bash
apt-get download fonts-lato python3-fonttools     # brak pip w tym venv
dpkg-deb -x fonts-lato_*.deb lato && dpkg-deb -x python3-fonttools_*.deb ft
PYTHONPATH=ft/usr/lib/python3/dist-packages python3 -m fontTools.subset \
  lato/usr/share/fonts/truetype/lato/Lato-Semibold.ttf \
  --text="0123456789. " --output-file=lato-sb-digits.ttf --no-hinting
# 676 KB -> 4.8 KB; base64 w <style> jako @font-face = +6.5 KB na plik
```

`@font-face` z nazwą rodziny `Lato-Semibold` wstaw na początek `<style>` — jest
pierwsza na liście `font-family`, więc wygrywa i **nie trzeba ruszać `<text>`**.
Gotowiec z subsetem w komplecie: `tools/svg_embed_font.py` (też pomija pliki,
które `@font-face` już mają).
Sprawdzian jest ilościowy: wyrenderuj numer z krzywych obok numeru z `<text>`
i zmierz bounding box. Wyszło 276 × 106 przeciw 275 × 106 — to jest zgodność.

`build_pdf.py` renderuje przez headless Chrome, więc osadzenie naprawia PDF-y
tym samym ruchem.

## Teksty i języki

**Instrukcja ma 20 locale, aplikacja ma 8** (`de en es fr it no pl tr`, katalog
`packages/apisense_core/l10n/`). Reguła, którą przyjęliśmy:

- dla tych ośmiu — etykieta w języku locale, **wzięta wprost z `app_*.arb`**,
  nie przetłumaczona,
- dla pozostałych dwunastu — **angielski**, bo aplikacja pokazuje im angielski
  fallback i instrukcja ma opisywać to, co użytkownik widzi na ekranie.

Nazwy własne zostają wszędzie bez tłumaczenia: **Hub, ColonyLink, VitalSensor,
Scale, NFC, Apisense Pro AI**.

Zastrzeżenie z `audyt-instrukcji.md` obowiązuje i tutaj: **wartość w ARB nie
jest dowodem, że etykieta jest wyrenderowana**. Dwie z trzech rozbieżności
znalezionych w tym przebiegu potwierdził dopiero zrzut ekranu — `Verification
Code` w instrukcji okazało się `Confirmation code` w aplikacji. Zostały jeszcze
dwie niepotwierdzone: instrukcja mówi `Add beehive` i `Beehive`, ARB mówi
`Add Hive` i `Hive`.

Etykiety pól w listach kroków (`<li><b>Username</b>`) były wspólne dla
wszystkich locale. Rozbicie ich na per-locale spany działa — przełącznik chowa
`[lang]` niezależnie od zagnieżdżenia, a kolumna etykiet w `.micro` rośnie do
treści.

## Weryfikacja

```bash
python3 -m http.server 8899 --directory docs    # podgląd: /assembly/
python3 tools/check_i18n.py                     # komplet spanów w 20 locale
python3 tools/check_labels.py                   # etykiety UI vs ARB + reguła 8/12
python3 tools/check_anchors.py --against main
python3 tools/check_image_refs.py --against main

python3 tools/svg_embed_font.py                 # @font-face tam, gdzie żyje <text>
python3 tools/svg_add_bezel.py                  # obudowa telefonu w rozdziale 04
```

Oba skrypty `svg_*` są idempotentne — puść je po każdej nowej paczce od grafika
i przeczytaj, co pominęły.

`check_image_refs.py` skanuje wyłącznie markdown w `docs/`, więc instrukcji
montażu **nie pilnuje** — to HTML. Zmiany nazw plików w `figs/` trzeba
sprawdzić ręcznie: `grep -o 'figs/[a-z0-9-]*\.\(webp\|svg\)' docs/assembly/index.html`.

Podgląd oglądaj w kilku locale, nie tylko w polskim. Najdłuższe etykiety mają
niemiecki i francuski, a arabski i grecki jadą osobnymi krojami
(patrz `adr/0003-kroje-greka-arabski.md`).

## Waga

Zrzuty w base64 są ciężkie, a `build_standalone.py` wkleja wszystko do jednego
HTML-a wysyłanego mailem. Przed wdrożeniem:

- przeskaluj zrzut do rozsądnej rozdzielczości — panel renderuje się przy ~742
  jednostkach, więc źródło 1712 px jest przeszło dwukrotnie przesamplowane,
- przepuść SVG przez `svgo`.

Dla porównania: podmiana rysunku listy pasiek (1712 × 3684, 844 KB) na kafelek
zasilania Huba zbiła plik z 888 KB na 452 KB.

## Stan i co dalej

Rozdziały **01–04 przerobione**. Druga dostawa od grafika (`svg en/`) naprawiła
pięć plików, które wcześniej miały zepsute linki do `../instrukcja/instrukcja/EN/*.png` —
zrzuty są w nich osadzone jako `data:` URI.

Po tej dostawie doszły dwa wyrównania stylistyczne, oba opisane wyżej:
**obudowa telefonu** dorysowana czternastu panelom rozdziału 04 i **osadzony
Lato-Semibold** w pięciu plikach z żywym `<text>`.

Rozdziały **02, 03, 04 i 05 są generowane** przez `tools/svg_build_panels.py` —
jedna komenda. Rozdział 01 (kody QR sklepów + badge App Store / Google Play) i
`montaz-systemu-animated.svg` (etykiety: Hub, VitalSensor, Scale, „1–2 m" —
same nazwy własne i miara) **nie zawierają treści zależnych od języka** i
zostają statyczne. `step04-colonylink-qr.svg` trzyma ekran skanera po
angielsku tą samą decyzją, co wektorowy asset skanera. Pliki grafika przestały
być źródłem i stały się wynikiem:
jego zrzuty wyciągnięte do `docs/assembly/shots/en/`, kształty do `tools/assets/`,
a układ do tablicy `FIGURES`. Rozdział 05 dostał przy okazji bieżące ekrany
zamiast wektorowych odtworzeń ze starej paczki, razem z nieaktualnymi etykietami
`Verification Code`, `Add beehive` i `Beehive no. 1`.

Zrzuty grafika niosą **pary „pusty → wypełniony"** dla każdego urządzenia —
z wyszarzonym przyciskiem dalej po lewej i żółtym po prawej. Suite ma po jednym
stanie na ekran, więc odtworzenie rozdziału 04 z suite'u skasowałoby ten kontrast.
Dlatego #81 musi prosić o **stany**, nie tylko o języki.

Zmienił się też opisywany przepływ, nie tylko etykiety: wyposażenie to teraz
**trzy osobne ekrany w stałej kolejności ColonyLink → VitalSensor → Scale**, a
przycisk zapisu siedzi na ostatnim z nich. Dla rozdziału 05 to sedno — ekran
Scale przechodzisz pusty i to z niego zatwierdzasz ul. Kanon jest w
`docs/manual/app-manual.*` §2.1–§2.1.3; stamtąd bierz przepływ, nie z poprzedniej
treści decku.

Uwaga na zrzut `add_beehive_devices_colonylink.png`: niesie komunikat
*„ColonyLink is optional on your plan"*, który zależy od planu abonamentowego.
Treść decku celowo tego nie powtarza.

Otwarte: **#81** — zrzuty dla instrukcji montażu we wszystkich ośmiu językach
aplikacji. Do czasu realizacji deck ma zrzuty mieszane językowo, a warstwa
tekstowa jest już kompletna w dwudziestu.
