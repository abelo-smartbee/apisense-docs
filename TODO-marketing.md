# TODO dla marketingu — materiały do instrukcji montażu Apisense BOX

**Czego dotyczy:** `Apisense_Box_Assembly_Instruction.pdf` (InDesign, 10 stron A4) oraz wersja online `docs.apisense.ai/assembly/`
**Źródło prawdy dla treści:** `docs/manual/configuration/index.pl.md` + `quick-guide.pl.md` (plus poprawki produktowe niżej)
**Stan:** PDF opisuje **poprzednią generację sprzętu**. Wersja online została już przepisana według dokumentacji i tymczasowo korzysta z rysunków z `docs/manual/pictures/`. PDF jest ostatnim materiałem niezgodnym z resztą.

---

## Zasada: grafik dowozi **rysunki**, tekst piszemy my

Teksty przestają być robotą grafika. Powód jest praktyczny, nie estetyczny:

- **Tłumaczenia.** Tekst wtopiony w rysunek znaczy, że każdy język to osobny eksport. Dziś PL i EN, docelowo także DE, FR, IT. Tekst w HTML → jeden komplet rysunków, tłumaczenia jako zwykłe stringi.
- **Koszt poprawki.** Wszystkie błędy, które wyszły przy tej rewizji — `Accound` zamiast `Account`, niemiecki podpis w angielskich zrzutach, `info@` zamiast `bee@`, USB-C, baterie — to **tekst**. Dziś każda literówka to ticket do grafika i nowy eksport PDF-u. W HTML to poprawka na minutę.
- **Zmiana nazwy produktu.** `Apisense Tag` → `ColonyLink` wymusiła przerysowanie, chociaż sam rysunek był w porządku. Nazwa w HTML = zmiana w jednym miejscu.
- **Wyszukiwanie i dostępność.** Tekst w HTML jest zaznaczalny, wyszukiwalny, czytany przez czytniki ekranu i indeksowany przez Google. Tekst wtopiony w grafikę nie jest niczym z tego.

### Co zostaje w rysunku, a co idzie do HTML

| W rysunku | W HTML |
|---|---|
| **wymiary i wartości** — `1–2 m`, `30–50°`, `≤ 35 m`, `x < 26 mm` | zdania, instrukcje, opisy kroków |
| linie odniesienia, strzałki, okręgi powiększeń, numery pozycji (`01`, `02`) | tytuły kroków i podpisy pod rysunkami |
| symbole — słońce, dioda, znak zakazu | **nazwy produktów** (Hub, Scale, VitalSensor, ColonyLink) |

Linia podziału jest prosta: **liczba z jednostką zostaje w rysunku** — jest przywiązana do konkretnego miejsca i nie wymaga tłumaczenia. **Proza idzie do HTML.**

Nazwy produktów też prosimy do HTML. To nazwy własne, więc tłumaczenia same w sobie nie wymagają — ale historia `Tag → ColonyLink` pokazuje, że potrafią się zmienić, a wtedy nie chcemy przerysowywać kompletu.

Jeśli jakiś podpis absolutnie musi siedzieć w rysunku, prosimy o **SVG z `<text id="...">`** — wtedy podmieniamy treść przy budowaniu strony, bez ruszania grafiki.

---

## A. Rysunki do przerysowania

### A1. Apisense Hub — bryła urządzenia ⚠️ krytyczne

Obecnie: płaska płytka z dwiema antenami i stopą montażową, przykręcana do daszka ula.
Ma być: moduł z **panelem fotowoltaicznym**, dwie anteny zewnętrzne (BLE i LTE), mocowany na **uchwycie aparatowym** (przegub kulowy).

Referencje w repo: `docs/manual/pictures/hub.png` (render), `hub_installation.png` (zdjęcie w pasiece).

### A2. Scena montażu Huba ⚠️ krytyczne — dziś wprowadza w błąd

Obecny rysunek (strona 4) pokazuje Hub przykręcony do daszka ula. Zgodnie z dokumentacją decyduje **słońce, nie bliskość ula**. Nowy rysunek musi pokazać:

- **1–2 m nad ziemią** — niżej panel nie zbiera dość światła, zwłaszcza zimą
- **nachylenie 30–50°** względem poziomu (min. 20°), panelem ku słońcu, bez zacienienia
- montaż na słupku, drzewie lub drewnianej konstrukcji — **nie do metalu** (zakłóca BLE i LTE)
- w centrum pasieki, **≤ 35 m** od najdalszego ula z VitalSensorem lub Scale
- **obie anteny pionowo do góry** — obecny rysunek jest tu poprawny
- Hub **nie musi** być zamocowany do ula

**Usunąć USB-C z tego kroku.** Hub uruchamia się przez **wystawienie na słońce**; zasila go panel fotowoltaiczny. Obecna scena z wtyczką i podpisem „Charger not included / Ładowarka nie jest dołączona” wypada.

### A3. Apisense Scale — scena montażu

Bryła belki jest OK. Do zmiany:

- „listwa dystansowa" → **drewniana kantówka** (nazwa z dokumentacji)
- Scale ustawiona **prostopadle do ramek** w ulu — obecny rysunek tego nie pokazuje
- kantówka **równolegle** do Scale, w odległości dającej **równomierne rozłożenie ciężaru** ula
- stabilne i równe podłoże, wypoziomowanie — kluczowe dla dokładności pomiaru

Referencja: `docs/manual/pictures/scale_installation.jpg`.

### A4. Apisense VitalSensor — scena montażu ⚠️ krytyczne

Obecny rysunek (strona 7) pokazuje czujnik na beleczce ramki przy ściance ula, z wariantami mocowania `x < 26 mm` / `x > 26 mm` i opaską zaciskową. To inny sposób montażu niż opisany w dokumentacji.

Ma być:

- na **centralnej ramce, w kłębie**, w górnym rogu
- **pionowo**, tak żeby naklejka QR była widoczna od góry po włożeniu ramki
- mocowanie **uchwytami montażowymi do ramki** z zestawu
- ramka w środkowej części korpusu gniazdowego, bez zakłócania wentylacji

Referencje: `docs/manual/pictures/sensor_installation_1.jpg` (czujnik na ramce), `sensor_installation_2.jpg` (ramka w ulu).

**Do potwierdzenia z produktem:** czy warianty `x < 26 mm` / `x > 26 mm` z opaską nadal obowiązują, czy odpadły razem z uchwytami montażowymi.

### A5. Apisense Tag → ColonyLink ⚠️ krytyczne

Cała sekcja „Apisense Tag" (opisz numerem, zawieś na ścianie ula) do zastąpienia. ColonyLink to identyfikator ula z **kodem QR i tagiem NFC**, bez baterii i konfiguracji, umieszczany na **froncie ula**.

**Blokada — rozstrzygnąć przed rysowaniem:** dokumentacja sama sobie przeczy.

- `manual/configuration/index.pl.md` opisuje ColonyLink jako *„wodoodporną naklejkę"*, którą się *„nakleja na front ula"* i *„dociska na całej powierzchni, żeby taśma montażowa dobrze przylegała"*
- `docs/manual/pictures/sensor_tag.jpg` pokazuje **czerwoną zawieszkę na opasce zaciskowej** z kodem QR i numerem SN

Potrzebna decyzja produktowa: naklejka czy zawieszka. Zdjęcie w dokumentacji też wtedy do wymiany.

### A6. Zawartość zestawu — strona 1

Rysunek rozłożenia w kartonie i lista elementów do przerysowania po zmianach A1–A5:

- Hub w nowej bryle (panel PV)
- **ColonyLink** zamiast „Apisense Tag"
- elementy montażowe wprost, zgodnie z dokumentacją: **uchwyt aparatowy** (Hub), **drewniana kantówka** (Scale), **uchwyty montażowe do ramki** (VitalSensor)
- **do potwierdzenia:** czy `Apisense Beeframe Holder` (uchwyt na wyjętą ramkę, strona 10 PDF-u) nadal wchodzi w skład zestawu — nie występuje w `manual/configuration`, więc został na razie usunięty z wersji online

Prosimy o **każde urządzenie także osobno**, na przezroczystym tle — potrzebujemy ich pojedynczo, do kafelków „co jest w pudełku".

### A7. Lokalizacje kodów QR

Close-upy na stronach 3, 5 i 6 pokazują naklejki na starych obudowach. Do przerysowania na aktualnym sprzęcie.

Referencje: `docs/manual/pictures/hub_qr.jpg`, `scale_qr.jpg`, `sensor_qr.jpg`.

### A8. Nowa scena: uruchomienie urządzeń

Krok, którego w PDF-ie nie ma. **Bez wkładania baterii** — Scale i VitalSensor przychodzą z **zamontowanymi bateriami**. Rysunek pokazuje wyłącznie **kontrolę diody** potwierdzającej uruchomienie, a dla Huba **wystawienie na słońce**.

---

## B. Specyfikacja dostawy

### B1. Format

**SVG** (albo AI z konturami do konwersji). Rysunki są liniowe, więc wektor daje ostry obraz na każdym ekranie i plik kilka razy mniejszy od rastra. Raster tylko tam, gdzie grafika jest fotorealistyczna.

### B2. Jeden rysunek = jeden plik

Bez zbiorczych plansz. Strona składa układ sama i musi móc pokazać każdy rysunek osobno, w innej kolejności i w innym rozmiarze niż w PDF-ie.

Nazewnictwo: `hub-montaz.svg`, `scale-montaz.svg`, `vitalsensor-qr.svg`, `zestaw-hub.svg` — bez polskich znaków i spacji.

### B3. Bez prozy w grafice

W rysunku zostają tylko wymiary, symbole, strzałki i numery pozycji (patrz tabela na górze). Żadnych zdań, tytułów kroków ani nazw produktów.

Jeśli podpis musi być w rysunku — SVG z `<text id="...">` i stabilnym `id`, żeby dało się podmienić treść przy budowaniu strony.

### B4. Tło i kadr

Przezroczyste albo białe, bez ramek, bez cieni pod rysunkiem, bez marginesów „na oko". Kadr ciasno do zawartości — odstępy dodaje strona.

Spójny `viewBox` w obrębie serii (np. wszystkie sceny montażu w tej samej proporcji), żeby rysunki równały się na stronie.

### B5. Kody QR

Wektorowo, nigdy jako raster. Muszą zostać **skanowalne po zmniejszeniu** — bez kompresji stratnej na samym kodzie i bez skalowania poniżej czytelności modułu.

### B6. Materiał, który już istnieje

W repo są **animowane SVG aktualnej generacji**, zrobione do dokumentacji:
`docs/manual/pictures/montaz-{systemu,hub,wagi,sensora,colonylink}-animated.svg`

Wersja online używa ich teraz jako rysunków montażowych. Warto potraktować je jako punkt wyjścia albo przynajmniej jako referencję stylu — będzie spójnie między PDF-em a stroną.

---

## C. Decyzja do podjęcia: skąd bierze się PDF

Sprawa osobna od powyższych. Dziś PDF i strona to dwa niezależne dokumenty, które się rozjechały — dokładnie ten problem teraz naprawiamy.

**Wariant 1 — PDF zostaje w InDesign.**
Sensowny, jeśli PDF jest **drukowaną wkładką do pudełka** (spady, CMYK, gramatura, druk). Wtedy tekst dostarczamy jako gotowy dokument tekstowy, a grafik go zalewa. Minus: dwa źródła prawdy dalej istnieją i po jakimś czasie znów się rozjadą.

**Wariant 2 — PDF generowany ze strony.** ✅ rekomendacja, jeśli PDF jest tylko plikiem do pobrania
Strona ma już arkusz do druku, w którym jeden krok = jedna strona. PDF powstaje wtedy jednym poleceniem, w PL i EN, i **nie da się go rozjechać z dokumentacją**, bo pochodzi z tego samego źródła. Grafik dowozi wyłącznie rysunki.

Do rozstrzygnięcia: czy ten PDF jest drukowany do pudełka, czy tylko udostępniany do pobrania. Od tego zależy wariant.

---

## D. Poprawki tekstowe — nasza strona, nie grafika

Zebrane dla kompletności. **Wersja online ma je już naniesione.** Do PDF-u trafią automatycznie w wariancie 2; w wariancie 1 przekazujemy je jako copy deck.

- **Kontakt:** `info@apisense.ai` → `bee@apisense.ai`. Telefon `+48 606 153 759` — potwierdzić, czy aktualny.
- **Literówka:** strona 2, krok 02 — „Create an **Accound**" → „Account".
- **Obcy język w zrzutach:** zrzuty **04.9** (strona 6) i **05.6** (strona 9) mają w polu VitalSensor niemiecki podpis *„Klicken Sie auf das Symbol, um den QR-Code vom Gerät zu scannen."* — reszta jest po angielsku.
- **Kolejność kroków:** konfiguracja w aplikacji → uruchomienie i kontrola diod → **~2 h na pierwszą synchronizację** → dopiero montaż. Obecny PDF montuje od razu po zeskanowaniu kodu.
- **Nazewnictwo:** Hub, Scale, VitalSensor, ColonyLink.
- **Do weryfikacji z zespołem mobile:** formularz „Add beehive" w PDF-ie ma tylko pola *Scale* i *VitalSensor*, a dokumentacja mówi, że ColonyLink skanuje się przy tworzeniu ula. Jeśli w aplikacji jest osobne pole — doszedł krok i potrzebne są nowe zrzuty.

---

## Kolejność prac

| Priorytet | Pozycje | Dlaczego |
|---|---|---|
| **1 — blokuje** | A5 (naklejka czy zawieszka), C (wariant PDF-u) | bez pierwszego nie da się narysować ColonyLinka, bez drugiego nie wiadomo, czy grafik dostaje jeszcze tekst |
| **2 — wprowadza w błąd** | A1, A2, A4 | montaż Huba i VitalSensora na obecnych rysunkach jest niezgodny z zaleceniami |
| **3** | A3, A6, A7, A8 | niepełne albo nieaktualne, ale nie mylące |
| **4 — po naszej stronie** | D | zrobione na stronie, do PDF-u zależnie od wariantu C |
| **do wyjaśnienia** | A4 (warianty 26 mm), A6 (Beeframe Holder), D (pole ColonyLink) | wymaga potwierdzenia z produktem / zespołem mobile |
