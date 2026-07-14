# Rozwiązywanie problemów

## 1. Lista problemów i proponowane rozwiązania

| Nr  | Problem                                                                      | Urządzenie  | Proponowane rozwiązanie                                                                                                                                                                                                                                                                                                                                                                                                               |
| --- | ---------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Urządzenie nieaktywne (nigdy się nie zgłosiło)                               | VitalSensor | 1. Sprawdź poprawność montażu baterii. Wyjmij baterię i włóż ponownie, zwracając uwagę na polaryzację. 2. Sprawdź, czy bateria nie jest rozładowana. Jeśli jest - wymień baterię. **Uwaga**: po poprawnym montażu baterii dioda LED powinna się zaświecić. 3. Jeśli problem nadal występuje lub przewody zostały uszkodzone, skontaktuj się z pomocą Apisense.                                                                         |
| 2   | Rozładowana bateria / bardzo niski poziom baterii                            | VitalSensor | Wymień baterie, zwracając uwagę na polaryzację. **Uwaga**: po poprawnym montażu baterii dioda LED powinna się zaświecić. Po wymianie baterii nie trzeba ponownie parować urządzenia, zmieniać ustawień w aplikacji ani resetować Huba — wystarczy umieścić urządzenie w zasięgu Huba i poczekać na synchronizację (szczegóły: [FAQ — po wymianie baterii](../../faq/index.md#po-wymianie-baterii)). Jeśli problem nadal występuje lub przewody zostały uszkodzone, skontaktuj się z pomocą Apisense.                                                                                                                                                                                                              |
| 3   | Brak komunikacji z Apisense Hubem mimo poprawnego zasilenia (brak zasięgu BLE) | VitalSensor | Umieść VitalSensor bliżej Apisense Huba. W ciągu 12 godzin VitalSensor powinien pojawić się w systemie. Jeśli problem nadal występuje, skontaktuj się z pomocą Apisense.                                                                                                                                                                                                                                                                       |
| 4   | Słaby zasięg BLE (poniżej -90 dBm)                                           | VitalSensor | Odwróć VitalSensor w ramce lub całą ramkę o 180° (dioda LED w VitalSensorze skierowana w stronę Apisense Huba). Poziom sygnału powinien się zwiększyć powyżej -90 dBm. Jeśli problem nadal występuje, rozważ zmianę lokalizacji Huba, tak by był bliżej VitalSensora. Należy zadbać, aby nie pogorszyć zasięgu pozostałych urządzeń. W razie problemów skontaktuj się z pomocą Apisense.                                                             |
| 5   | Brak komunikacji z Apisense Hubem (brak zasięgu BLE)                           | Scale       | Umieść Scale bliżej Apisense Huba. W ciągu 12 godzin urządzenie powinno pojawić się w panelu Jeśli problem nadal występuje, skontaktuj się z pomocą Apisense.                                                                                                                                                                                                                                                                           |
| 6   | Słaby zasięg BLE (poniżej -90 dBm)                                           | Scale       | Upewnij się, że elektronika urządzenia Scale jest skierowana w stronę Apisense Huba. Rozważ zmianę lokalizacji Apisense Huba (bliżej Scale), dbając o zasięg pozostałych urządzeń. Poziom sygnału powinien się zwiększyć powyżej -90 dBm. Jeśli problem nadal występuje rozważ zmianę lokalizacji Huba, tak by był bliżej Scale. W razie problemów skontaktuj się z pomocą Apisense.                                                                   |
| 7   | Dioda LED się nie zaświeca po włączeniu przycisku „Power”                    | Hub         | Sprawdź zasilanie - jeżeli Hub nie otrzymuje wystarczającej ilości światła rozważ zmianę jego położenia (nachylenie, wysokość) lub użyj zewnętrznego zasilania. Pozwól Hubowi się naładować (ok. 3 godziny), po czym kliknij przycisk "Power" - dioda LED powinna się zaświecić, a w ciągu 90 minut Apisense Hub powinien pojawić się w panelu. Jeśli Apisense Hub nie był ładowany przez dłuższy czas — patrz problem „Brak ładowania”. |
| 8   | Brak ładowania                                                               | Hub         | Sprawdź podłączenie panelu zasilającego do Apisense Huba. Upewnij się, że ustawienie panelu jest prawidłowe (miejsce nie jest zacienione, panel skierowany w kierunku słońca, nachylenie minimum 20°). W panelu powinno być widoczne ładowanie Apisense Huba. Jeśli problem nadal występuje, skontaktuj się z pomocą Apisense.                                                                                                          |
| 8a  | Hub wolno się ładuje / szybko się rozładowuje / poziom baterii utknął na niskim % przy zasilaniu zewnętrznym (zasilacz DC) | Hub | Najczęstszą przyczyną jest spadek napięcia na złączu DC, a nie sam zasilacz. Sprawdź, czy używasz właściwego wtyku DC (pin **2,1 mm**, średnica zewnętrzna **5,5 mm**) i czy jest dociśnięty do oporu. Przejdź checklistę w sekcji [Diagnostyka zasilania zewnętrznego (zasilacz DC)](#3-diagnostyka-zasilania-zewnętrznego-zasilacz-dc) poniżej. Przy braku poprawy skontaktuj się z pomocą Apisense. |
| 9   | Częsty status „Pasieka nieaktywna” / brak zasięgu Hub                        | Hub         | Przejdź checklistę w sekcji [Diagnostyka Hub — brak zasięgu](#2-diagnostyka-hub-brak-zasięgu) poniżej. Przy braku poprawy skontaktuj się z pomocą Apisense.                                                                                                                                                                                                                                                                            |
| 10  | Słaby sygnał z urządzeniami (BLE poniżej -90 dBm)                            | Hub         | Obróć Apisense Hub o 90° w osi pionowej. Po 12 godzinach sprawdź poziom sygnału w panelu; w razie potrzeby powtórz. Jeśli problem nadal występuje rozważ zmianę lokalizacji Apisense Huba; sprawdź przeszkody (metal, linie energetyczne). Przy braku poprawy — zgłoś do Apisense. Przy braku poprawy skontaktuj się z pomocą Apisense.                                                                                                |
| 11  | Inne problemy                                                                | —           | Skontaktuj się z Apisense: **[bee@apisense.ai](mailto:bee@apisense.ai)**.                                                                                                                                                                                                                                                                                                                                                             |

## 2. Diagnostyka Hub — brak zasięgu

Jeśli Hub nie raportuje danych lub pojawia się status „Pasieka nieaktywna”, przejdź po kolei poniższą listę kontrolną.

1. **Antena dokręcona** — sprawdź, czy obie anteny (BLE i LTE) są mocno dokręcone do gniazd Huba.
2. **Anteny pionowo do góry** — anteny muszą być skierowane pionowo, nigdy poziomo ani w dół.
3. **Hub na zewnątrz** — urządzenie nie może znajdować się pod dachem ani w pomieszczeniu (wymagane przez GPS i zasięg sieci komórkowej).
4. **Brak przeszkód w pobliżu** — sprawdź, czy obok Huba nie ma dużych metalowych przedmiotów ani linii energetycznych.
5. **Panel solarny** — kierunek na słońce, nachylenie min. 20°, brak zacienienia. W aplikacji powinno być widoczne ładowanie.
6. **Zasięg sieci komórkowej w lokalizacji** — sprawdź telefonem na miejscu, czy w danym punkcie jest zasięg LTE/GSM. Bez zasięgu Hub nie wyśle danych.

Jeśli po sprawdzeniu listy problem nadal występuje, napisz do nas na **[bee@apisense.ai](mailto:bee@apisense.ai)** i **dołącz zdjęcie miejsca zamontowania Huba** (widoczne otoczenie, panel solarny, anteny) — przyspieszy to diagnozę.

## 3. Diagnostyka zasilania zewnętrznego (zasilacz DC)

Jeśli Hub jest zasilany zewnętrznym zasilaczem DC, a mimo to ładuje się wolno, szybko się rozładowuje lub poziom baterii utrzymuje się na niskim poziomie, najczęstszą przyczyną jest **spadek napięcia na złączu DC**, a nie sam zasilacz. Przejdź po kolei poniższą listę kontrolną.

1. **Pomiar napięcia na wejściu Huba** — zmierz napięcie nie na zasilaczu, lecz na samym wtyku wpiętym do gniazda Huba. Zasilacz 12 V pokazujący ok. 12,3 V jest prawidłowy; problemem jest sytuacja, gdy na wejściu Huba napięcie jest zauważalnie niższe (np. ok. 11 V) — to oznacza spadek na złączu.
2. **Średnica pinu wtyku** — Hub wymaga wtyku DC z pinem **2,1 mm** (średnica zewnętrzna **5,5 mm**). Wtyk **2,5 mm** nie daje prawidłowego styku i jest częstą przyczyną takiego objawu.
3. **Średnica obudowy wtyku** — czarna plastikowa obudowa wtyku powinna mieć **maksymalnie 9 mm** średnicy. Grubsza obudowa nie wejdzie do końca w tulejkę w obudowie Huba i nie dociśnie styku.
4. **Wtyk dociśnięty do oporu** — upewnij się, że wtyk jest wciśnięty do końca.

Rekomendowany wtyk: **DC 2,1 / 5,5 mm**, męski, z kablem.

Jeśli po sprawdzeniu listy problem nadal występuje, napisz do nas na **[bee@apisense.ai](mailto:bee@apisense.ai)**.

## 4. Po wymianie baterii w Scale lub VitalSensor

Po rutynowej wymianie baterii (2× AA) w urządzeniu Scale lub VitalSensor **nie są wymagane** żadne dodatkowe czynności w aplikacji ani na urządzeniu Hub, Scale ani VitalSensor. Nie należy ponownie parować urządzeń, dodawać ich do ula ani naciskać przycisku RESET.

Po wymianie baterii wystarczy:

- ponownie umieścić urządzenie w jego docelowym miejscu,
- upewnić się, że znajduje się ono w zasięgu Huba (maksymalnie około 35 m),
- poczekać na kolejny cykl pomiarowy.

Zaktualizowane dane pojawią się w aplikacji automatycznie — może to potrwać do kilku godzin, pod warunkiem że Hub poprawnie komunikuje się z systemem i nie jest w trybie offline.

Szczegółowe instrukcje wymiany baterii oraz odpowiedzi na najczęstsze pytania: [FAQ — po wymianie baterii](../../faq/index.md#po-wymianie-baterii).

Po rozładowaniu Huba i ponownym podłączeniu go do ładowania lub wystawieniu na słońce Hub automatycznie wznowi pracę — **nie naciskaj** przycisku RESET.
