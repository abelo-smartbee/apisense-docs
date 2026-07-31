# ADR 0004: Kod locale dla portugalskiego — `pt` czy `pt-BR`

Data: 2026-07-31 · Status: **zaakceptowany** 2026-07-31 — przyjęto rekomendację
`pt` z etykietą „Português (Brasil)". #49 zamyka się bez zmiany w kodzie, #62
traci blokadę i wchodzi jako zwykły locale dwuznakowy.

## Kontekst

Epik #47 dokłada instrukcji montażu dwanaście języków. Jedenaście z nich ma kod
dwuliterowy (`cs sk hu el hr fi nl ro sv da ar`). Dwunasty, `pt-BR`, jest
**jedynym kodem z myślnikiem w całej dwudziestce** — i cały mechanizm i18n tej
strony zakłada, że locale ma dokładnie dwa znaki.

`lang="pt-BR"` jest poprawnym BCP 47 i przeglądarka rozumie go bez zastrzeżeń.
Nie rozumieją go nasze wzorce. Stąd #49, który blokuje #62 (tłumaczenie PT-BR) i
wypada poza falę #51 (szkielet dla dziewięciu locale łacińskich) — pozostałe
dziewięć rusza bez żadnej pracy strukturalnej, `pt-BR` czeka na tę decyzję.

Pytanie jest tańsze niż implementacja: **czy w ogóle potrzebujemy podznacznika
regionu.** Jeśli wystarczy `pt`, ten ticket znika, a #62 wchodzi do fali #51.

## Prawdziwy zasięg zmiany

Ticket wymienił pięć miejsc z pamięci. Po przejściu kodu jest ich **trzynaście w
pięciu plikach**, a dwa z najbardziej podstępnych nie były wymienione wcale.

| Plik:linia | Co zakłada dwa znaki | W tickecie? |
|---|---|---|
| `tools/i18n_lib.py:31` | `LOCALE_ORDER` — lista, przez którą filtruje się wszystko pozostałe | nie |
| `tools/i18n_lib.py:36` | `_OPEN`: `lang="([a-z]{2})"` — **z flagą `re.I`** | regex tak, flaga nie |
| `tools/check_i18n.py:43` | `DEFAULT_LOCALES` | nie |
| `tools/check_i18n.py:57` | reguły CSS: `\[data-lang="([a-z]{2})"\] \[lang\]` | tak |
| `tools/check_i18n.py:58` | allowlist w `<head>`: `'([a-z]{2})'(?=[,\]])` | tak |
| `tools/check_i18n.py:59` | pigułki: `data-set-lang="([a-z]{2})"` | tak |
| `tools/check_i18n.py:60` | `<option value="([a-z]{2})"` | tak |
| `tools/check_i18n.py:61` | `HEAD_TEXT`: `^\s{4}([a-z]{2}): \{$` — zakłada też **klucz bez cudzysłowu** | regex tak, cudzysłów nie |
| `tools/check_i18n.py:69` | `if loc in LOCALE_ORDER` — filtr wrażliwy na wielkość liter | nie |
| `tools/build_pdf.py:27` | `LOCALES` — klucze i nazwy plików PDF | tak (w kryteriach) |
| `tools/i18n_inject.py:33` | `I18N / f"{locale}.json"` — nazwa pliku tłumaczenia | nie |
| `docs/assembly/index.html:24` | allowlist w bootstrapie: `['pl','en',…].indexOf(l)` | tak |
| `docs/assembly/index.html:1474` | `langSpan('pl', …)`, `langSpan('en', …)` — **dymki szyny generowane w JS, tylko PL/EN** | **nie** |

Do tego miejsca, które zmieniają się mechanicznie razem z każdym locale i nie
wymagają decyzji: `index.html:2` (`<html lang>`), `:109–116` (osiem reguł CSS),
`:798–805` (pigułki), `:811–818` (`<option>`), `:1622–1661` (`HEAD_TEXT`),
`check_i18n.py:95` i `i18n_inject.py:53` (walidacja `--locales`).

Ticket **nie przeszacował** — przeszacowaniem byłoby wymienić coś, czego nie ma.
Niedoszacował: pominął listę, przez którą filtrują wszystkie pozostałe
(`LOCALE_ORDER`), flagę `re.I`, cudzysłowy w `HEAD_TEXT` i runtime'owy
`langSpan`.

## Co się psuje poza regexami

Pięć rzeczy, które przechodzą happy path i gubią locale po cichu. Wszystkie
sprawdzone na tej wersji plików, nie z pamięci.

**1. `re.I` w `_OPEN` znosi kontrolę wielkości liter.** Naiwne rozszerzenie do
`[a-z]{2}(?:-[A-Z]{2})?` przy `re.I` łapie równie chętnie `pt-br`, `PT-BR` i
`Pt-Br`, a `Element.locale` niesie dalej to, co było w pliku. `by_locale` kluczuje
po tym stringu, więc grupa ze spanem `pt-br` zgłasza brak `pt-BR` — 148 grup
niekompletnych przy komplecie tłumaczeń. Rozszerzenie regexa bez **normalizacji do
formy kanonicznej w jednym miejscu** jest gorsze niż brak rozszerzenia, bo błąd
przestaje być czytelny.

**2. `[data-lang=…]` i `[lang=…]` zachowują się różnie.** Sprawdzone w Chrome
headless na stronie testowej:

```
[lang="pt-br"]      dopasowuje  lang="pt-BR"        → true
[data-lang="pt-br"] dopasowuje  data-lang="pt-BR"   → false
```

`lang` jest na spisie atrybutów, które HTML porównuje w selektorach bez względu na
wielkość liter; `data-*` nie jest. Reguła `[data-lang="pt-BR"] [lang]:not([lang="pt-BR"])`
składa się z obu naraz. Skutek: `data-lang="pt-br"` (z `localStorage`, z ręcznej
edycji, z `build_pdf.py`) nie trafia w żadną regułę — **żaden `[lang]` nie zostaje
ukryty i strona pokazuje wszystkie dwadzieścia języków naraz.** To dokładnie ten
failure mode, przed którym broni `check_i18n.py`, tyle że nieosiągalny statycznie.

**3. `HEAD_TEXT` wymaga cudzysłowów.** Wszystkie osiem kluczy to dziś gołe
identyfikatory (`pl: {`). `pt-BR: {` jest błędem składni JS — trzeba `'pt-BR': {`.
Wzorzec walidatora (`^\s{4}([a-z]{2}): \{$`) tego wariantu nie widzi, więc po
poprawnym dopisaniu klucza walidator zgłosi „brak pt-BR w HEAD_TEXT". Gorzej:
`HEAD_TEXT[cur] || HEAD_TEXT.pl` (`:1682`) **cicho wraca do polskiego** — brak
klucza to polski `<title>` i polski `<meta description>` na brazylijskiej stronie,
bez śladu w konsoli. Epik #47 sam nazywa `HEAD_TEXT` najsłabiej zweryfikowaną
częścią gałęzi.

**4. Nazwa pliku tłumaczenia.** `tools/i18n/pt-BR.json` jest poprawne, ale na
systemie plików bez rozróżniania wielkości liter (macOS, Windows) `pt-br.json` i
`pt-BR.json` to ten sam plik. `i18n_inject.load()` (`:33`) sklei ścieżkę z
czegokolwiek dostanie i wczyta plik o innej nazwie niż zapisana w gicie.

**5. Nazwa PDF-a.** `Apisense_BOX_Instrucoes_de_montagem_pt-BR.pdf` — myślnik w
nazwie pliku jest bezpieczny (`_pl.pdf` → `_pt-BR.pdf`), ale łamie obecną
konwencję sufiksu i jest jedyną nazwą z wielką literą w środku. Kosmetyka, nie
blokada.

Dodatkowo, niezależnie od tej decyzji: **dymki na szynie nawigacji są od zawsze
tylko PL/EN.** `index.html:1474` buduje je z `data-title-pl` / `data-title-en`
(20 slajdów × 2 atrybuty), a reguła CSS ukrywa `[lang]` inne niż bieżący — więc w
`de fr es it no tr` dymek jest **pusty już dziś**. `check_i18n.py` tego nie widzi,
bo te spany powstają w JS, nie w źródle HTML. Nowy locale, jakkolwiek nazwany,
dziedziczy tę dziurę.

## Strona językowa

Instrukcja montażu to nie tekst marketingowy: 148 grup zdań rozkazujących o
przykręcaniu sprzętu i o przechodzeniu przez ekrany aplikacji. Ale te dwie połowy
zachowują się zupełnie inaczej.

**Połowa sprzętowa jest praktycznie identyczna w obu wariantach.** Słownictwo
pszczelarskie jest wspólne (`colmeia`, `apiário`, `quadro`, `melgueira`), tak samo
montażowe (`parafuso`, `fita`, `pilhas AA`), a nazwy urządzeń zostają po angielsku
(`Hub`, `Scale`, `VitalSensor`, `ColonyLink`) — tak jak ustalono przy es/it/no/tr.

**Połowa aplikacyjna ma realny rozjazd leksykalny**, i to na słowach, które w tym
dokumencie występują często (liczby z polskich spanów):

| PT-PT | PT-BR | wystąpień |
|---|---|---|
| `ecrã` | `tela` | ekran ×7 |
| `telemóvel` | `celular` | telefon ×4 |
| `aplicação` | `aplicativo` | aplikac* ×14 |
| `utilizador` | `usuário` | ×1 |
| `ficheiro` | `arquivo` | plik* ×14 |
| `guardar` | `salvar` | tylko w `HEAD_TEXT` („Zapisz jako PDF") |

Tryb rozkazujący zbiega się w obu wariantach (`Toque em`, `Digite`), więc gramatyka
nie jest problemem — problemem jest kilkanaście rzeczowników. Teza z ticketu, że
„różnice w tekście technicznym są niewielkie", jest **prawdziwa dla montażu i
fałszywa dla przejścia przez aplikację**.

To jednak nie jest argument za `pt-BR` jako kodem, bo nikt nie proponuje dwóch
tłumaczeń. Piszemy jeden tekst portugalski i jedyne pytanie brzmi: w którym
wariancie go napisać i jaką etykietą go podpisać. Wariant brazylijski jest
oczywisty (Brazylia to rynek, Portugalia nie jest w planie). Kod to osobna sprawa:
`pt` **nie twierdzi, że tekst jest europejski** — po prostu nie deklaruje regionu.
Tekst brazylijski pod kodem `pt` jest poprawny; niedookreślony, nie błędny.

## Decyzja (propozycja)

**Zostajemy przy `pt`.** Tekst piszemy w wariancie brazylijskim, a w przełączniku
podpisujemy go jawnie: `<option value="pt">Português (Brasil)</option>` i pigułka
`PT`. Kod dwuliterowy, etykieta brazylijska.

Konsekwencja proceduralna: **#49 zamyka się bez zmiany w kodzie**, a #62 przestaje
być blokowane i wchodzi do fali #51 jako dziesiąty locale łaciński.

Czytelnik dostaje ten sam sygnał („to jest wersja brazylijska") w miejscu, w
którym faktycznie patrzy — na liście języków. Tracimy wyłącznie maszynowo
czytelną regionalność w `<html lang>`, a w tym repo **nikt jej nie konsumuje**:
strona nie robi negocjacji treści, nie ma hyphenation per region, PDF-y adresuje
się nazwą pliku, `mkdocs-static-i18n` nie obejmuje `docs/assembly/index.html`
(to surowy HTML, nie para `.pl.md`/`.en.md`).

## Rozważone alternatywy

| Opcja | Werdykt | Powód |
|---|---|---|
| `pt-BR` teraz — rozszerzyć wzorce do `[a-z]{2}(?:-[A-Z]{2})?` + normalizacja + test negatywny | odrzucona (na dziś) | trwałe zerwanie inwariantu „locale = 2 znaki" w 13 miejscach dla **1 z 20** locale; zysk czysto deklaratywny, a przy okazji wchodzą pułapki 1–3 powyżej |
| `pt-BR` i `pt-PT` jako dwa tłumaczenia | odrzucona | 148 grup × 2 do utrzymania w nieskończoność za kilkanaście rzeczowników; Portugalia nie jest w planie #47 |
| `pt` z tekstem europejskim | odrzucona | rynkiem jest Brazylia; `tela`/`celular` czyta się w Portugalii lekko obco, `ecrã`/`telemóvel` w Brazylii **czyta się jak obcy język** — asymetria jest realna |
| `br` jako kod | odrzucona | `br` to bretoński (ISO 639-1); byłby to błąd, nie skrót |
| Odłożyć decyzję, wypuścić 19 locale bez portugalskiego | odrzucona | #62 stoi bez powodu, a decyzja nie tanieje z czasem |

## Koszt odwrotu

Kluczowe pytanie, bo to ono czyni tę decyzję odwracalną: **ile kosztuje `pt` →
`pt-BR`, jeśli marketing zmieni zdanie po wydaniu?**

1. Praca strukturalna z sekcji „Prawdziwy zasięg" — dokładnie ta sama, ani mniej,
   ani więcej. Nie znika, tylko się odkłada.
2. `git mv tools/i18n/pt.json tools/i18n/pt-BR.json` — treść bez zmian, klucze to
   identyfikatory grup, nie locale.
3. Jedna podmiana `lang="pt"` → `lang="pt-BR"` na ~148 spanach w `index.html` plus
   pięć list przełącznika. Mechaniczne, a wynik weryfikuje `check_i18n.py`, który
   dla tego locale zgłosi 148 braków, jeśli podmiana będzie niepełna.
4. Nowa nazwa PDF-a i jeden komunikat w release notes.

Czyli: koszt późniejszy = koszt dzisiejszy **+ jedna mechaniczna podmiana pod
nadzorem walidatora**. Ta nadwyżka jest rzędu godziny. Odwrotnie — zrobienie
`pt-BR` dziś nie zwraca się nigdy, jeśli marketing nigdy o to nie poprosi.

Jedyny scenariusz, w którym `pt` wychodzi drożej, to **dołożenie kiedyś
portugalskiego europejskiego**: wtedy trzeba i rozszerzyć wzorce, i przenieść
istniejące `pt` na `pt-BR`, i dopisać `pt-PT` — dwie migracje zamiast jednej.
Warunkiem uznania tej decyzji za złą jest więc konkretna decyzja biznesowa o
rynku portugalskim, a nie samo pojawienie się `pt-BR` w cudzej tabelce.

## Konsekwencje

- #49 zamyka się jako „nie robimy"; #62 traci blokadę i idzie razem z #51.
- Zostaje inwariant **locale = dokładnie dwa znaki `[a-z]`**, obowiązujący dla
  wszystkich dwudziestu. Warto go zapisać w `dev-docs/glossary.md`, żeby następny
  kod z myślnikiem trafił na tę decyzję, a nie na `AssertionError`.
- Tłumaczenie #62 dostaje jawną instrukcję: **wariant brazylijski**, z tabelką
  `tela`/`celular`/`aplicativo`/`usuário`/`arquivo` jako obowiązującą, oraz
  `salvar` w `HEAD_TEXT`.
- W przełączniku etykieta „Português (Brasil)" przy kodzie `pt` — pozorna
  niespójność, którą ten ADR jest jedynym miejscem tłumaczącym. Bez niego wygląda
  jak przeoczenie.
- Pułapki 1–3 **nie znikają, tylko przestają być pilne**. Zostają tu opisane, żeby
  dzień, w którym pierwszy hyphenated locale jednak wejdzie, nie zaczynał się od
  zera. Do tego czasu warto niezależnie: dopisać brakujący test negatywny
  (`check_i18n.py` nie ma dziś **żadnego** testu — repo nie ma katalogu testów) i
  zdecydować, co zrobić z pustymi dymkami szyny w locale innych niż PL/EN.

## Aktualizacja po scaleniu gałęzi integracyjnej (2026-07-31)

Rekomendacja stoi bez zmian — `pt`, tekst brazylijski, etykieta „Português
(Brasil)". Zmieniło się natomiast to, co ten ADR opisuje jako stan kodu: #50
usunął pigułki, a #51 dołożył dziewięć locale, więc numery linii i jedna pozycja
tabeli są nieaktualne. Poniżej sprostowanie, żeby dzień wdrożenia nie zaczynał
się od szukania nieistniejących miejsc.

**„Prawdziwy zasięg" to dziś dwanaście miejsc, nie trzynaście.** Wiersz
`check_i18n.py:59` — „pigułki: `data-set-lang="([a-z]{2})"`" — **przestał
istnieć**: #50 zastąpił pigułki jednym `<select>`, `SWITCHER_LISTS` ma cztery
wpisy zamiast pięciu, a `data-set-lang` nie występuje już nigdzie na stronie.
Konsekwentnie w sekcji „Koszt odwrotu" jest **cztery listy przełącznika**, nie
pięć, a w „Decyzji" zostaje sam `<option value="pt">Português (Brasil)</option>`
— **pigułki `PT` nie ma czym podpisać**.

Pozostałe odsyłacze po przenumerowaniu:

| Było | Jest |
|---|---|
| `i18n_lib.py:31` (`LOCALE_ORDER`) | `:34` |
| `i18n_lib.py:36` (`_OPEN`) | `:50` |
| `check_i18n.py:43` (`DEFAULT_LOCALES`) | `:61` |
| `check_i18n.py:57–61` (listy przełącznika) | `:83–86` (cztery) |
| `check_i18n.py:69` (`if loc in LOCALE_ORDER`) | `:94` |
| `check_i18n.py:95` (walidacja `--locales`) | `:126` |
| `build_pdf.py:27` (`LOCALES`) | `:42` |
| `index.html:1474` (`langSpan`) | `:1492` |
| `index.html:109–116` (osiem reguł CSS) | `:110–126` (siedemnaście) |
| `index.html:798–805` (pigułki) | usunięte |
| `index.html:811–818` (`<option>`) | `:819–836` |
| `index.html:1622–1661` (`HEAD_TEXT`) | `:1651–1737` |
| `index.html:1682` (`HEAD_TEXT[cur] \|\| HEAD_TEXT.pl`) | `:1754` |

Bez zmian: `i18n_lib.py` `_OPEN` nadal ma flagę `re.I`, `HEAD_TEXT` nadal ma
klucze bez cudzysłowów, a `i18n_inject.py:33` nadal skleja nazwę pliku z
argumentu. Pułapki 1–5 obowiązują w całości.

**Puste dymki szyny to dziś 15 z 17 locale, nie 6 z 8.** `index.html:1492`
buduje je nadal tylko z `langSpan('pl', …)` / `langSpan('en', …)`, przy 20
kropkach szyny. Każdy kolejny locale powiększa tę dziurę o jeden; naprawa wymaga
nowej treści do przetłumaczenia, nie zmiany w tych plikach.
