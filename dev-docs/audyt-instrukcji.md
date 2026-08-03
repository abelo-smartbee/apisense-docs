# Audyt instrukcji aplikacji — jak go przeprowadzić

Dotyczy `docs/manual/app-manual.{pl,en}.md`. Powstało po audycie z sierpnia 2026
(issue #75, PR #76), który znalazł 11 błędów blokujących i około czterdziestu
mylących — po to, żeby następny przebieg zaczynał od metody, a nie od zera.

## Po co, skoro jest `auto_docs`

W `apisense-mobile` działa workflow `auto_docs.yml`: przy każdym wydaniu
produkcyjnym `deploy_prod.yml` go dyspozycjonuje, ten diffuje release względem
bazy, prosi Claude'a o aktualizację dokumentacji i otwiera tu PR. To działa —
`#19`, `#21` i `#28` powstały tak i zostały zmergowane.

Ten mechanizm **nie zastępuje audytu**, bo widzi wyłącznie jedno okno.
Przykład z audytu: litera zniknęła z kafelka pasieki w maju 2026 (`#150`,
wprowadzenie `_ApiaryCardIcon`). Wszystkie trzy przebiegi `auto_docs` odbyły się
później i żaden jej nie tknął, bo diff release'u jej nie zawierał. Zmiana starsza
niż bieżące okno jest dla diffu niewidoczna na zawsze — i to jest dokładnie ta
klasa rozjazdu, którą audyt ma wyłapywać.

## Kiedy

Co dwa, trzy wydania produkcyjne mobile. Przy obecnym tempie wychodzi mniej
więcej kwartalnie.

## Źródło prawdy: trzy poziomy, nie jeden

Najdroższa lekcja z audytu i z review do niego. Za każdym razem, gdy coś
poszło źle, przyczyną było zatrzymanie się na pierwszym poziomie, który
wyglądał na wystarczający.

**Poziom 1 — wartość w ARB.** `apisense-mobile/packages/apisense_core/l10n/app_{pl,en}.arb`.
Daje dokładne brzmienie etykiety. Nie daje odpowiedzi, czy etykieta gdziekolwiek
występuje.

**Poziom 2 — użycie klucza w Dart.**

```bash
grep -rn "<klucz>" --include='*.dart' lib packages/*/lib | grep -v generated
```

W ARB leży sporo **martwych stringów** — potwierdzone przy audycie:
`notificationTabSuggestions`, `settingsNotificationsSuggestions`,
`settingsUnitSectionTitle`, `taskFilterAll`, `apiaryDetailsShortCode`,
`addApiaryShortNameLabel`, `addHiveCodeLabel`, `authPasswordHintDetailed`.
Zakładka *Sugestie* w powiadomieniach nie istnieje, choć ma komplet tłumaczeń.

**Poziom 3 — czy widget to renderuje.** Tu poległem w review PR `#76`: trzy z
ośmiu uwag dotyczyły tego samego. `avatarText` (kafelek pasieki),
`hiveIdentifier` i `avatarColor` (kafelek ula) są wypełniane w
`apiary_list_view.dart` i `hive_list_tab.dart`, więc na poziomie 2 wszystko się
zgadza. A karty ich nie rysują: `_ApiaryCardHeader` wstawia stałe
`_ApiaryCardIcon`, `_HiveHeader` stałą ikonę `AppAsset.hives` ze sztywnym
kolorem, `hiveIdentifier` nie jest używany nigdzie.

Dodatkowo `edit_apiary_details_screen.dart` naprawdę liczy
`avatar: name[0].toUpperCase()` i wysyła to do backendu. Wartość istnieje,
jest liczona, jest zapisywana — i nie jest pokazywana. **Martwe propsy to ta sama
klasa błędu co martwe stringi ARB, tylko o poziom głębiej.** Dojść do widgetu,
który faktycznie coś rysuje.

## Żywa aplikacja: prod, nie QA

`app.apisense.ai` to produkcja i to ona jest źródłem prawdy dla instrukcji.
`apisense-ab522.web.app` (QA) ma inny build — przy poprzedniej pracy różniło się
menu ⋮ i na podstawie jednego zrzutu z QA skasowałem z instrukcji istniejącą
pozycję *Wyloguj*.

Dwie konsekwencje:

- zrzut z jednego ekranu nie uprawnia do uogólnienia na całą aplikację;
- kod na `main` w mobile bywa **przed** produkcją. Plakietka planu (`AI` / `Pro AI`)
  w ustawieniach konta jest w kodzie renderowana bezwarunkowo, a prod jej nie
  pokazuje — dlatego świadomie nie ma jej w instrukcji. Jeśli coś jest w kodzie,
  ale nie na prodzie, opisujemy prod.

Aplikacja jest Flutterem na web, więc renderuje się do canvas i drzewo
dostępności jest puste. Automatyzacja przeglądarki musi klikać po współrzędnych,
`find` nie zadziała.

## Przebieg

1. **Podziel plik na rozdziały i przejdź je osobno.** Plik ma ~2200 linii na
   locale; jeden przebieg „od góry do dołu" gubi kontekst. Przy `#75` trzy
   niezależne przebiegi po rozdziałach dały komplet.

2. **Każde ustalenie z dowodem** w postaci `plik.dart:linia` albo klucza ARB.
   Ustalenie bez dowodu wraca w review.

3. **Podziel wynik na trzy kategorie**, bo sterują kolejnością pracy:
   - **blokujące** — użytkownik nie wykona opisanego kroku (brakujący krok
     kreatora, wymagane pole, którego nie ma w opisie, ścieżka do nieistniejącej
     zakładki);
   - **mylące** — opis nieprawdziwy, ale nie zatrzymuje użytkownika;
   - **kosmetyczne** — brzmienie etykiety, literówka w nazwie statusu.

4. **Załóż issue** w tym formacie (wzór: `#75`). Kolejna osoba ma wtedy zacząć od
   issue, nie od audytu.

## Wykonanie poprawek

- **PL i EN parami.** Nawigacja jest per-locale w `plugins.i18n.languages[].nav`
  w `mkdocs.yml`; przy nowej stronie trzeba dopisać ją do **obu**, a nie tylko
  do `nav:` na górze.
- **EN ma własne błędy.** Nie jest tłumaczeniem PL jeden do jednego — przy `#76`
  wyszła niespójność `Hive status` / `Hive state` wewnątrz samego pliku EN.
- **Odnośniki do rozdziałów po polsku i angielsku są różne.** Skopiowanie kotwicy
  z PL do EN to najczęstszy błąd przy przenoszeniu treści (`#analiza-danych-i-raporty`
  w pliku EN).
- **Nie zmieniaj nazw plików obrazów.** Patrz niżej.

## Walidacja przed PR

```bash
mkdocs build --strict                        # ta sama komenda co w CI
python3 tools/check_anchors.py --against main
python3 tools/check_image_refs.py --against main
```

Dlaczego to trzy komendy, a nie jedna:

- `mkdocs build --strict` **nie wywraca się** na zerwanej kotwicy wewnątrzstronowej
  — raportuje ją na poziomie INFO i buduje dalej. Link do nieistniejącego nagłówka
  wchodzi na produkcję bez śladu w CI.
- `check_anchors.py` jest tą bramką, której build nie stanowi. Tryb `--against`
  pokazuje wyłącznie to, co zepsuła bieżąca gałąź, więc reorganizacja rozdziałów
  nie tonie w historycznych zgłoszeniach.
- `check_image_refs.py` pilnuje kontraktu z pipeline'em screenshotów w
  `apisense-mobile`, który kluczuje ujęcia po **nazwie pliku** obrazu
  (`integration_test/screenshots/manifest.yaml`). Zmiana nazwy albo skasowanie
  ostatniej referencji nie psuje niczego tutaj — psuje **następną** synchronizację
  screenshotów, w drugim repo, kilka dni później.

Oba skrypty czytają ref przez `git show` i nie dotykają drzewa roboczego. To jest
celowe: oczywista implementacja przez `git stash` + `checkout` potrafi przy czystym
drzewie zdjąć cudzy starszy stash.

## Czego audyt nie obejmuje

- **Oznaczanie funkcji per TIER** — osobny temat. Uwaga: znaczna część ustaleń
  z kategorii „mylące" to w istocie gatowanie planem (`FeatureFlag.diseases`,
  `hardware`, `assistant`, `computerVision`, `guardWrite()`, granica czasowa
  `pro_ai_through`), więc te dwa tematy warto robić razem.
- **Twierdzenia sprzętowe** w „Dobrych praktykach" (2×AA, zasięg BLE ~35 m, panel
  PV) — nie da się ich zweryfikować z repo `apisense-mobile`.
