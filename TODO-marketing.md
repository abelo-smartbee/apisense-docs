# Instrukcja montażu Apisense BOX — co potrzebujemy od marketingu

Aktualizacja `Apisense_Box_Assembly_Instruction.pdf`. Obecny PDF pokazuje **poprzednią generację sprzętu** — rysunki montażu Huba i VitalSensora są niezgodne z zaleceniami i wprowadzają pszczelarza w błąd.

**Potrzebujemy wyłącznie rysunków. Teksty piszemy my** — tłumaczenia, poprawki i podpisy zostają po naszej stronie.

| Zostaje w rysunku | Nie umieszczać w rysunku |
|---|---|
| wymiary: `1–2 m`, `30–50°`, `≤ 35 m`, `x < 26 mm` | zdania i opisy kroków |
| strzałki, linie odniesienia, okręgi powiększeń, numery pozycji | tytuły i podpisy |
| symbole: słońce, dioda, znak zakazu | nazwy produktów |

---

## Rysunki do dostarczenia

### 1. Hub — bryła urządzenia ⚠️
Płaska płytka z antenami → moduł z **panelem fotowoltaicznym**, dwie anteny, **uchwyt aparatowy** (przegub kulowy).
Referencja: `hub.png`, `hub_installation.png`

### 2. Hub — scena montażu ⚠️
Nie na daszku ula. Ma pokazywać:
- **1–2 m nad ziemią**, nachylenie **30–50°** (min. 20°), panelem ku słońcu, bez zacienienia
- słupek, drzewo lub drewno — **nie metal**
- w centrum pasieki, **≤ 35 m** od najdalszego ula
- obie anteny **pionowo do góry**

Usunąć scenę z wtyczką USB-C i podpisem „Charger not included" — Hub uruchamia się przez wystawienie na słońce.

### 3. Scale — scena montażu
- Scale **prostopadle do ramek**, na stabilnym i równym podłożu
- **drewniana kantówka** (nie „listwa dystansowa") **równolegle**, w odległości dającej równomierne rozłożenie ciężaru

Referencja: `scale_installation.jpg`

### 4. VitalSensor — scena montażu ⚠️
Nie na beleczce przy ściance. Ma być:
- na **centralnej ramce, w kłębie**, w górnym rogu
- **pionowo**, naklejka QR widoczna od góry po włożeniu ramki
- mocowanie **uchwytami montażowymi do ramki**

Referencje: `sensor_installation_1.jpg`, `sensor_installation_2.jpg`

### 5. ColonyLink ⚠️ — zablokowane, patrz „Do potwierdzenia"
Zastępuje całą sekcję „Apisense Tag" (opisz numerem, zawieś na ścianie). ColonyLink: kod QR + NFC, na **froncie ula**, bez baterii i konfiguracji.

### 6. Zawartość zestawu — strona 1
Rozłożenie w kartonie po zmianach 1–5, plus **każde urządzenie osobno na przezroczystym tle** (potrzebne do kafelków „co jest w pudełku").

Elementy montażowe pokazać wprost: uchwyt aparatowy (Hub), drewniana kantówka (Scale), uchwyty montażowe do ramki (VitalSensor).

### 7. Lokalizacje kodów QR
Close-upy naklejek na **aktualnych obudowach** — Hub, Scale, VitalSensor.
Referencje: `hub_qr.jpg`, `scale_qr.jpg`, `sensor_qr.jpg`

### 8. Nowa scena: uruchomienie urządzeń
Krok, którego w PDF-ie nie ma. **Bez wkładania baterii** — urządzenia przychodzą z zamontowanymi. Pokazać wyłącznie **kontrolę diody**, a dla Huba **wystawienie na słońce**.

### 9. Zrzuty ekranu aplikacji
Do wymiany dwa: **04.9** (strona 6) i **05.6** (strona 9) — mają niemiecki podpis *„Klicken Sie auf das Symbol…"* wśród angielskich.

> Wszystkie pliki referencyjne: `docs/manual/pictures/` w repo `apisense-docs`.

---

## Format plików

- **SVG** (lub AI z konturami). Raster tylko dla grafik fotorealistycznych.
- **Jeden rysunek = jeden plik.** Bez zbiorczych plansz — układ składamy sami.
- Nazwy plików bez polskich znaków i spacji: `hub-montaz.svg`, `scale-montaz.svg`.
- **Bez prozy w grafice** (patrz tabela na górze). Jeśli podpis musi zostać w rysunku — SVG z `<text id="...">` i stabilnym `id`.
- Tło przezroczyste lub białe, bez ramek i cieni. Kadr ciasno do zawartości.
- Spójny `viewBox` w obrębie serii — żeby rysunki równały się na stronie.
- **Kody QR wektorowo**, nigdy jako raster. Muszą pozostać skanowalne po zmniejszeniu.

**Styl:** w repo są animowane SVG aktualnej generacji — `docs/manual/pictures/montaz-{systemu,hub,wagi,sensora,colonylink}-animated.svg`. Warto potraktować je jako punkt wyjścia; wersja online już z nich korzysta.

---

## Do potwierdzenia — blokuje pracę

| Pytanie | Kto odpowiada | Blokuje |
|---|---|---|
| **ColonyLink to naklejka czy zawieszka?** Dokumentacja opisuje wodoodporną naklejkę na front ula, zdjęcie `sensor_tag.jpg` pokazuje czerwoną zawieszkę na opasce. | produkt | rysunek 5 |
| Czy warianty mocowania VitalSensora `x < 26 mm` / `x > 26 mm` z opaską nadal obowiązują? | produkt | rysunek 4 |
| Czy `Apisense Beeframe Holder` (strona 10) jest jeszcze w zestawie? Nie występuje w dokumentacji. | produkt | rysunek 6 |
| Czy w aplikacji jest osobne pole na ColonyLink przy tworzeniu ula? Jeśli tak — potrzebne nowe zrzuty. | zespół mobile | rysunek 9 |
| Czy telefon `+48 606 153 759` jest aktualny? | marketing | — |
| **Czy PDF jest drukowaną wkładką do pudełka, czy tylko plikiem do pobrania?** Od tego zależy, czy zostaje w InDesign, czy generujemy go ze strony. | marketing | zakres tekstów |

---

## Kolejność

1. **Odpowiedzi na pytania blokujące** — bez pierwszego nie da się narysować ColonyLinka.
2. **Rysunki 1, 2, 4** — dziś wprowadzają w błąd.
3. **Rysunki 3, 6, 7, 8, 9.**
