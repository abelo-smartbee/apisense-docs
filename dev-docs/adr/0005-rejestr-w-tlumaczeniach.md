# ADR 0005: Rejestr (formalny / nieformalny) w tłumaczeniach instrukcji montażu

Data: 2026-07-31 · Status: zaakceptowany

## Kontekst

Epik #47 dołożył `docs/assembly/index.html` dziewięć locale (#53–#61). Każde
tłumaczenie powstawało w osobnej gałęzi, bez wglądu w pozostałe, na podstawie
polskiego oryginału. Polski oryginał jest **nieformalny** („Zeskanuj kod QR
Huba", „Na ekranie głównym otwórz swoją pasiekę").

Po scaleniu widać, że dziewiątka rozeszła się na dwie grupy:

| Rejestr | Locale z tej partii |
|---|---|
| formalny (V) | `cs`, `hr`, `ro` |
| nieformalny (T) | `sk`, `hu`, `nl` |
| brak żywego rozróżnienia w tym gatunku | `fi`, `sv`, `da` |

`fi`, `sv` i `da` nie są wyborem: skandynawska reforma „du" i fińska praktyka
instrukcji technicznych nie zostawiają w tym gatunku formy grzecznościowej, więc
tłumacz nie miał czego wybierać. Realny rozjazd to **`cs`/`hr`/`ro` przeciw
`sk`/`hu`/`nl`**, a najbardziej rzuca się w oczy przy parze `cs`/`sk` — językach
najbliższych sobie w całej partii, które poszły w przeciwne strony:

```
EN  Tap Add beehive.
cs  Klepněte na Add beehive.      ← V
sk  Stlač Add beehive.            ← T
```

Kluczowa obserwacja jest jednak taka, że **ten rozjazd nie jest nowy i nie
przyszedł z tą gałęzią**. Osiem locale wydanych wcześniej (#37–#40) dzieli się
dokładnie tak samo:

| Rejestr | Locale wydane wcześniej |
|---|---|
| formalny (V) | `fr` („Ouvrez votre rucher", „Appuyez sur"), `tr` („arılığınızı açın", „dokunun") |
| nieformalny (T) | `de` („Öffne deinen Bienenstand", „Tippe auf"), `es` („Abre tu colmenar", „Pulsa"), `it` („apri il tuo apiario", „Tocca") |
| brak rozróżnienia | `no` |

Czyli nie stoimy przed pytaniem „czy wprowadzić niespójność", tylko przed
pytaniem „czy zerwać z normą, która jest w produkcji od #37". Bilans po
scaleniu: **5 locale formalnych (`fr` `tr` `cs` `hr` `ro`) i 6 nieformalnych
(`de` `es` `it` `nl` `sk` `hu`)** wśród jedenastu języków z żywym T/V.

## Decyzja

**Rejestr wybiera język docelowy, nie dom.** Tłumaczenie idzie w rejestrze,
w jakim dany język pisze konsumenckie instrukcje sprzętu i aplikacji — nawet
jeśli różni się od rejestru polskiego oryginału i od rejestru sąsiedniego
języka. Dziewięć tłumaczeń z #53–#61 wchodzi **bez zmian**.

Trzy powody, w kolejności wagi:

1. **Czytelnik nigdy nie widzi dwóch języków naraz.** Reguła
   `[data-lang="xx"] [lang]:not([lang="xx"])` pokazuje dokładnie jeden locale.
   Niespójność między `cs` a `sk` jest widoczna w diffie i w tabelce takiej jak
   powyższa — nie jest widoczna w produkcie. Koszt ponosi recenzent, nie
   pszczelarz.
2. **Cena wyrównania jest asymetryczna.** Wymuszenie „wszędzie T" każe czeskiej
   i rumuńskiej instrukcji sprzętu brzmieć poufale wbrew konwencji gatunku;
   wymuszenie „wszędzie V" robi to samo niemieckiej i hiszpańskiej — a te dwie
   **są już wydane** i musiałyby zostać przetłumaczone od nowa. Nie ma wariantu
   wyrównania, który nie każe co najmniej jednemu językowi czytać się źle.
3. **To jest istniejąca norma, tylko nigdy niezapisana.** `fr` i `tr` są
   formalne w produkcji od #37–#40 obok nieformalnych `de`/`es`/`it`. Dziewiątka
   nie wprowadziła nowej zasady, tylko powtórzyła starą — dziewięć razy, każdy
   agent osobno, i za każdym razem wyszła ta sama.

Decyzja jest podjęta świadomie i zapisana tutaj **właśnie po to**, żeby nie
czytała się jak dziewięciu tłumaczy, którzy przypadkiem się nie dogadali.

## Konsekwencje

- **Każdy kolejny locale** rozstrzyga rejestr według normy swojego języka i
  odnotowuje wybór w opisie PR-a. Domyślną odpowiedzią na „a dlaczego tu inaczej
  niż w sąsiednim języku" jest ten ADR.
- **Wewnątrz jednego locale rejestr musi być jednolity.** Ta decyzja zwalnia z
  spójności między językami, nie w obrębie języka — mieszanie T i V w jednej
  instrukcji to zwykły błąd i łapie się je w review tłumaczenia.
- Nic tego nie waliduje maszynowo i nie ma sensownego sposobu, żeby to zrobić:
  `check_i18n.py` liczy obecność spanów, nie ich ton. Rejestr zostaje pozycją
  ludzkiego review.
- Gdyby marketing kiedyś zażądał jednego rejestru w całej rodzinie językowej, to
  **nie jest przełącznik w konfiguracji, tylko ponowne tłumaczenie** jedenastu
  locale z żywym T/V, w tym pięciu już wydanych. Warunkiem uznania tej decyzji
  za złą jest taka decyzja marki — nie samo zauważenie rozjazdu w diffie.
- `pl` (oryginał) i `en` zostają nieformalne; `fi`, `sv`, `da`, `no` nie mają w
  tym gatunku wyboru i nie należy im go dorabiać.
