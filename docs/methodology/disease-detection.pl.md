# Jak działa wykrywanie chorób

Coraz częściej pytacie nas, **jak właściwie działa wykrywanie chorób w Apisense** i skąd aplikacja „wie”, że z rodziną dzieje się coś niepokojącego. Na tej stronie tłumaczymy to prostym językiem — bez wzorów i tabel statystycznych.

Jeśli interesuje Cię, **jak krok po kroku powstają nasze modele** (od pomysłu, przez laboratorium, po wdrożenie w pasiekach), zajrzyj na stronę [Jak powstają nasze modele](research-process.md).

______________________________________________________________________

## W skrócie

Czujnik **VitalSensor** umieszczony między ramkami **w sposób ciągły „wącha” powietrze w ulu**. Każda rodzina ma swój naturalny „zapach” — chemiczny odcisk złożony z wielu związków. Gdy w rodzinie rozwija się choroba, ten odcisk **zmienia się w charakterystyczny sposób**, zwykle na długo, zanim zobaczysz objawy gołym okiem.

Nasza **sztuczna inteligencja (AI)** nauczyła się rozpoznawać te wzorce i na ich podstawie przypisuje rodzinie **status zdrowia oraz poziom zakażenia** — a wynik widzisz w aplikacji Apisense Pro AI.

!!! info "To uzupełnienie, nie zamiennik"
    Wykrywanie chorób z powietrza ula **wspiera** Twoje obserwacje i przeglądy — nie zastępuje ich. Traktuj alerty jako wczesny sygnał „przyjrzyj się tej rodzinie”, a nie jako ostateczną diagnozę.

______________________________________________________________________

## Co „czuje” czujnik

VitalSensor mierzy kilkanaście parametrów wnętrza ula. Najważniejsze z nich to:

- **Skład chemiczny powietrza** — związki lotne (VOC), czyli ten chemiczny „zapach” rodziny,
- **Temperatura i wilgotność** — mikroklimat gniazda,
- **Inne parametry środowiskowe** — m.in. poziom dwutlenku węgla i aktywność akustyczna (dźwięki rodziny).

Można to porównać do lekarza, który rozpoznaje chorobę po zapachu czy oddechu pacjenta — tyle że tutaj „nosem” jest czujnik, a „pamięcią doświadczeń” sztuczna inteligencja.

______________________________________________________________________

## Skąd AI wie, co jest chore

Sama liczba z czujnika nic by nam nie powiedziała, gdyby nie **odniesienie do rzeczywistości**. Dlatego nasze modele uczą się na **tysiącach oznaczonych próbek**, w których odczyty czujnika są zestawione z **faktycznym wynikiem badania** danej rodziny — np. liczbą spor *Nosema* pod mikroskopem czy poziomem porażenia *Varroa*.

Dane te zbieramy zarówno w **laboratorium** (rodziny w klateczkach z czujnikami), jak i w **prawdziwych pasiekach**. Każda choroba zostawia w danych swój własny, rozpoznawalny „podpis”, a model uczy się go odróżniać od stanu zdrowego.

Cały ten proces — od pomysłu po globalne wdrożenie — opisujemy na stronie [Jak powstają nasze modele](research-process.md).

______________________________________________________________________

## Poziomy zakażenia — co oznaczają

Dla niektórych chorób aplikacja pokazuje nie tylko „jest / nie ma”, ale też **poziom**: niski, umiarkowany lub wysoki. Poniższe wartości to **orientacyjne progi**, których używamy do oznaczania danych — są zgodne ze standardowymi badaniami, które pszczelarze wykonują na co dzień, więc łatwo je odnieść do własnej pasieki.

### Warroza (*Varroa destructor*)

| Poziom | Flotacja (przemywanie alkoholem) | Osyp dzienny | Co to oznacza |
|---|---|---|---|
| **Niski** | do ok. 2% porażenia | 2–3 roztocze na dobę | Stan dopuszczalny i powszechny — warroza jest obecna, ale jeszcze nie zagraża rodzinie. |
| **Umiarkowany** | ok. 3–4% porażenia | 4–10 roztoczy na dobę | Choroba — warto zaplanować działania. |
| **Wysoki** | powyżej ok. 5% porażenia | powyżej 11 roztoczy na dobę | Zaawansowana warroza — rodzina wymaga interwencji. |

!!! note "Flotacja: przemywanie alkoholem vs. metoda cukrowa"
    Progi flotacji powyżej odnoszą się do **przemywania alkoholem** — metody referencyjnej (najdokładniejszej, ale niszczącej próbkę). W codziennym monitoringu opisujemy także łagodniejszą, nieinwazyjną [flotację cukrową](../procedures/varroa-sugar-roll.md), po której pszczoły wracają do ula. Obie metody podają poziom porażenia w procentach, ale metoda cukrowa zwykle wykrywa nieco mniej roztoczy.

### Nosemoza (*Nosema* / *Vairimorpha* spp.)

| Poziom | Liczba spor (na 10 pszczół) | Co to oznacza |
|---|---|---|
| **Niski** | 1–3 spory | Stan dopuszczalny i powszechny — nosemoza obecna, ale jeszcze nie zagraża. |
| **Umiarkowany** | 4–40 spor | Choroba. |
| **Wysoki** | powyżej 40 spor | Zaawansowana choroba. |

!!! note "Skąd ta liczba spor"
    Liczbę spor wyznacza się pod mikroskopem — opisujemy to w procedurze [Mikroskopia Nosema/Vairimorpha](../procedures/nosema-microscopy.md). Wartości w tabeli to uśredniona liczba spor przypadająca na 10 pszczół.

### Zgnilec amerykański i grzybica wapienna

Dla tych chorób model wykrywa **obecność**, a nie poziom:

- **Zgnilec amerykański (AFB)** — sygnał „pojawiło się ryzyko zgnilca”. To choroba **zwalczana z urzędu**, dlatego dane zbieramy w szczególny sposób — opisujemy to na stronie [Jak powstają nasze modele](research-process.md#zgnilec-wyjatek).
- **Grzybica wapienna (*chalkbrood*)** — rozróżniamy stan zdrowy, samą ekspozycję (kontakt bez widocznych objawów) oraz wyraźne objawy choroby.

______________________________________________________________________

## Kolejne choroby w przygotowaniu

System stale rozwijamy. Pracujemy nad wykrywaniem kolejnych zagrożeń, m.in. **choroby pełzakowej**, **barciaka większego** oraz **wirusów** przenoszonych przez *Varroa* (np. wirus zdeformowanych skrzydeł, DWV). Gdy modele przejdą nasz proces walidacji, dodamy je do aplikacji.

______________________________________________________________________

## Zobacz też

- [Jak powstają nasze modele](research-process.md) — droga od pomysłu do wdrożenia w pasiekach.
- [Procedury badań](../procedures/index.md) — jak samodzielnie wykonać flotację i mikroskopię i zaraportować wyniki.
- [Opis systemu](../overview/index.md) — czym są VitalSensor, Hub, Scale i aplikacja Apisense Pro AI.
