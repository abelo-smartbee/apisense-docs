# TODO dla grafika — aktualizacja instrukcji montażu Apisense BOX

**Plik:** `Apisense_Box_Assembly_Instruction.pdf` (Adobe InDesign, 10 stron A4)
**Źródło prawdy dla treści:** `docs/manual/configuration/index.pl.md` + `docs/manual/configuration/quick-guide.pl.md`
**Kontekst:** PDF opisuje poprzednią generację sprzętu. Wersja online (`docs.apisense.ai/assembly/`) została już przepisana według dokumentacji i tymczasowo korzysta z rysunków z `docs/manual/pictures/`. PDF zostaje ostatnim materiałem niezgodnym z resztą.

---

## A. Rysunki sprzętu — do przerysowania

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
- **obie anteny pionowo do góry** — to zostaje bez zmian, obecny rysunek jest tu poprawny
- Hub **nie musi** być zamocowany do ula

Do zachowania: informacja o USB-C i o tym, że ładowarka nie jest dołączona.

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

### A7. Lokalizacje kodów QR

Close-upy na stronach 3, 5 i 6 pokazują naklejki na starych obudowach. Do przerysowania na aktualnym sprzęcie.

Referencje: `docs/manual/pictures/hub_qr.jpg`, `scale_qr.jpg`, `sensor_qr.jpg`.

---

## B. Treść i teksty

### B1. Baterie — brakuje w PDF

Dodać krok: **Scale i VitalSensor zasilają 2 baterie AA**, po włożeniu sprawdzić diodę potwierdzającą uruchomienie.

### B2. Kolejność kroków

Obecny PDF montuje urządzenie od razu po zeskanowaniu kodu. Dokumentacja (`quick-guide`) ustawia to inaczej:

1. konfiguracja w aplikacji (pasieka, ule, kody QR)
2. **uruchomienie urządzeń i kontrola diod**
3. **~2 h — pierwsza synchronizacja**, sprawdzenie odczytów w aplikacji (status *Brak danych* → aktualny)
4. dopiero teraz montaż w pasiece

Sens: pszczelarz wie, że wszystko działa, zanim wejdzie między ule.

### B3. Kontakt

`info@apisense.ai` → **`bee@apisense.ai`** (adres z dokumentacji).
Telefon `+48 606 153 759` — potwierdzić, czy aktualny.

### B4. Literówka

Strona 2, krok 02: „Create an **Accound**" → „Create an **Account**".

### B5. Obcy język w zrzutach ekranu

Zrzuty **04.9** (strona 6) i **05.6** (strona 9) mają w polu VitalSensor niemiecki podpis:
*„Klicken Sie auf das Symbol, um den QR-Code vom Gerät zu scannen."*
Pozostałe zrzuty są po angielsku. Do wymiany na spójną wersję językową.

### B6. Nazewnictwo

Konsekwentnie jak w dokumentacji: **Hub**, **Scale**, **VitalSensor**, **ColonyLink**.

### B7. Ekrany aplikacji — do weryfikacji z zespołem mobile

Formularz „Add beehive" w PDF-ie ma tylko pola *Scale* i *VitalSensor*. Dokumentacja mówi, że **ColonyLink skanuje się podczas tworzenia ula** — jeśli w aplikacji jest dziś osobne pole, doszedł krok do udokumentowania i nowe zrzuty.

---

## C. Format dostawy

### C1. PDF

Bez zmian — wektorowy, InDesign, A4, 300 DPI. Z niego wycinamy rysunki do wersji online.

### C2. Rysunki osobno — bardzo pomoże

Jeśli da się dostarczyć rysunki także **poza PDF-em, jako SVG lub AI**, wersja online użyje wektorów zamiast rastrów: ostrzejszy obraz, kilka razy mniejszy plik, działa na każdym ekranie.

Wtedy: jeden rysunek = jeden plik, białe albo przezroczyste tło, bez ramek i bez podpisów wtopionych w grafikę (podpisy dodaje strona, i tłumaczy je na PL/EN).

### C3. Kody QR

Kody muszą zostać **skanowalne po zmniejszeniu** — bez przeskalowania w dół poniżej czytelności modułu i bez kompresji stratnej na samym kodzie.

### C4. Materiał, który już istnieje

W repo są **animowane SVG aktualnej generacji**, zrobione do dokumentacji:
`docs/manual/pictures/montaz-{systemu,hub,wagi,sensora,colonylink}-animated.svg`

Wersja online używa ich teraz jako rysunków montażowych. Warto je potraktować jako punkt wyjścia albo przynajmniej jako referencję stylu — będzie spójnie między PDF-em a stroną.

---

## Kolejność prac

| Priorytet | Pozycje | Dlaczego |
|---|---|---|
| **1 — blokuje** | A5 (decyzja: naklejka czy zawieszka) | bez tego nie da się narysować ColonyLinka |
| **2 — wprowadza w błąd** | A1, A2, A4 | montaż Huba i VitalSensora na obecnych rysunkach jest niezgodny z zaleceniami |
| **3** | A3, A6, A7, B1, B2 | niepełne albo nieaktualne, ale nie mylące |
| **4 — drobne** | B3, B4, B5, B6 | teksty i literówki |
| **do wyjaśnienia** | A4 (warianty 26 mm), A6 (Beeframe Holder), B7 (pole ColonyLink) | wymaga potwierdzenia z produktem / zespołem mobile |
