# ADR 0003: Krój dla greki i arabskiego (Poppins ich nie ma)

Data: 2026-07-31 · Status: **zaakceptowany częściowo** 2026-07-31 — przyjęto
wariant 1 **w części greckiej**: Noto Sans, subset `greek`, cztery grubości,
wpięte przez `:lang(el)`. Wdraża to #63.

**Arabski jest odroczony, nie odrzucony.** Ten ADR sam czyni `ar` warunkowym
(patrz „Decyzja"), a warunek — RTL, #52 — nie jest spełniony. Cairo wchodzi
razem z układem dwukierunkowym albo wcale; font bez RTL dałby tekst poprawnie
ukształtowany w układzie odbitym na opak, czyli regres gorszy niż brak
arabskiego. Do tego czasu z tego dokumentu obowiązuje wyłącznie połowa grecka:
**+117 040 B**, nie +284 944 B.

## Kontekst

Epik #47 rozszerza `docs/assembly/index.html` do 20 locale. Dwa z nich — `el`
i `ar` — nie mają w czym się wyświetlić. Poppins jest jedynym krojem tej strony
(13 reguł `font-family: Poppins` w arkuszu) i **nie ma glifów greckich ani
arabskich**.

Sprawdzone nie po nazwie subsetu, tylko po `cmap` rozpakowanych woff2 (subset
nazwany `greek` bywa niepełny — nazwa nie jest dowodem). Poppins z
`css2?family=Poppins:wght@200;300;400;500;600` (User-Agent desktopowy, jak
w `tools/build_standalone.py`) zwraca trzy subsety — `devanagari`, `latin`,
`latin-ext`, razem 15 plików woff2. Wynik przecięcia:

- **0/69** znaków współczesnej greki (24 wielkie + 24 małe + ς + akcentowane
  ά έ ή ί ό ύ ώ ΐ ΰ ϊ ϋ + Ά Έ Ή Ί Ό Ύ Ώ Ϊ Ϋ) — w żadnym z 15 plików.
- **0/58** znaków arabskiego (28 liter bazowych + ء أ إ آ ؤ ئ ة ى + tatweel +
  8 harakat + cyfry ٠–٩ + ، ؛ ؟) — w żadnym z 15 plików.
- Tabela `GSUB` Poppins deklaruje skrypty `DFLT`, `deva`, `dev2`. Nie ma `grek`,
  nie ma `arab`. Brak też jakichkolwiek cech kształtowania (`init`/`medi`/`fina`).

To nie jest kwestia `KEEP_SUBSETS` w `tools/build_standalone.py` — tam nie ma
czego dołożyć. Pozostałe języki epiku mieszczą się w obecnym
`("latin", "latin-ext")` bez zmian.

Ograniczenie kosztowe: bundle standalone (`python3 tools/build_standalone.py`)
ma dziś **3 388 103 B (3,231 MiB)** i trzyma fonty jako base64, żeby działał
offline z załącznika mailowego. Base64 puchnie o 4/3 — 10 obecnych krojów
Poppins to 67 088 B surowo, 89 464 B w bundlu.

**Jedna rodzina nie załatwi sprawy.** Z 1942 rodzin w katalogu Google Fonts
tylko **5** deklaruje jednocześnie subset `greek` i `arabic`: Alyamama (szeryfowa),
Cascadia Code i Cascadia Mono (monospace), Handjet (display, pikselowa),
Oi (display, tłusta). Żadna nie jest krojem tekstowym bezszeryfowym. Wariant
„jedna rodzina na wszystko" nie istnieje — każdy wariant to dwie rodziny, pytanie
tylko czy obok Poppins, czy zamiast.

## Decyzja (proponowana)

**Wariant 1 — osobna rodzina tylko dla `el` i `ar`**, wpięta przez `:lang(el)` /
`:lang(ar)`:

- `el` → **Noto Sans**, subset `greek`, **4 grubości** (300/400/500/600)
- `ar` → **Cairo**, subset `arabic`, **4 grubości** (300/400/500/600)

Cztery grubości, nie pięć: waga 200 obsługuje w całej stronie wyłącznie regułę
`.ghost` — wielki numer kroku, `aria-hidden="true"`, treść to cyfry zachodnie
`00`–`07` i znak `✱`. Nigdy tekst tłumaczony. Grecki i arabski nie potrzebują
wagi 200 w ogóle; to −20% kosztu na starcie.

`unicode-range` nowych krojów ogranicza je do bloku greckiego / arabskiego, więc
**łacinka wewnątrz tekstów el i ar zostaje w Poppins** — nazwy produktów
(„Apisense BOX", „Hub", „VitalSensor") wyglądają wszędzie tak samo. Zero
dodatkowych bajtów za łacinkę Noto/Cairo.

Zmierzony wynik: **3 673 047 B (3,503 MiB), +284 944 B, +8,4%** względem
dzisiejszego bundla.

**Wdrożenie `ar` jest warunkowe.** Strona nie ma dziś żadnej obsługi RTL —
`direction` występuje w arkuszu wyłącznie jako `flex-direction`, nie ma ani
jednego `dir="rtl"`. Font jest najtańszą częścią arabskiego (+164 kB);
przepisanie układu na dwukierunkowy to osobna, większa robota. Jeśli nie ma na
nią miejsca w tej partii, `ar` wypada z partii (wariant 3 dla samego `ar`), a `el`
wchodzi — grecki jest LTR i nie wymaga niczego poza krojem.

## Pomiary

Wszystkie liczby ze świeżo pobranych plików Google Fonts (`css2`, UA desktopowy →
woff2) i z realnie wygenerowanych bundli, nie z szacunków. Data pomiaru:
2026-07-31.

### Rozmiar jednego kroju (subset × grubość)

| Rodzina / subset | B na grubość (surowo) | 4 grubości surowo | 4 grubości w base64 | cmap | pokrycie |
|---|---|---|---|---|---|
| Poppins / `latin` (stan obecny) | 7 748 – 8 000 | 31 472 | 41 968 | 217 | — |
| Poppins / `latin-ext` (stan obecny) | 5 484 – 5 644 | 22 176 | 29 576 | 137 | — |
| **Noto Sans / `greek`** | 21 776 | 87 104 | 116 144 | 125 | **69/69 greki** |
| **Cairo / `arabic`** | 30 896 | 123 584 | 164 784 | 302 | **58/58 arabskiego** |
| Readex Pro / `arabic` | 22 864 | 91 456 | 121 952 | 82 | 58/58 |
| IBM Plex Sans Arabic / `arabic` | 42 848 – 45 688 | 178 880 | 238 512 | 681 | 58/58 |
| Noto Sans Arabic / `arabic` | 165 960 | 663 840 | 885 120 | 1226 | 58/58 |

Wszyscy czterej kandydaci arabscy mają w `GSUB` skrypt `arab` z cechami
`init`/`medi`/`fina`/`rlig` — kształtowanie kontekstowe jest w foncie, nie
zależy od dodatkowych glifów w cmap.

### Bundle — zmierzony, plik po pliku

Punkt odniesienia: **3 388 103 B (3,231 MiB)**.

| Wariant | Bundle | Przyrost | % |
|---|---|---|---|
| `el`: Noto Sans greek, 4 grubości | 3 505 143 | +117 040 | +3,5% |
| `el`: Noto Sans greek, 5 grubości | 3 534 403 | +146 300 | +4,3% |
| `el`: Noto Sans greek + latin, 4 grubości | 3 697 475 | +309 372 | +9,1% |
| `ar`: Readex Pro, 4 grubości | 3 513 195 | +125 092 | +3,7% |
| `ar`: Cairo, 4 grubości | 3 556 007 | +167 904 | +5,0% |
| `ar`: Cairo, 5 grubości | 3 597 983 | +209 880 | +6,2% |
| `ar`: IBM Plex Sans Arabic, 4 grubości | 3 629 795 | +241 692 | +7,1% |
| `ar`: Noto Sans Arabic, 4 grubości | 4 276 387 | +888 284 | +26,2% |
| `ar`: Noto Sans Arabic, 5 grubości | 4 498 458 | +1 110 355 | +32,8% |
| **Wariant 1 (rekomendacja): Noto Sans greek + Cairo, 4 grubości** | **3 673 047** | **+284 944** | **+8,4%** |
| Wariant 1 z 5 grubościami | 3 744 283 | +356 180 | +10,5% |
| Wariant 1 z Noto Sans Arabic zamiast Cairo, 4 grubości | 4 393 427 | +1 005 324 | +29,7% |
| Wariant 2: Poppins **usunięty**, Noto Sans (latin+latin-ext+greek) + Noto Sans Arabic, 5 grubości | 5 913 604 | +2 525 501 | **+74,5%** |
| Wariant 2 tańszy: Poppins **usunięty**, Cairo (latin+latin-ext+arabic) + Noto Sans greek, 5 grubości | 3 991 029 | +602 926 | +17,8% |
| Wariant 3: rezygnacja z `el` i `ar` | 3 388 103 | 0 | 0% |

Wariant 2 w wersji Noto puchnie nie od greki ani arabskiego, tylko od łacinki:
subset `latin-ext` Noto Sans waży **167 960 B na grubość** wobec 5 524 B
w Poppins — 30×. Do tego `arabic` Noto Sans Arabic 165 960 B na grubość.

### Czego **nie** zmierzono

- **Nie ma jeszcze tłumaczeń `el` i `ar`** (`tools/i18n/` zawiera dziś es, it, no,
  tr). Pokrycie liczone przeciwko kanonicznemu repertuarowi obu pism, nie
  przeciwko realnym stringom instrukcji. Po dostarczeniu tłumaczeń warto
  powtórzyć przecięcie na faktycznym tekście.
- **Nie renderowano strony** z tekstem greckim/arabskim w przeglądarce ani nie
  drukowano PDF-a (`tools/build_pdf.py`). Kształtowanie arabskiego potwierdzone
  tylko z tabel `GSUB`, nie z pikseli.
- Nie oceniano, jak Cairo i Noto Sans wyglądają obok Poppins w realnym składzie —
  to ocena projektowa, nie pomiar.

## Rozważone alternatywy

| Opcja | Werdykt | Powód |
|---|---|---|
| **Wariant 1: Noto Sans (el) + Cairo (ar), 4 grubości** | **rekomendowana** | +284 944 B (+8,4%); pełne pokrycie obu pism; Poppins zostaje krojem marki w 18 locale i w łacince pozostałych dwóch |
| Wariant 1 z Readex Pro zamiast Cairo | odrzucona (druga w kolejności) | tańsza o 42 812 B, ale subset `arabic` ma tylko 82 punkty kodowe wobec 302 w Cairo — margines na znaki spoza naszego repertuaru jest cienki; Cairo jest bezpieczniejsze za ~42 kB |
| Wariant 1 z Noto Sans Arabic | odrzucona | +888 284 B za sam arabski (26% bundla) przy tym samym pokryciu naszego repertuaru co Cairo; 1226 punktów kodowych, których nie użyjemy |
| Wariant 1 z IBM Plex Sans Arabic | odrzucona | +241 692 B, dobre pokrycie, ale krój wyraźnie „IBM-owy" — gorzej dobiera się do geometrycznego Poppins niż Cairo |
| Wariant 1 z 5 grubościami | odrzucona | +71 236 B za wagę 200, której w greckim i arabskim nie da się użyć: jedyny jej konsument to `.ghost` z cyframi zachodnimi |
| Wariant 1 + łacinka Noto Sans w `el` | odrzucona | +192 332 B za to, żeby „Apisense BOX" w greckiej wersji wyglądało inaczej niż we wszystkich pozostałych |
| **Wariant 2: zmiana kroju globalnie** | odrzucona | **cała instrukcja idzie do przeskładania** (13 reguł, wszystkie kroje nagłówków, `.ghost`, letter-spacingi dostrojone pod Poppins) i strona przestaje pasować do identyfikacji Apisense — to koszt, nie przypis. Do tego +74,5% bundla w wersji Noto albo +17,8% w wersji Cairo. Nie kupuje nawet spójności: żaden tekstowy bezszeryf w Google Fonts nie ma łacinki, greki i arabskiego naraz (5 rodzin ma oba pisma, wszystkie to szeryfówka, monospace albo display) — dwie rodziny zostają tak czy owak |
| **Wariant 3: rezygnacja z `el` i `ar`** | odrzucona dla `el`, **otwarta dla `ar`** | grecki kosztuje 117 040 B i nic poza tym — rezygnacja byłaby nieuzasadniona. Arabski kosztuje 167 904 B fontu **plus** obsługę RTL, której strona nie ma; jeśli RTL nie mieści się w tej partii, `ar` przechodzi do następnej |
| Subsetowanie fontów pod faktyczny tekst (`text=` w Google Fonts / pyftsubset) | odrzucona na teraz | ścięłoby grekę i arabski do ~10–20 kB łącznie, ale wiąże bundle z konkretnym stringiem: każda korekta tłumaczenia wymaga przegenerowania fontu, a brakujący glif wypada cicho. Do rozważenia osobno, jeśli 3,5 MiB okaże się za dużo na załącznik |

## Konsekwencje

- **Strona świadomie miesza kroje.** W wersji greckiej i arabskiej jedno zdanie
  może nieść glify z dwóch rodzin: pismo rodzime z Noto Sans / Cairo, łacińskie
  nazwy produktów z Poppins. To wybór, nie niedopatrzenie — alternatywą jest
  albo +192 332 B za łacinkę Noto w `el`, albo utrata Poppins w nazwach marki.
  Różnice wysokości x i grubości kreski będą widoczne przy bezpośrednim
  sąsiedztwie; jeśli okażą się rażące, korekta idzie przez `font-size-adjust`
  na `:lang(el)`/`:lang(ar)`, nie przez zmianę rodziny.
- Bundle standalone rośnie z 3,23 do 3,50 MiB. Nadal jeden plik, nadal offline,
  nadal do maila.
- `tools/build_standalone.py` przestaje mieć jedną listę `KEEP_SUBSETS` i jeden
  `FONT_CSS` — musi pobrać trzy arkusze i filtrować subsety per rodzina. To
  zmiana strukturalna w tym pliku, nie dopisanie stringa.
- `tools/build_pdf.py` (`LOCALES`) i `tools/check_i18n.py` (`DEFAULT_LOCALES`)
  dostają `el`, a `ar` tylko razem z RTL.
- Arabski bez RTL byłby regresem gorszym niż jego brak: tekst wyświetliłby się
  poprawnie ukształtowany, ale w układzie odbitym na opak. Dlatego `ar` jest
  warunkowe.
- Poppins zostaje krojem Apisense. Ta decyzja niczego w identyfikacji nie zmienia
  — i o to chodzi.

## Aktualizacja po scaleniu gałęzi integracyjnej (2026-07-31)

Ten ADR zmierzono, zanim wylądowało dziewięć łacińskich locale. Wnioski się nie
zmieniły, ale dwie liczby bazowe już nie opisują repo, więc podaję je świeże —
pomiary greki i arabskiego zostają nietknięte, bo dotyczą plików Google Fonts,
a nie tej gałęzi.

- Baza bundla to dziś **3 494 225 B (3,332 MiB)**, nie 3 388 103 B. `index.html`
  to **259 494 B**, nie 154 185 B.
- Koszt dwóch rodzin (**+284 944 B**) jest niezależny od liczby locale — to
  fonty, nie tekst. Względem nowej bazy daje to **+8,2%** zamiast +8,4%, a bundle
  po wdrożeniu **3 779 169 B (3,604 MiB)** zamiast 3,503 MiB.
- Zdanie „Epik #47 rozszerza stronę do 20 locale" opisuje zamówienie, nie stan.
  Gałąź dowozi **17**: `el` i `ar` (#63, #64) czekają na akceptację tego ADR-a,
  `pt` (#62) na ADR 0004. Status pozostaje **proponowany** — nic z tego nie jest
  wdrożone i nie powinno być, dopóki właściciel identyfikacji się nie wypowie.

## Sprostowanie po wdrożeniu części greckiej (#63, 2026-07-31)

Akapit wyżej jest już nieaktualny w jednym zdaniu: część grecka **została
wdrożona**, zgodnie ze statusem z nagłówka („zaakceptowany częściowo").
Decyzja się nie zmienia — poniżej tylko to, co ADR wprost zostawił
niezmierzone, uzupełnione realnymi liczbami. `ar` nadal nietknięty.

**Pokrycie na faktycznym tekście** (sekcja „Czego nie zmierzono" prosiła
o powtórzenie przecięcia po dostarczeniu tłumaczeń). Liczone na wydrukowanym
PDF-ie, per znak, a nie na tekście źródłowym — bo `text-transform: uppercase`
produkuje znaki, których w `tools/i18n/el.json` nie ma (ό → Ό). W dokumencie
renderuje się **57** różnych punktów kodowych greckich; wszystkie 57 rysuje
Noto Sans i wszystkie 57 są w cmapie osadzonego subsetu `greek`. Zero
łacinki i cyfr rysuje Noto Sans, zero greki rysuje Poppins. Sam tekst
źródłowy (spany + HEAD_TEXT + endonim) ma 50 różnych znaków greckich, też
50/50 — to ta mniejsza liczba, którą dałoby sprawdzenie bez renderu.

**Strona i PDF zostały wyrenderowane** — druga rzecz z tej samej sekcji.
Poza jednym wyjątkiem cały dokument idzie z dwóch zamierzonych rodzin;
`LiberationSans` (fallback systemu) rysuje dokładnie jeden znak, `≤`, tak
samo jak w `pl`. `✱` i `≤` pozostają znane i nienaprawione we wszystkich
locale.

**Rozmiar.** Baza urosła jeszcze raz od poprzedniej aktualizacji: bundle
przed zmianą to **3 503 753 B**, nie 3 494 225 B. Sama część grecka kosztuje
**+118 852 B** wobec przewidywanych +117 040 B (różnica +1,5% — to Google
Fonts, nie błąd rachunku; woff2 waży dokładnie 21 776 B na grubość, jak
w tabeli). Po dołożeniu tłumaczenia bundle ma **3 641 593 B**.

**Mechanizm łacinki wyszedł prostszy, niż zakładała „Decyzja".** ADR pisał
o `unicode-range` ograniczającym nowy krój do bloku greckiego. W praktyce
wystarczył sam porządek stosu — `Poppins, 'Noto Sans', …` — bo dopasowanie
fontu w CSS działa per znak, a Poppins nie ma greki (0/69). `unicode-range`
i tak przychodzi z Google Fonts i działa jako druga warstwa. Własny
`@font-face` z ręcznie wpisanym zakresem nie był potrzebny i byłby kosztem
utrzymania. Efekt jest ten, który ADR obiecywał: „Apisense BOX", „Hub",
„VitalSensor", „ColonyLink" w wersji greckiej rysuje Poppins.
