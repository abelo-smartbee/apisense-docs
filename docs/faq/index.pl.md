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

!!! note "Uwaga"
    Po zakończeniu wymiany baterii nie są wymagane żadne dodatkowe czynności w aplikacji ani na urządzeniu Hub czy VitalSensor. Nie należy ponownie parować urządzeń, dodawać ich do ula ani naciskać przycisku RESET. Wystarczy umieścić urządzenie VitalSensor z powrotem w zasięgu łączności Huba i poczekać na kolejną synchronizację danych. Zaktualizowane dane pojawią się w aplikacji automatycznie - może to potrwać do kilku godzin, pod warunkiem że Hub poprawnie komunikuje się z systemem (nie jest w trybie offline - rozładowana bateria/brak łączności).

## Hub i łączność

### Czy Hub można zamontować w pomieszczeniu lub pod dachem?

Nie. Musi znajdować się na zewnątrz, aby zapewnić działanie GPS i prawidłową łączność.

### Czy mogę zasilać Hub na stałe z sieci?

Tak, możesz go zasilać przez USB-C — pod warunkiem że pozostaje na zewnątrz i nie jest niczym przykryty.

### Czy Hub wymaga wymiany baterii?

Nie. Hub ładuje się z panelu słonecznego (PV). Przy słabym nasłonecznieniu możesz doładować go przez USB-C.

### Czy po rozładowaniu Huba i ponownym podłączeniu go do ładowania lub wystawieniu na słońce muszę nacisnąć przycisk RESET?

Nie. Po wystarczającym naładowaniu Hub automatycznie wznowi pracę, połączy się z systemem i urządzeniami.

### Czy po wymianie baterii w Scale lub VitalSensor muszę nacisnąć przycisk RESET na Hubie?

Nie. Nie należy wykonywać resetu Huba po wymianie baterii w urządzeniach Scale lub VitalSensor. Po wymianie baterii wystarczy umieścić urządzenie z powrotem w zasięgu łączności Huba i poczekać na kolejną synchronizację danych. Pamiętaj, że przy tym Hub musi poprawnie komunikować się z systemem (nie może być w trybie offline — rozładowany lub brak łączności).

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

    ![Rozkręcanie kątowników kluczem imbusowym 4 mm](pictures/scale-battery-1-brackets.jpg){width=450}

2. Odkręć dwie śrubki Torx T6 w czarnej obudowie.

    ![Śrubka Torx T6 w czarnej obudowie](pictures/scale-battery-2-housing.jpg){width=450}

3. Wymień baterie na **2× AA alkaliczne**.

    ![Wymiana baterii na 2× AA alkaliczne](pictures/scale-battery-3-replace.jpg){width=450}

4. Skręć czarną obudowę z powrotem.
5. Skręć kątowniki z powrotem.

!!! note "Uwaga"
    Po zakończeniu wymiany baterii nie są wymagane żadne dodatkowe czynności w aplikacji ani na urządzeniu Hub czy Scale. Nie należy ponownie parować urządzeń, dodawać ich do ula ani naciskać przycisku RESET. Wystarczy umieścić urządzenie Scale z powrotem w zasięgu łączności Huba i poczekać na kolejną synchronizację danych. Zaktualizowane dane pojawią się w aplikacji automatycznie - może to potrwać do kilku godzin, pod warunkiem że Hub poprawnie komunikuje się z systemem (nie jest w trybie offline - rozładowana bateria/brak łączności).

### Który ul powinien stać na Scale?

Dowolny ul wyposażony w VitalSensor — bardziej liczą się trendy niż dokładna masa konkretnego ula.

## Po wymianie baterii

<a id="po-wymianie-baterii"></a>

### Co należy zrobić po wymianie baterii w Scale/VitalSensor?

Po wymianie baterii wystarczy:

- ponownie umieścić urządzenie Scale lub VitalSensor w jego docelowym miejscu,
- upewnić się, że znajduje się ono w zasięgu Huba (maksymalnie około 35 m),
- poczekać na kolejny cykl pomiarowy.

Zaktualizowane dane pojawią się w aplikacji automatycznie - może to potrwać do kilku godzin, pod warunkiem że Hub poprawnie komunikuje się z systemem (nie jest w trybie offline - rozładowana bateria/brak łączności).

### Czy po wymianie baterii muszę ponownie sparować urządzenie Scale lub VitalSensor?

Nie. Wymiana baterii nie wymaga ponownego parowania urządzenia. Wystarczy umieścić urządzenie z powrotem w zasięgu łączności Huba i poczekać na kolejną synchronizację danych. Pamiętaj, że przy tym Hub musi poprawnie komunikować się z systemem (nie może być w trybie offline — rozładowany lub brak łączności).

### Czy po wymianie baterii muszę usunąć i ponownie dodać Scale lub VitalSensor do ula?

Nie. Nie musisz niczego zmieniać w aplikacji po wymianie baterii w urządzeniu Scale lub VitalSensor. Wystarczy umieścić urządzenie z powrotem w zasięgu łączności Huba i poczekać na kolejną synchronizację danych. Pamiętaj, że przy tym Hub musi poprawnie komunikować się z systemem (nie może być w trybie offline — rozładowany lub brak łączności).

### Czy po wymianie baterii muszę usunąć i ponownie dodać ul w aplikacji?

Nie. Nie ma potrzeby usuwania ani ponownego dodawania ula lub przypisanych do niego urządzeń. Po wymianie baterii w urządzeniu Scale lub VitalSensor wystarczy umieścić urządzenie z powrotem w zasięgu łączności Huba i poczekać na kolejną synchronizację danych. Pamiętaj, że przy tym Hub musi poprawnie komunikować się z systemem (nie może być w trybie offline — rozładowany lub brak łączności).

## Wprowadzanie danych i obsługa aplikacji

<a id="przybytek-miodu-waga"></a>

### Czy jest możliwe, aby waga ula wskazywała wartość dodatnią, podczas gdy przybytek miodu był ujemny, mimo że jest on wyliczany na podstawie pomiarów wagi?

Tak, jest to jak najbardziej możliwe. Przykładowo, pszczelarz może dołożyć półkorpus, co spowoduje wzrost całkowitej masy ula. Jednocześnie, jeśli rodzina pszczela jest osłabiona, produkcja miodu może się zmniejszyć. W takiej sytuacji na wykresie wagi ula widoczny będzie wyraźny wzrost wynikający z dołożenia półkorpusu. Natomiast na wykresie przybytku masa dodanego półkorpusu nie zostanie uwzględniona, dzięki czemu wykres będzie odzwierciedlał wyłącznie rzeczywistą zmianę ilości miodu. W efekcie na wykresie przybytku widoczny będzie spadek związany z ograniczoną aktywnością pszczół, a nie sztuczny wzrost wynikający z ingerencji pszczelarza.

### Czy notatki muszą być dodawane od razu na pasieczysku?

Nie. Można je dodać później, wskazując prawidłową datę.

### Czy wiele osób może mieć dostęp do tych samych danych w aplikacji?

Jeszcze nie potwierdzone — Apisense skontaktuje się w tej sprawie mailowo.

## Badania i próbki

### Czy w badaniach Global Field Validation Study trzeba wykonywać flotację na Varroa (sugar roll)?

Tak — zawsze. Flotacja na Varroa (sugar roll) jest **obowiązkowa w każdym zaplanowanym badaniu** (Test 1, 2 i 3), dla wszystkich monitorowanych rodzin. Wykonujesz ją za każdym razem, niezależnie od pory sezonu, wskazań czujników czy braku widocznych objawów warrozy. W każdym badaniu wykonujesz komplet **obu procedur**: flotację na Varroa **oraz** mikroskopię Nosema/Vairimorpha. Szczegóły: [Procedury badań](../procedures/index.md).

### Czy można zamrażać próbki pszczół do badania na Nosemę?

Tak — **zamrażanie pszczół jest dopuszczalne wyłącznie** w przypadku badań na *Nosemę*.

- Każda zamrożona próbka musi być **czytelnie i jednoznacznie opisana**, tak aby można było ustalić, z którego ula pochodzi.
- Temperatura przechowywania: **co najmniej −8 °C**.
- Próbki można przechowywać w zamrażarce przez około **3–5 miesięcy** przed wykonaniem badania lub wysłaniem do laboratorium.
- Próbek **nie wolno rozmrażać i zamrażać ponownie**.

Szczegóły: [Mikroskopia Nosema/Vairimorpha](../procedures/nosema-microscopy.md#przechowywanie-przed-badaniem), [Rejestrowanie próbki](../manual/app-manual.md#rejestrowanie-probki).

### Czy mogę wysłać Pocztą Polską żywe pszczoły do Lublina?

Tak. Próbki żywych pszczół należy nadawać **Pocztą Polską** na adres laboratorium w Lublinie (Uniwersytet Przyrodniczy w Lublinie, ul. Doświadczalna 54, 20-280 Lublin) — od **poniedziałku do czwartku**  (szacowany koszt **20–30 zł**). Pszczoły należy wysłać **żywe**, w klateczkach transportowych zapewniających dostęp powietrza, z kawałkiem ciasta cukrowego i kodem badania z aplikacji Apisense na każdej klateczce. Przesyłki z żywymi pszczołami za pośrednictwem Poczty Polskiej mogą być nadawane wyłącznie przez właścicieli pasiek zlokalizowanych w Polsce. Szczegóły: [Protokół 2 — żywe pszczoły](../samples/protocol-2-live-bees.md).

## Praktyki pszczelarskie

### Czy mogę stosować zabiegi z użyciem kwasu szczawiowego lub mrówkowego?

Tak. Pamiętaj, aby zaznaczyć to w notatce w aplikacji.

<a id="przenoszenie-vitalsensora"></a>

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

<a id="przepinanie-urzadzen"></a>

## Przepinanie urządzeń między ulami i pasiekami

Ta sekcja opisuje, co zrobić w aplikacji, gdy VitalSensor (albo Scale) zmienia ul — bo ramka z czujnikiem trafiła do innego ula, rodzina przeniosła się na inne pasieczysko albo Huby zamieniły się miejscami.

!!! warning "Najpierw skontaktuj się z nami"
    Jeśli bierzesz udział w badaniu Global Field Validation Study, nie przenoś VitalSensora między rodzinami bez uzgodnienia z zespołem Apisense — patrz [Czy VitalSensor można przenieść…](#przenoszenie-vitalsensora). Poniższe kroki opisują wyłącznie stronę aplikacyjną i nie zwalniają z tego obowiązku.

<a id="zasada-urzadzenie-nalezy-do-ula"></a>

### Zasada ogólna: urządzenie należy do ula, a Hub do pasieki

- VitalSensor i Scale są **przypisane do ula**, a nie do Huba. Hub jest wyłącznie pośrednikiem — przekazuje dane z urządzeń stojących w jego pasiece do systemu.
- Urządzenie zawsze raportuje przez **Hub tej pasieki, w której stoi jego ul**. Gdy przypniesz czujnik do ula w innej pasiece, system sam przestawi go na Hub tamtej pasieki i odświeży konfigurację obu Hubów. **Nie skanujesz w tym celu kodu QR Huba.**
- Dlatego czujnik **nie musi zostać przy pierwotnym Hubie** i nie musisz przewozić rodziny z powrotem tylko po to, żeby „wrócić do starego Huba".
- Historia pomiarów jest zapisywana pod **numerem seryjnym urządzenia** i pokazywana w ulu **od momentu powiązania** urządzenia z tym ulem.
- ColonyLink zostaje przy ulu (jest naklejony na ul) — przepinając czujnik, nie ruszasz ColonyLinka.

<a id="skanowanie-qr-z-poziomu-ula"></a>

### Jak zeskanować kod QR czujnika z poziomu konkretnego ula?

Kod QR urządzenia skanujesz zawsze „z wnętrza" tego ula, do którego urządzenie ma trafić:

1. Zakładka **Pasieki** → kafelek pasieki → zakładka *Ule* → kafelek wybranego ula.
2. W zakładce *Szczegóły* kliknij ikonę **⋮** (prawy górny róg) i wybierz *Ustawienia*.
3. Rozwiń sekcję **Wyposażenie** i znajdź blok **VitalSensor** (albo **Scale**).
4. Kliknij **ikonę kodu QR** po prawej stronie pola i zeskanuj kod z urządzenia — *Numer seryjny* i *Kod potwierdzający* uzupełnią się same.
5. Zapisz zmiany żółtym przyciskiem w prawym dolnym rogu.

Na co zwrócić uwagę:

- Ikona kodu QR jest dostępna tylko wtedy, gdy pola danego urządzenia są **puste**, czyli w tym ulu nie ma jeszcze VitalSensora (lub Scale).
- Sekcja *Wyposażenie* w ogóle się nie pojawi, jeśli do pasieki nie jest przypisany Hub.
- W pasiece udostępnionej Ci przez inną osobę sekcja *Wyposażenie* może być tylko do odczytu — zarządzanie urządzeniami należy do właściciela pasieki.

Szczegółowy opis widoku: [Omówienie ustawień ula](../manual/app-manual.md#omowienie-ustawien-ula).

<a id="przepiecie-w-tej-samej-pasiece"></a>

### Przełożyłem czujnik do innego ula w tej samej pasiece (ten sam Hub) — co zrobić?

1. **Odłącz czujnik od starego ula.** *Ustawienia ula* → *Wyposażenie* → *Odłącz VitalSensor* → **zostaw włączony** przełącznik *Zachowaj historię danych VitalSensor dla tego ula* → *Odłącz*.
2. **Przypnij czujnik do nowego ula** — kroki jak w [skanowaniu kodu QR z poziomu ula](#skanowanie-qr-z-poziomu-ula). Jeśli ul docelowy jeszcze nie istnieje w aplikacji, najpierw go utwórz.
3. **Dodaj notatkę z datą** w obu ulach — dzięki temu przerwa na wykresie będzie później czytelna.

Huba nie dotykasz — jego konfiguracja odświeża się automatycznie po obu operacjach.

**Kolejność ma znaczenie.** Dopóki nie odłączysz czujnika od starego ula, próba zeskanowania jego kodu w nowym ulu zakończy się komunikatem: *„VitalSensor jest już przypisany do ula X. Odłącz urządzenie z ula X lub zeskanuj kod QR z innego VitalSensor."*

<a id="przepiecie-do-innej-pasieki"></a>

### Przełożyłem czujnik do ula w innej pasiece (inny Hub) — czy mogę zarejestrować go przy tamtym Hubie?

**Tak.** Czujnik nie jest „przywiązany" do Huba, przy którym był rejestrowany po raz pierwszy. Kroki są dokładnie takie same jak przy przepięciu w obrębie jednej pasieki: najpierw *Odłącz VitalSensor* w starym ulu, potem zeskanuj jego kod QR w ulu docelowym. System sam przypisze czujnik do Huba pasieki docelowej.

Warunki, które muszą być spełnione:

- pasieka docelowa musi mieć **własny Hub** — w przeciwnym razie zobaczysz komunikat *„Scale i VitalSensor wymagają podłączonego Huba do pasieki"*;
- czujnik musi znaleźć się **w zasięgu tego Huba** (do ok. 30–40 m).

!!! note "Wyjątek: cała rodzina przeprowadziła się razem ze swoim ulem"
    Jeśli nie chodzi o przełożenie ramki, tylko o przewiezienie **tego samego ula z tą samą rodziną** na inne pasieczysko, i chcesz zachować pełną historię tego ula (pomiary, notatki, przeglądy, badania, próbki, dane o matce), **nie twórz nowego ula i nie przepinaj urządzeń**. Aplikacja nie pozwala jeszcze samodzielnie przenieść ula między pasiekami — napisz na [bee@apisense.ai](mailto:bee@apisense.ai), a przeniesiemy ul po naszej stronie razem z całą historią i przypisanymi urządzeniami (wykresy pozostaną ciągłe). Jeśli w tej sytuacji założysz nowy ul, historia jednej rodziny zostanie rozdzielona na dwa rekordy.

<a id="przepiecie-czujnika-bez-ula"></a>

### Czujnik nie był wcześniej przypisany do żadnego ula — co zrobić?

Po prostu zeskanuj jego kod QR w ulu docelowym ([kroki wyżej](#skanowanie-qr-z-poziomu-ula)) — nie ma czego odłączać. Możliwe komunikaty:

| Komunikat | Znaczenie |
| :---- | :--------- |
| *„VitalSensor o podanym numerze seryjnym nie istnieje w systemie"* | Zeskanowany kod nie odpowiada żadnemu urządzeniu — sprawdź, czy skanujesz kod z właściwej naklejki. |
| *„To urządzenie nie może zostać powiązane z tym kontem"* | Czujnik jest zarejestrowany na inne konto. |
| *„Niepoprawny kod potwierdzający VitalSensor"* | Brakuje kodu potwierdzającego — zeskanuj kod QR, który uzupełnia oba pola naraz, zamiast wpisywać sam numer seryjny. |

<a id="dane-w-starym-ulu"></a>

### Co stanie się z danymi w starym ulu?

Odłączenie urządzenia dotyczy wyłącznie urządzenia. W starym ulu **zostają bez zmian**: notatki, przeglądy, zadania, badania, próbki, dane o matce oraz odpowiedzi na formularze chorobowe.

Z danymi pomiarowymi jest tak:

- przełącznik *Zachowaj historię…* **włączony** (ustawienie domyślne) — pomiary zostają w systemie, ale ul przestaje je pokazywać: w widoku *Stan ula* wiersze *Waga* i *Warunki* pokazują *Brak Scale* / *Brak VitalSensor*, a wykresów nie da się rozwinąć;
- przełącznik **wyłączony** — pomiary tego urządzenia dla tego ula są **trwale usuwane**, a w przypadku VitalSensora usuwane są także próbki zarejestrowane w tym ulu tym czujnikiem. Tej operacji **nie da się cofnąć**.

Jeśli później przypniesz do starego ula inne urządzenie, jego wykresy zaczną się **od momentu tego nowego powiązania**. Wcześniejsze pomiary pozostają w systemie, ale nie wracają na wykres.

!!! warning "Nie usuwaj starego ula tylko dla porządku"
    Usunięcie ula kasuje całą jego zawartość (notatki, przeglądy, badania) oraz historię pomiarów odpiętych od niego urządzeń. Ul bez urządzeń nic nie kosztuje i nie przeszkadza — zostaw go jako zapis historii tej rodziny.

<a id="dane-w-nowym-ulu"></a>

### Co stanie się z danymi w nowym ulu?

- **Wykresy zaczynają się od momentu powiązania.** Pomiary z poprzedniego ula nie są przenoszone — opisywały inną rodzinę i inne warunki.
- **Urządzenie przechodzi pierwsze uruchomienie od nowa.** Na kafelku ula zobaczysz kolejno *Czekamy na połączenie*, a po nawiązaniu łączności *Urządzenie połączone — czekamy na pierwszy pomiar*. Pierwszy kontakt może zająć do kilku godzin i wymaga, aby Hub był online. Szczegóły: [Pierwsze uruchomienie urządzeń](../manual/app-manual.md#pierwsze-uruchomienie).
- **Ocena zdrowia rodziny startuje od zera.** Przez pierwsze ok. 3 dni od przypisania na kafelku ula widnieje *Zbieramy dane*, a na kafelku pasieki *Zbieramy dane o zdrowiu X z Y uli*. Szczegóły: [Stan zdrowia rodziny](../manual/app-manual.md#stan-zdrowia).
- **Scale: powiązanie z ulem zeruje tarowanie.** Po zamontowaniu wagi pod nowym ulem wykonaj tarowanie ponownie — patrz [Waga](../manual/app-manual.md#4-waga).

<a id="przepinanie-ryzyka"></a>

### O czym pamiętać — ryzyka

- **Ryzyko przeniesienia choroby.** Czujnik wędruje między rodzinami razem z ramką. Odkażaj VitalSensor przed montażem w kolejnej rodzinie, a w badaniu Global Field Validation Study najpierw uzgodnij przeniesienie z zespołem Apisense.
- **Zachowaj kolejność:** najpierw *Odłącz* w starym ulu, dopiero potem skanowanie w nowym. Odwrotna kolejność kończy się komunikatem o konflikcie.
- **Nie wyłączaj przełącznika *Zachowaj historię…***, chyba że świadomie chcesz skasować pomiary — to operacja nieodwracalna, która przy VitalSensorze usuwa też próbki tego ula.
- **Nie twórz nowego ula**, jeśli to ta sama rodzina, która przeprowadziła się razem ze swoim ulem — napisz do nas, przeniesiemy ul bez utraty historii.
- **Przerwa w danych podczas przepinania jest normalna.** Wykres w nowym ulu zaczyna się od dnia powiązania, a w starym urywa się w dniu odłączenia.
- **Sprawdź zasięg.** Czujnik musi być w promieniu ok. 30–40 m od Huba swojej nowej pasieki, inaczej po okresie pierwszego połączenia zobaczysz status *poza zasięgiem*.
- **Dodaj notatkę z datą w obu ulach.** Bez niej urwany wykres wygląda później jak awaria sprzętu, a nie jak Twoja decyzja.
- **Nie licz na uśrednienie danych.** Krótka historia w nowym ulu oznacza, że alerty chorobowe i trendy staną się wiarygodne dopiero po kilku dniach.

<a id="zamiana-hubow"></a>

### Ktoś zamienił Huby między pasiekami — co się dzieje i co zrobić?

**Co się dzieje z danymi:** nic nie ginie. Hub jest wyłącznie pośrednikiem, a historia pomiarów zapisuje się pod numerem seryjnym urządzenia. Zamiana ani wymiana Huba nie ucina wykresów, nie kasuje tarowania i nie gubi przybytku miodu.

**Co się dzieje z łącznością:** każdy Hub ma konfigurację z listą urządzeń swojej pasieki. Po fizycznej zamianie Hub stoi przy ulach, których nie ma na swojej liście — te ule przestają raportować i po pewnym czasie pokażą *Brak połączenia*, mimo że baterie są sprawne.

**Co zrobić — najprościej:** zamień Huby z powrotem, każdy na swoje pasieczysko. Urządzenia wrócą do raportowania przy najbliższej synchronizacji i nie musisz nic zmieniać w aplikacji.

**Jeśli Huby mają zostać po zamianie:** Hub pasieki zmienia się w *Ustawienia pasieki* → sekcja **Hub** → ikona kodu QR → zeskanuj kod Huba, który stoi teraz w tej pasiece → zapisz. Jest jednak haczyk: **zamiana „na krzyż" między dwiema Twoimi pasiekami nie uda się w aplikacji**, bo przy próbie przypisania Huba wciąż należącego do drugiej pasieki zobaczysz komunikat *„Hub jest już przypisany do pasieki X. Odłącz urządzenie z pasieki X lub zeskanuj kod QR z innego Hub."* W takiej sytuacji napisz na [bee@apisense.ai](mailto:bee@apisense.ai) — przestawimy Huby po naszej stronie.

Po podmianie Huba w pasiece urządzenia zostają w swoich ulach razem z historią i tarowaniem, ale nawiązują połączenie od nowa — przez chwilę na kafelkach uli zobaczysz *Czekamy na połączenie*.
