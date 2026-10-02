# Sygnalizacja urządzeń

Strona referencyjna: **co widzę na urządzeniu → co to znaczy → co zrobić**.

Jeśli szukasz rozwiązania konkretnego problemu (np. „urządzenie nie zgłasza się"), zacznij od [Rozwiązywania problemów](troubleshooting.md). Ta strona pomaga zinterpretować same sygnały — dioda, przycisk, sekwencja startu — niezależnie od tego, czy coś nie działa.

!!! info "Diody tylko potwierdzają działanie"
    Żadne z urządzeń nie pokazuje diodą poziomu baterii ani błędów.

---

## Apisense Hub

### Dioda LED

W przycisku Huba są dwie diody: **niebieska** i **czerwona**. Diody tylko potwierdzają działania z tabeli. Przez resztę czasu nie świecą — także wtedy, gdy Hub pracuje normalnie i jest uśpiony między pomiarami.

| Co widzę | Kiedy | Co to znaczy | Co zrobić |
|---|---|---|---|
| Niebieska miga 3 razy, potem czerwona 1 raz | Po uruchomieniu lub restarcie Huba | Hub się uruchamia | Nic — stan normalny |
| Niebieska miga 1 raz | Po krótkim naciśnięciu przycisku (krócej niż 3 s) | Hub się wybudził | Nic — stan normalny |
| Niebieska miga 2 razy | Po podłączeniu ładowarki USB | Hub się wybudził i zaczyna ładowanie | Nic — stan normalny |
| Niebieska miga 3 razy | Samoczynnie, gdy na panel pada dość światła | Wbudowany panel solarny zaczyna ładowanie | Nic — nie trzeba niczego podłączać |
| Niebieska miga 4 razy | Po podłączeniu zewnętrznej ładowarki 12 V | Hub się wybudził i zaczyna ładowanie | Nic — stan normalny |
| Niebieska miga 3 razy, powoli | W trakcie trzymania przycisku dłużej niż 10 s | Brak działania | Nic |
| Diody nie świecą | Przez resztę czasu | Hub pracuje normalnie lub jest uśpiony | Nic — stan normalny |

### Przycisk Power

Hub reaguje w chwili **puszczenia** przycisku. Bardzo krótkie muśnięcie przycisku jest ignorowane.

| Akcja użytkownika | Efekt | Sygnalizacja |
|---|---|---|
| Naciśnięcie krótsze niż 3 s | Hub się wybudza | Niebieska miga 1 raz |
| Przytrzymanie od 3 do 10 s | Hub się restartuje | Sekwencja uruchomienia: niebieska 3 razy, potem czerwona 1 raz. Diody zaświecą się dopiero, gdy Hub wstanie po restarcie |
| Przytrzymanie dłużej niż 10 s | Brak działania | Niebieska miga 3 razy, powoli — jeszcze w trakcie trzymania |

### Sekwencja uruchomienia

Po każdym uruchomieniu i po każdym restarcie Hub pokazuje tę samą sekwencję: niebieska dioda miga 3 razy, potem czerwona 1 raz. Później diody gasną.

### Ładowanie

Hub potwierdza diodą tylko **początek** ładowania. Liczba mignięć niebieskiej diody mówi, skąd pochodzi energia:

- 2 mignięcia — ładowarka USB,
- 3 mignięcia — wbudowany panel solarny,
- 4 mignięcia — zewnętrzna ładowarka 12 V.

Dioda nie pokazuje, że ładowanie trwa ani że bateria jest pełna.

### Niski stan baterii

Hub nie sygnalizuje diodą niskiego stanu baterii.

### Brak łączności LTE

Hub nie sygnalizuje diodą braku łączności LTE.

### Brak łączności BLE

Hub nie sygnalizuje diodą braku połączenia z VitalSensorem lub Scale.

### Factory reset

Hub nie ma funkcji przywracania ustawień fabrycznych. Dostępny jest tylko restart: przytrzymaj przycisk od 3 do 10 s.

### Stan błędu krytycznego

Hub nie sygnalizuje diodą błędów.

---

## Apisense VitalSensor

### Dioda LED

VitalSensor ma jedną diodę. Widać ją przez obudowę.

| Co widzę | Kiedy | Co to znaczy | Co zrobić |
|---|---|---|---|
| Szybkie miganie (około 5 razy na sekundę) | Po włożeniu baterii, zwykle przez około 15 s | VitalSensor się uruchomił | Nic — stan normalny |
| Wolne miganie (około 1 raz na sekundę), do 2 minut | Po 12 godzinach bez połączenia z Hubem | VitalSensor ponownie szuka połączenia | Nic — urządzenie robi to samo z siebie |
| Dioda nie świeci | Przez resztę czasu | VitalSensor pracuje normalnie i wykonuje pomiary | Nic — stan normalny |

### Przycisk

VitalSensor nie ma przycisku.

### Sekwencja po włożeniu baterii

Po włożeniu 2× AA dioda zaczyna szybko migać. Miga zwykle około 15 s, potem gaśnie. Zgaszona dioda oznacza normalną pracę: VitalSensor działa i czeka na kolejny cykl pomiarowy.

### Niski stan baterii

VitalSensor nie sygnalizuje diodą niskiego stanu baterii.

### Pairing / discovery z Hubem

Dioda nie pokazuje, czy VitalSensor połączył się z Hubem.

### Brak zasięgu BLE

Na bieżąco dioda nie pokazuje braku zasięgu. Po 12 godzinach bez połączenia VitalSensor sam ponawia szukanie — dioda miga wtedy wolno, do 2 minut.

### Reset

VitalSensor nie ma przycisku resetu.

### Błąd czujnika

VitalSensor nie sygnalizuje diodą błędów. Informacje o błędach trafiają do systemu razem z pomiarami.

---

## Apisense Scale

### Dioda LED

Scale ma jedną diodę. Dioda jest **wewnątrz czarnej obudowy** — żeby ją zobaczyć, trzeba otworzyć obudowę.

| Co widzę | Kiedy | Co to znaczy | Co zrobić |
|---|---|---|---|
| Szybkie miganie (około 5 razy na sekundę) | Po włożeniu baterii, zwykle przez około 15 s | Scale się uruchomił | Nic — stan normalny |
| Wolne miganie (około 1 raz na sekundę), do 2 minut | Po 12 godzinach bez połączenia z Hubem | Scale ponownie szuka połączenia | Nic — urządzenie robi to samo z siebie |
| Dioda nie świeci | Przez resztę czasu | Scale pracuje normalnie i wykonuje pomiary | Nic — stan normalny |

### Przycisk

Scale nie ma przycisku.

### Sekwencja po włożeniu baterii

Po włożeniu 2× AA, jeszcze przed zamknięciem obudowy, dioda zaczyna szybko migać. Miga zwykle około 15 s, potem gaśnie. Zgaszona dioda oznacza normalną pracę: Scale działa i czeka na kolejny cykl pomiarowy.

### Kalibracja

Scale nie ma przycisku, więc tarowania na urządzeniu nie ma.

### Niski stan baterii

Scale nie sygnalizuje diodą niskiego stanu baterii.

### Brak zasięgu BLE

Na bieżąco dioda nie pokazuje braku zasięgu. Po 12 godzinach bez połączenia Scale sam ponawia szukanie — dioda miga wtedy wolno, do 2 minut. Zobaczysz to tylko przy otwartej obudowie.

### Reset

Scale nie ma przycisku resetu.

### Stan błędu

Scale nie sygnalizuje diodą błędów. Informacje o błędach trafiają do systemu razem z pomiarami.
