# Najczęściej zadawane pytania (FAQ)

Zebrane pytania i odpowiedzi z badania **Apisense 2026 Global Field Validation Study**.

## VitalSensor i montaż

### Czy kolor naklejki NFC/QR przyklejonej do VitalSensora ma znaczenie?

Nie. Kolor nie ma znaczenia — liczy się powiązanie VitalSensor–tag.

### Gdzie dokładnie należy umieścić VitalSensor?

Pionowo, na ramce z czerwiem w gnieździe ula — najlepiej na środku lub obok środka.

### Czy mogę przesuwać VitalSensor w górę/w dół przy dodawaniu kolejnych korpusów?

Tak, w obrębie gniazda. Każdą taką operację odnotuj w aplikacji (najlepiej wraz ze zdjęciem).

### Czy VitalSensor można montować na nietypowych ramkach?

Tak, za pomocą opasek zaciskowych. Po montażu dodaj notatkę (najlepiej ze zdjęciem zamontowanego VitalSensora).

### Czy VitalSensor można używać w odkładach (i innych mniejszych ulach), a później przenosić je do większych?

Zalecamy wstrzymanie się z montażem VitalSensora, dopóki ul nie osiągnie docelowego rozmiaru (chyba że chcesz korzystać z mniejszego rozmiaru, np. mini plus, przez cały sezon — w takiej sytuacji najpierw skontaktuj się z nami).

### Jak wymienić baterie w VitalSensorze?

VitalSensor zasilają dwie baterie **2× AA alkaliczne**.

1. Otwórz pokrywkę.
2. Wymień baterie na **2× AA alkaliczne**.
3. Zamknij pokrywkę.

## Hub i łączność

### Czy Hub można zamontować w pomieszczeniu lub pod dachem?

Nie. Musi znajdować się na zewnątrz, aby zapewnić działanie GPS i prawidłową łączność.

### Czy mogę zasilać Hub na stałe z sieci?

Tak, możesz go zasilać przez USB-C — pod warunkiem że pozostaje na zewnątrz i nie jest niczym przykryty.

### Czy Hub wymaga wymiany baterii?

Nie. Hub ładuje się z panelu słonecznego (PV). Przy słabym nasłonecznieniu możesz doładować go przez USB-C.

### Hub nie ładuje się mimo pełnego słońca — dlaczego?

To zachowanie prawidłowe — zadziałało zabezpieczenie akumulatorów. Hub ładuje się tylko wtedy, gdy temperatura wewnątrz urządzenia nie przekracza **50°C**. Przy montażu od strony południowej i w czasie upałów temperatura wewnątrz może dochodzić do ok. **70°C**, więc ładowanie zostaje wstrzymane ze względów bezpieczeństwa. Paradoksalnie to całodzienne, pełne słońce jest tu przyczyną wstrzymania ładowania — urządzenie działa poprawnie. Gdy temperatura spadnie, ładowanie wznowi się samoczynnie.

### Jak daleko Hub może znajdować się od uli?

Do około 30–40 metrów.

### Hub nie pojawia się w aplikacji — co robić?

Postępuj zgodnie z instrukcją w podręczniku użytkownika; możesz też zapytać asystenta w aplikacji o instrukcje. Ogólne zalecenia:

- Sprawdź orientację (logo czytelne, anteny pionowo do góry).
- Pozostaw urządzenie na zewnątrz przez ~15 minut.
- Spróbuj podłączyć ładowanie USB-C.

Jeśli problem nadal występuje, skontaktuj się z [bee@apisense.ai](mailto:bee@apisense.ai).

### VitalSensor lub Scale nie łączy się z Hubem — co robić?

Urządzenia łączą się z serwerem przez Hub (VitalSensor/Scale → Bluetooth → Hub → LTE → serwer), dlatego kolejność ma znaczenie:

1. **Najpierw musi połączyć się Hub.** Żaden VitalSensor ani Scale nie połączy się, dopóki Hub nie jest online. Hub jest zasilany solarnie — pierwszy kontakt po uruchomieniu zajmuje od ok. 30 minut (naładowany) do nawet 24 godzin (rozładowany, przy złej pogodzie). W aplikacji wybierz scenariusz uruchomienia, aby zobaczyć szacowany czas.
2. **Po połączeniu Huba** każdy VitalSensor i Scale ma własne okno pierwszego połączenia. W tym czasie aplikacja pokazuje status *„oczekiwanie na połączenie”* — to normalne, poczekaj.
3. Jeśli po upływie tego okna urządzenie nadal się nie połączyło, aplikacja pokaże status *„poza zasięgiem”* — oznacza to, że Hub jest online, ale nie widzi urządzenia przez Bluetooth. Najczęstsze przyczyny: urządzenie za daleko od Huba albo problem z samym urządzeniem (np. zasilanie).

Jeśli część urządzeń łączy się, a część nie (np. jeden VitalSensor działa, pozostałe nie) — problem dotyczy konkretnych urządzeń, a nie Huba.

Jeśli problem nie ustępuje, skontaktuj się z [bee@apisense.ai](mailto:bee@apisense.ai).

## Scale

### Czy Scale wymaga baterii lub ładowania?

Tak. Scale zasilają dwie baterie **2× AA alkaliczne**. Po zamontowaniu i dodaniu w aplikacji (kod QR) Scale działa automatycznie — baterie wymieniasz tylko wtedy, gdy się wyczerpią.

### Jak wymienić baterie w Scale?

Potrzebny będzie klucz imbusowy **4 mm** (do kątowników) oraz klucz Torx **T6** (do czarnej obudowy).

1. Rozkręć kątowniki kluczem imbusowym 4 mm — odkręć dwie śruby.
2. Odkręć dwie śrubki Torx T6 w czarnej obudowie.
3. Wymień baterie na **2× AA alkaliczne**.
4. Skręć czarną obudowę z powrotem.
5. Skręć kątowniki z powrotem.

### Który ul powinien stać na Scale?

Dowolny ul wyposażony w VitalSensor — bardziej liczą się trendy niż dokładna masa konkretnego ula.

## Wprowadzanie danych i obsługa aplikacji

### Czy notatki muszą być dodawane od razu na pasieczysku?

Nie. Można je dodać później, wskazując prawidłową datę.

### Czy wiele osób może mieć dostęp do tych samych danych w aplikacji?

Jeszcze nie potwierdzone — Apisense skontaktuje się w tej sprawie mailowo.

## Badania i próbki

### Czy w badaniach Global Field Validation Study trzeba wykonywać flotację na Varroa (sugar roll)?

Tak — zawsze. Flotacja na Varroa (sugar roll) jest **obowiązkowa w każdym zaplanowanym badaniu** (Test 1, 2 i 3), dla wszystkich monitorowanych rodzin. Wykonujesz ją za każdym razem, niezależnie od pory sezonu, wskazań czujników czy braku widocznych objawów warrozy. W każdym badaniu wykonujesz komplet **obu procedur**: flotację na Varroa **oraz** mikroskopię Nosema/Vairimorpha. Szczegóły: [Procedury badań](../procedures/index.md).

## Praktyki pszczelarskie

### Czy mogę stosować zabiegi z użyciem kwasu szczawiowego lub mrówkowego?

Tak. Pamiętaj, aby zaznaczyć to w notatce w aplikacji.

### Czy VitalSensor można przenieść, jeśli rodzina padnie lub zostanie utracona?

Nie przenoś VitalSensor bez wcześniejszego poinformowania zespołu Apisense! Ze względu na ryzyko rozprzestrzeniania chorób oraz integralność danych, w takiej sytuacji za każdym razem skontaktuj się z nami bezpośrednio i poczekaj na dalsze instrukcje.

### Przekładam VitalSensor do innej rodziny (np. po osypaniu się rodziny) — jak odwzorować to w aplikacji?

Nowa rodzina = nowy ul w aplikacji. Wykonaj to w trzech krokach:

1. **Utwórz nowy ul** w aplikacji — stary ul zostaje bez zmian.
2. **Odepnij urządzenia od starego ula** i **przypnij je do nowego** (po odkażeniu VitalSensora).
3. Od tej pory nowe pomiary trafiają do nowego ula.

Historii pomiarów **nie przenosimy** między ulami — to była inna rodzina, więc dane ze starego ula nie opisują nowej. Dlatego dane zaczynają się od nowa wraz z utworzeniem nowego ula. Nie musisz nas o tym informować — gdy utworzysz nowy ul i przepniesz tam urządzenia, mamy pełen obraz sytuacji.

### A co z odkładami lub dodawaniem/zdejmowaniem nadstawek?

Zawsze dodawaj notatkę o takich czynnościach — pomaga to w prawidłowej interpretacji danych.

### Co jeśli przewożę swoje ule?

Przewieź wszystkie ule + Hub + Scale razem i dodaj notatkę w aplikacji.
