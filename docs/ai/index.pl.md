# Asystent

Asystent w Apisense to nie ogólny chatbot z internetu. To **dedykowany asystent zintegrowany z całym Twoim systemem Apisense** — czyta na bieżąco dane z czujników IoT w Twoich ulach, zna każdą notatkę i każdy przegląd, który wpisałeś w aplikacji, sięga po prognozę pogody dla Twojej pasieki, zna oficjalne instrukcje obsługi i konfiguracji systemu Apisense oraz materiały wideo na naszym kanale YouTube.

Innymi słowy: Asystent **tłumaczy surowe dane techniczne z systemu IoT na proste odpowiedzi po polsku**. Zamiast przeglądać tabelę z odczytami wagi sprzed 24 godzin — pytasz „czy w ulu numer 3 dzieje się coś niepokojącego?” i dostajesz konkretną odpowiedź.

Nie musisz uczyć się żadnych komend ani filtrów. Wystarczy, że zadasz pytanie tak, jak zadałbyś je sąsiadowi-pszczelarzowi.

______________________________________________________________________

## 1. Po co Ci Asystent

Asystent to **inteligentny czat dostępny w aplikacji mobilnej i w przeglądarce**. Zadajesz pytanie, dostajesz odpowiedź. Asystent zna Twoje pasieki, ule, status urządzeń, zaplanowane przeglądy i pogodę — i potrafi odpowiedzieć na pytania od „Ile mam uli?” po „Jak rozpoznać warrozę?” i „Jak ustawić alarm wagi w aplikacji?”.

Wszystkie szczegóły, przykłady rozmów i dobre praktyki znajdziesz w [pełnym opisie Asystenta →](assistant.md)

______________________________________________________________________

## 2. Skąd Asystent czerpie wiedzę

Asystent łączy **sześć niezależnych źródeł** Twojej pasieki i wiedzy Apisense, żeby odpowiadać konkretnie i na temat. To jest właśnie to, co odróżnia go od ogólnego chatbota:

- **Dane z systemu IoT** — Asystent czyta na bieżąco surowe odczyty z Twoich urządzeń: wagi (Scale) — masa ula, temperatura, wilgotność; czujniki (VitalSensor) — temperatura i parametry wewnątrz ula; bramki (Hub) — sygnał LTE, poziom baterii, ostatni czas połączenia. Te liczby przekłada na zrozumiały komentarz („wszystko w normie”, „bateria do wymiany w przyszłym tygodniu”, „brak kontaktu od 2 dni — sprawdź urządzenie”).
- **Twoje wpisy w aplikacji** — wszystko, co sam wprowadzasz: notatki, opisy przeglądów, kalendarz zabiegów, oznaczone choroby, zarejestrowane próbki i badania. Asystent zestawia te informacje z aktualnymi pomiarami z czujników.
- **Pogoda dla Twoich pasiek** — Asystent automatycznie pobiera prognozę pogody dla **konkretnej lokalizacji** każdej Twojej pasieki. Nie musisz podawać miasta — Asystent wie, gdzie stoją Twoje ule.
- **Baza wiedzy Apisense o pszczelarstwie** — choroby pszczół (warroza, nosema, zgnilec), zalecane terminy zabiegów, dobre praktyki zarządzania pasieką. Materiały przygotowane przez ekspertów Apisense.
- **Oficjalne instrukcje systemu Apisense** — pełna dokumentacja konfiguracji urządzeń (Hub, Scale, VitalSensor), instrukcja aplikacji Apisense Pro AI, opis ustawień konta i powiadomień. Gdy pytasz „jak ustawić alarm wagi” albo „jak podłączyć nową bramkę” — Asystent odpowiada wprost z naszej dokumentacji.
- **Materiały wideo Apisense na YouTube** — gdy do Twojego pytania istnieje **oficjalny tutorial wideo Apisense**, Asystent dorzuci do odpowiedzi konkretny link do filmu — w Twoim języku, jeśli taka wersja jest dostępna.

______________________________________________________________________

## 3. O co możesz zapytać Asystenta

Asystent odpowiada na pytania w sześciu głównych obszarach. Pełne przykłady rozmów i odpowiedzi znajdziesz w [pełnym opisie Asystenta](assistant.md):

- **Twoja pasieka i ule** — np. „Ile mam aktywnych uli?”, „Pokaż status pasieki Lipowa”.
- **Urządzenia i bramki** — np. „Które wagi mają niski poziom baterii?”, „Czy moja bramka ma sygnał LTE?”.
- **Kalendarz i przeglądy** — np. „Jakie zabiegi mam zaplanowane w tym tygodniu?”, „Kiedy ostatni raz robiłem przegląd ula 7?”.
- **Pogoda nad pasieką** — np. „Jaka pogoda w pasiece Lipowa dziś?”, „Czy jutro będzie deszczowo?”.
- **Wiedza o pszczelarstwie** — np. „Jak rozpoznać warrozę?”, „Kiedy zacząć dokarmianie zimowe?”.
- **Instrukcje aplikacji i konfiguracji urządzeń** — np. „Jak dodać nowy ul w aplikacji?”, „Jak ustawić alarm spadku masy?”.

______________________________________________________________________

## 4. Czego Asystent nie zrobi

Asystent to pomocnik — nie wykonuje działań w pasiece za Ciebie:

- Nie zmienia ani nie usuwa danych w aplikacji (nie skasuje ula, nie doda przeglądu, nie wystawi alarmu).
- Nie analizuje zdjęć, nagrań audio ani wideo. Pracuje wyłącznie na tekście.
- Nie zna informacji o cudzych pasiekach (zobacz [Możliwości i prywatność](limits-privacy.md)).

Pełną listę ograniczeń i zasady prywatności znajdziesz na osobnej stronie.

______________________________________________________________________

## 5. Twoja prywatność

Asystent widzi tylko **Twoje** dane (lub pasieki, do których masz dostęp). Twoje rozmowy są zapisywane, żebyś mógł do nich wrócić — ale możesz je w każdej chwili usunąć. Dane nie są wykorzystywane do trenowania modeli zewnętrznych firm.

Szczegóły: [Możliwości i prywatność →](limits-privacy.md)

______________________________________________________________________

## 6. Jak zacząć

Asystent jest wbudowany w aplikację Apisense Pro AI:

- W aplikacji mobilnej i w wersji przeglądarkowej dostępny jest pod ikoną **Twój asystent** w dolnym menu.
- Działa w widokach *Pasieki*, *Ule* i *Ul*, więc pomoc jest pod ręką niezależnie od tego, gdzie aktualnie pracujesz.
- Pisz w swoim języku — Asystent odpowiada w tym samym języku, w którym zadałeś pytanie.

<!-- TODO: screenshot - widok zakładki "Twój asystent" z otwartą pustą rozmową -->
