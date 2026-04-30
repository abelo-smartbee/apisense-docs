# Asystent AI

Asystent AI to **Twój cyfrowy pomocnik w pasiece** — zadasz pytanie, dostaniesz odpowiedź. Działa w aplikacji Apisense Pro AI (mobilnej i w przeglądarce) pod zakładką **Twój asystent** w dolnym menu.

Asystent zna Twoje pasieki, ule, urządzenia, kalendarz przeglądów i pogodę nad ulami. Potrafi też odpowiadać na pytania o pszczelarstwo i podpowiadać, jak coś zrobić w aplikacji.

______________________________________________________________________

## 1. Po co Ci Asystent AI

W codziennej pracy w pasiece pojawiają się pytania, na które trudno szybko znaleźć odpowiedź:

- *„Czy waga w ulu numer 3 jeszcze się łączy?"*
- *„Kiedy ostatni raz robiłem przegląd w pasiece Lipowa?"*
- *„Jak wygląda jutrzejsza prognoza pogody nad moją pasieką?"*
- *„Co zrobić, jeśli widzę pszczoły z deformacją skrzydeł?"*
- *„Jak ustawić alarm w aplikacji, gdy waga ula nagle spadnie?"*

Zamiast klikać po kilku ekranach, czytać dokumentację albo szukać w internecie — pytasz Asystenta. Asystent **sam zajrzy w dane z Twoich czujników IoT, w Twoje notatki, w prognozę pogody, w oficjalne instrukcje Apisense, a nawet w nasze tutoriale wideo** — i odpowie zwięźle, w Twoim języku.

______________________________________________________________________

## 1a. Asystent tłumaczy techniczne dane z czujników

Twój ul przesyła do Apisense dziesiątki odczytów dziennie: masa, temperatura, wilgotność, ciśnienie, status połączenia, poziom baterii. Surowe liczby same w sobie niewiele mówią — trzeba znać kontekst, normy i trendy. Asystent AI bierze te dane i **przekłada je na zwięzłą diagnozę po polsku**.

!!! example "Przykład — surowe dane → zrozumiała odpowiedź"
    **Surowe dane** w bazie Apisense (czego pszczelarz na co dzień nie ogląda):

    > ul 4, pasieka Lipowa: masa 38,2 kg (-0,4 kg / 24h), temperatura wewn. 34,8°C, wilgotność 62%, czujnik bat. 88%, ostatni odczyt 12 min temu

    **Ty:** Co się dzieje w ulu 4 w pasiece Lipowa?

    **Asystent:** Ul 4 (Lipowa) ma się dobrze — temperatura wewnątrz 34,8°C jest w normie dla aktywnego czerwiu, wilgotność 62% prawidłowa. Masa spadła w ciągu doby o 0,4 kg, co przy obecnej pogodzie (brak pożytku, lekki wiatr) jest typowe — nie wskazuje na rojenie ani na problem z rodziną. Czujnik łączy się regularnie, bateria 88%.

To samo dotyczy bramek (Hub) i wag — Asystent **nie zostawia Cię z liczbami**, tylko je interpretuje w kontekście Twojej pasieki, pogody i historii ostatnich przeglądów.

______________________________________________________________________

## 2. Jak otworzyć rozmowę

Zakładka **Twój asystent** jest dostępna w dolnym menu w widokach *Pasieki*, *Ule* i *Ul*. Wejdź w nią, wpisz pytanie w polu na dole ekranu i wyślij.

Asystent odpowiada w czasie rzeczywistym — odpowiedź pojawia się na ekranie niemal natychmiast.

<!-- TODO: screenshot - zakładka "Twój asystent" z przykładowym pytaniem i odpowiedzią -->

______________________________________________________________________

## 3. O co możesz zapytać

Poniżej znajdziesz sześć grup typowych pytań z konkretnymi przykładami. **Możesz pytać własnymi słowami** — Asystent rozumie naturalne sformułowania, niekoniecznie te same co poniżej.

### 3.1 Twoja pasieka i ule

Asystent wie, ile masz pasiek i uli, jak się nazywają i w jakim są stanie.

!!! example "Przykład rozmowy"
    **Ty:** Ile mam aktywnych uli?

    **Asystent:** Masz 12 aktywnych uli rozmieszczonych w 3 pasiekach: Lipowa (5), Akacjowa (4), Wrzosowa (3).

!!! example "Przykład rozmowy"
    **Ty:** Pokaż status pasieki Lipowa.

    **Asystent:** Pasieka **Lipowa** zawiera 5 uli. Bramka jest online (sygnał LTE: dobry, ostatni kontakt: 8 minut temu, bateria: 78%). Najnowsze pomiary z czujników poniżej 24 godzin temu.

!!! example "Przykład rozmowy"
    **Ty:** W której pasiece mam najwięcej uli?

    **Asystent:** Najwięcej uli (5) masz w pasiece **Lipowa**.

### 3.2 Urządzenia i bramki

Asystent zna status każdej bramki (Hub), wagi (Scale) i czujnika (VitalSensor): kiedy ostatnio się łączyły, jaki mają poziom baterii.

!!! example "Przykład rozmowy"
    **Ty:** Czy moja bramka w pasiece Akacjowa ma sygnał LTE?

    **Asystent:** Tak. Bramka w pasiece **Akacjowa** ma dobry sygnał LTE i połączyła się 3 minuty temu. Bateria: 64%.

!!! example "Przykład rozmowy"
    **Ty:** Które wagi mają niski poziom baterii?

    **Asystent:** Dwie wagi mają poziom baterii poniżej 20%:

    - Pasieka **Lipowa**, ul nr 2 — 17%
    - Pasieka **Wrzosowa**, ul nr 1 — 12%

    Zaplanuj wymianę przed kolejnym wyjazdem do pasieki.

!!! example "Przykład rozmowy"
    **Ty:** Kiedy ostatnio łączył się czujnik w ulu nr 3 w pasiece Lipowa?

    **Asystent:** Czujnik w ulu nr 3 (pasieka Lipowa) ostatni raz łączył się 6 godzin temu. To w normie — czujnik wysyła dane co kilka godzin.

### 3.3 Kalendarz i przeglądy

Asystent czyta zaplanowane i wykonane przeglądy oraz zabiegi.

!!! example "Przykład rozmowy"
    **Ty:** Jakie zabiegi mam zaplanowane w tym tygodniu?

    **Asystent:** W tym tygodniu masz zaplanowane 2 zabiegi:

    - **wtorek** — kontrola obecności matki, pasieka Lipowa, ule 1–5
    - **piątek** — zabieg przeciw warrozie, pasieka Akacjowa, ule 1–4

!!! example "Przykład rozmowy"
    **Ty:** Kiedy ostatni raz robiłem przegląd ula 7 w pasiece Wrzosowa?

    **Asystent:** Ostatni przegląd ula 7 w pasiece Wrzosowa odbył się **12 dni temu**. W notatce zaznaczyłeś dobrą kondycję rodziny i zauważalny przybytek miodu.

### 3.4 Pogoda nad pasieką

Asystent automatycznie sięga po pogodę dla lokalizacji Twoich pasiek — nie musisz nawet podawać miasta.

!!! example "Przykład rozmowy"
    **Ty:** Jaka pogoda w pasiece Lipowa dziś?

    **Asystent:** W pasiece **Lipowa** dziś: temperatura 18°C, zachmurzenie częściowe, wiatr 12 km/h z zachodu. Brak opadów. Dobre warunki do lotu pszczół.

!!! example "Przykład rozmowy"
    **Ty:** Czy jutro będzie deszczowo nad moimi pasiekami?

    **Asystent:** Tak — w okolicy pasieki **Akacjowa** jutro od popołudnia spodziewane są opady (5–8 mm). Pozostałe pasieki zostają w strefie suchej.

### 3.5 Wiedza o pszczelarstwie

Asystent korzysta z bazy wiedzy Apisense — odpowie na pytania o choroby pszczół, dobre praktyki, zabiegi i zachowania rodzin pszczelich.

!!! example "Przykład rozmowy"
    **Ty:** Jak rozpoznać warrozę?

    **Asystent:** Warroza to inwazja pasożyta *Varroa destructor*. Najczęstsze objawy:

    - widoczne brązowo-rdzawe kleszcze na pszczołach lub czerwiu;
    - pszczoły z deformacjami skrzydeł (wirus DWV przenoszony przez warrozę);
    - osłabiona, źle zimująca rodzina.

    Diagnostykę robisz najczęściej testem cukrowym lub sypaniem cukru pudru. Apisense odnotowuje też rekomendacje zabiegowe — sprawdź zakładkę *Powiadomienia* → *Problemy*.

!!! example "Przykład rozmowy"
    **Ty:** Kiedy zacząć dokarmianie zimowe?

    **Asystent:** Dokarmianie zimowe rozpoczyna się zwykle na przełomie sierpnia i września — po ostatnim miodobraniu, przed obniżeniem temperatur. Dawki zależą od regionu i siły rodziny. Dla Twoich pasiek mogę sprawdzić ostatnie pomiary wagi i zasugerować, czy któraś rodzina pilnie wymaga karmienia.

### 3.6 Instrukcje obsługi i konfiguracji systemu Apisense

Asystent **został wytrenowany na pełnej oficjalnej dokumentacji Apisense** — instrukcji aplikacji Apisense Pro AI, instrukcji konfiguracji urządzeń (Hub, Scale, VitalSensor), opisie ustawień i powiadomień. Gdy pytasz „jak coś zrobić w aplikacji" albo „jak skonfigurować urządzenie" — Asystent odpowiada wprost z naszej dokumentacji, a nie ze ogólnych źródeł w internecie.

Dodatkowo, gdy do Twojego pytania istnieje **oficjalny tutorial wideo Apisense na YouTube**, Asystent dorzuci konkretny link do filmu — w Twoim języku, jeśli taka wersja jest dostępna. Nie generuje fałszywych adresów: jeśli oficjalny film nie istnieje, link się nie pojawi.

!!! example "Przykład rozmowy — instrukcja w aplikacji + wideo"
    **Ty:** Jak dodać nowy ul w aplikacji?

    **Asystent:** Nowy ul dodajesz w widoku pasieki:

    1. W zakładce *Pasieki* otwórz pasiekę, do której chcesz dodać ul.
    2. W widoku *Ule* kliknij ikonę **+** w prawym górnym rogu.
    3. Wpisz nazwę ula i (opcjonalnie) numer seryjny czujnika.
    4. Zatwierdź.

    Krótki tutorial wideo: [Apisense — dodawanie ula](https://www.youtube.com/) *(link pojawi się tylko, jeśli oficjalny film Apisense jest dostępny w Twoim języku)*.

!!! example "Przykład rozmowy — konfiguracja urządzenia"
    **Ty:** Jak ustawić alarm, gdy waga ula nagle spadnie o 5 kg?

    **Asystent:** Alarm progowy na nagłą zmianę masy ustawiasz w *Ustawieniach ula* → *Alarmy*:

    1. Wybierz ul w widoku *Ule*.
    2. Otwórz *Ustawienia ula* → zakładka *Alarmy*.
    3. Włącz „Alarm spadku masy" i ustaw próg (np. 5 kg / 24h).
    4. Wybierz, jak chcesz dostawać powiadomienie (push, e-mail).
    5. Zapisz.

    Po zapisaniu alarm zacznie działać natychmiast — system będzie monitorował każdy ul niezależnie.

______________________________________________________________________

## 4. Rozmowa pamięta kontekst

Możesz dopytywać tak, jak w normalnej rozmowie — Asystent pamięta, co przed chwilą powiedziałeś.

!!! example "Przykład rozmowy"
    **Ty:** Jaki jest status pasieki Lipowa?

    **Asystent:** Pasieka Lipowa: 5 uli, bramka online, ostatni kontakt 4 minuty temu...

    **Ty:** A w pasiece Akacjowa?

    **Asystent:** Pasieka Akacjowa: 4 ule, bramka online, ostatni kontakt 8 minut temu...

Każda rozmowa jest zapisana w Twoim koncie — możesz wrócić do niej później albo usunąć ją w ustawieniach. Możesz też zacząć **nową rozmowę** od zera, jeśli chcesz przejść na inny temat bez historii.

______________________________________________________________________

## 5. Wiele języków

Pisz po polsku, angielsku, niemiecku, włosku albo francusku — Asystent **odpowie w tym samym języku**, w którym napisałeś pytanie. Język aplikacji nie musi być ten sam co język rozmowy: możesz mieć aplikację po polsku i pytać Asystenta po angielsku.

______________________________________________________________________

## 6. Dobre praktyki pytań

Im konkretniej zapytasz, tym konkretniej dostaniesz odpowiedź. Kilka prostych zasad:

- **Podaj nazwę pasieki lub numer ula**, jeśli chcesz dane konkretnej pasieki: *„Status pasieki Lipowa"* zamiast *„Status mojej pasieki"*.
- **Pytaj wprost** — Asystent rozumie krótkie pytania równie dobrze co długie.
- **Nie potrzebujesz słów kluczowych** — pisz tak, jak mówisz.
- **Możesz dopytywać** — gdy odpowiedź jest zbyt ogólna, doprecyzuj („A z ostatniego tygodnia?", „Tylko ule z niską baterią").

______________________________________________________________________

## 7. Kiedy AI nie zna odpowiedzi

Asystent jest pomocny, ale nie wszechwiedzący. W kilku sytuacjach uczciwie powie *„nie wiem"* zamiast zgadywać:

- **Pytania o cudze pasieki** — Asystent widzi tylko Twoje dane (lub pasieki, do których masz uprawnienia).
- **Zdjęcia, audio, wideo** — Asystent pracuje na tekście. Nie analizuje fotografii pszczół ani nagrań ula.
- **Bardzo świeże dane** — jeśli czujnik właśnie się rozłączył, Asystent powie, że ostatnia odczytana wartość pochodzi sprzed kilku minut.
- **Działania w pasiece** — Asystent **nie wykona** akcji za Ciebie (nie zmieni alarmu, nie usunie ula). Powie Ci, jak to zrobić w aplikacji.

Jeśli odpowiedź wydaje Ci się błędna albo niepełna — zgłoś to (przycisk oceny rozmowy w aplikacji). Pomaga to ulepszać Asystenta.

Pełną listę ograniczeń znajdziesz w [Możliwości i prywatność](limits-privacy.md).
