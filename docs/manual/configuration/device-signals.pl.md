# Sygnalizacja urządzeń

Strona referencyjna: **co widzę na urządzeniu → co to znaczy → co zrobić**.

Jeśli szukasz rozwiązania konkretnego problemu (np. „urządzenie nie zgłasza się"), zacznij od [Rozwiązywania problemów](troubleshooting.md). Ta strona pomaga zinterpretować same sygnały — dioda, przycisk, sekwencja startu — niezależnie od tego, czy coś nie działa.

!!! note "Status strony"
    Strona w trakcie uzupełniania przez zespół embedded. Sekcje oznaczone **TODO** wymagają dopisania na podstawie aktualnego firmware. Jeśli dane urządzenie nie posiada określonego sygnału (np. brak buzzera) — zapisz to jawnie zamiast pomijać sekcję.

---

## Apisense Hub

### Dioda LED

!!! todo "TODO (embedded)"
    Wypełnić wszystkie stany LED na podstawie firmware Huba. Każdy wiersz = jeden rozróżnialny wzorzec (kolor + sekwencja migania). Jeśli LED jest wielokolorowy — wypisać każdą kombinację. Jeśli sygnał wymaga kontekstu (np. „tylko podczas boot") — dopisać w kolumnie *Kontekst*.

| Co widzę | Kontekst | Co to znaczy | Co zrobić |
|---|---|---|---|
| _np. zielona dioda świeci ciągle_ | _po wciśnięciu Power_ | _Hub uruchomiony, łączność OK_ | _nic — stan normalny_ |
| TODO | TODO | TODO | TODO |

### Przycisk Power

!!! todo "TODO (embedded)"
    Wypisać wszystkie rozpoznawane akcje przycisku. Uwzględnić: short press, long press (ile sekund), double press, kombinacje (np. trzymanie przy włożeniu zasilania = factory reset?). Jeśli któraś akcja nie istnieje — napisać wprost.

| Akcja użytkownika | Efekt | Sygnalizacja |
|---|---|---|
| _short press (<1s)_ | _wybudzenie / status check_ | _LED mignie raz na zielono_ |
| TODO | TODO | TODO |

### Sekwencja uruchomienia

!!! todo "TODO (embedded)"
    Opisać co user widzi 0–60s po wciśnięciu Power lub po podłączeniu zasilania. Krok po kroku: kiedy LED się zaświeca, kiedy gaśnie, kiedy Hub jest gotowy. Podać orientacyjne czasy.

### Ładowanie

!!! todo "TODO (embedded)"
    Jak rozpoznać że Hub łapie energię (panel solarny / USB-C / dodatkowy panel PV)? Czy LED to pokazuje, czy tylko aplikacja? Jak rozróżnić „ładuje" vs „naładowany" vs „nie ładuje mimo podłączonego źródła"?

### Niski stan baterii

!!! todo "TODO (embedded)"
    Próg włączenia ostrzeżenia (np. <20%). Jak sygnalizowane lokalnie (LED). Co Hub robi przy bardzo niskim stanie (sleep / shutdown).

### Brak łączności LTE

!!! todo "TODO (embedded)"
    Czy LED rozróżnia: brak SIM / brak rejestracji w sieci / brak zasięgu / serwer nieosiągalny? Czy jest jakakolwiek lokalna sygnalizacja, czy widoczne tylko w aplikacji?

### Brak łączności BLE

!!! todo "TODO (embedded)"
    Sygnalizacja gdy żaden Sensor/Scale nie łączy się z Hubem. Vs sygnalizacja częściowa (część urządzeń OK, część nie).

### Factory reset

!!! todo "TODO (embedded)"
    Procedura wywołania (kombinacja przycisków / czas trzymania). Co user widzi że poszedł reset. Co dokładnie się kasuje (konfiguracja sieci, parowania BLE, certyfikaty?).

### Stan błędu krytycznego

!!! todo "TODO (embedded)"
    Czy firmware ma stan „panic" / „nie da się dalej działać"? Jak sygnalizowane. Jak user ma się zachować (RMA, reset, kontakt support).

---

## Apisense VitalSensor

### Dioda LED

!!! todo "TODO (embedded)"
    Wszystkie stany LED VitalSensora. W [Instrukcji konfiguracji](index.md#3-pierwsze-uruchomienie) jest tylko *„dioda sygnalizacyjna powinna się zaświecić"* — rozwiń: jaki kolor, ile sekund, czy miga, czy świeci ciągle.

| Co widzę | Kontekst | Co to znaczy | Co zrobić |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

### Przycisk

!!! todo "TODO (embedded)"
    Czy VitalSensor ma w ogóle przycisk dostępny dla usera? Jeśli nie — napisać wprost. Jeśli tak — wypisać akcje.

### Sekwencja po włożeniu baterii

!!! todo "TODO (embedded)"
    Co user widzi 0–30s po włożeniu 2× AA. Kiedy LED zaczyna świecić, jak długo, kiedy gaśnie. Kiedy VitalSensor zaczyna szukać Huba.

### Niski stan baterii

!!! todo "TODO (embedded)"
    Próg ostrzeżenia, sygnalizacja LED, kiedy urządzenie przestaje wysyłać dane.

### Pairing / discovery z Hubem

!!! todo "TODO (embedded)"
    Jak user pozna że VitalSensor szuka Huba? Jak długo trwa pierwsze wykrycie? Czy LED się różni gdy znalazł vs gdy szuka?

### Brak zasięgu BLE

!!! todo "TODO (embedded)"
    Sygnalizacja lokalna gdy Hub poza zasięgiem / ekranowany. Czy Sensor próbuje cyklicznie i jak to widać.

### Reset

!!! todo "TODO (embedded)"
    Czy istnieje user-accessible reset (np. wyjęcie baterii na 10s — taki sposób jest opisany w `troubleshooting.md`)? Czy istnieje pełny factory reset?

### Błąd czujnika

!!! todo "TODO (embedded)"
    Czy firmware rozróżnia awarię konkretnego czujnika (NOx, VOC, RH, T, mikrofon)? Czy jest sygnalizacja lokalna, czy tylko w danych telemetrycznych?

---

## Apisense Scale

### Dioda LED

!!! todo "TODO (embedded)"
    Wszystkie stany LED Scale. W [Instrukcji konfiguracji](index.md#3-pierwsze-uruchomienie) jest informacja że dioda zapala się przy starcie — rozwiń jak Hub/VitalSensor.

| Co widzę | Kontekst | Co to znaczy | Co zrobić |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

### Przycisk

!!! todo "TODO (embedded)"
    Scale ma w ogóle przycisk dostępny dla usera? Jeśli nie — napisać wprost.

### Sekwencja po włożeniu baterii

!!! todo "TODO (embedded)"
    Co user widzi po włożeniu 2× AA, przed zamknięciem komory baterii. Jak długo świeci LED. Kiedy Scale zaczyna szukać Huba i wykonywać pierwszy pomiar.

### Kalibracja

!!! todo "TODO (embedded)"
    Czy Scale wykonuje jakąkolwiek auto-kalibrację po starcie (zerowanie tensometru)? Jak user pozna że trwa? Czy jest user-triggered kalibracja? Jeśli nie — napisać wprost.

### Niski stan baterii

!!! todo "TODO (embedded)"
    Próg, sygnalizacja, zachowanie. Scale ma claim 36 miesięcy żywotności — warto też podać orientacyjnie kiedy ostrzeżenie się pojawi przed końcem.

### Brak zasięgu BLE

!!! todo "TODO (embedded)"
    Sygnalizacja lokalna gdy Hub poza zasięgiem.

### Reset

!!! todo "TODO (embedded)"
    Procedura, sygnalizacja, zakres (czy kasuje kalibrację?).

### Stan błędu

!!! todo "TODO (embedded)"
    Czy firmware sygnalizuje błąd tensometru (np. uszkodzony, odłączony, przeciążony)? Lokalna sygnalizacja czy tylko telemetria.

---

## Konwencje strony

Aby strona pozostała czytelna podczas uzupełniania:

- **Jedna kolumna „Co widzę" = jeden rozróżnialny stan.** Nie łączyć kilku wzorców w jednym wierszu.
- **Język nietechniczny.** Nie „kod E001" — zamiast tego „dioda mignęła 3 razy żółto".
- **Brak żargonu firmware.** User nie wie co to „watchdog reset" — pisz „urządzenie samoczynnie się zrestartowało".
- **Jeśli czegoś nie ma — zapisać wprost** (np. „VitalSensor nie posiada zewnętrznego przycisku"). Brak informacji jest informacją.
- **Aktualizacja przy zmianie firmware.** Każda zmiana sygnalizacji w firmware → PR do tej strony w tym samym sprincie.
