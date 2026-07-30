# ADR 0002: Wersjonowanie `tools/` (generatory i walidator i18n)

Data: 2026-07-30 · Status: zaakceptowany

## Kontekst

`.gitignore` wycinał cały katalog `tools/` — intencja była taka, żeby repo
dokumentacji trzymało treść, a nie narzędzia. W `tools/` mieszkały jednak
`build_standalone.py` i `build_pdf.py`, czyli jedyny sposób na wyprodukowanie
jednoplikowej instrukcji do wysyłki i PDF-ów montażu. Skutek: artefakty
odtwarzała wyłącznie osoba, która miała skrypty lokalnie, a ich zmiany nie
przechodziły przez review.

Epik #34 (parytet 8 języków instrukcji montażu) postawił sprawę na ostrzu noża:

- `check_i18n.py` (#35) pilnuje 1200 spanów w 150 grupach × 8 locale. Brak
  jednego spanu = pusta sekcja bez ostrzeżenia, bo CSS nie ma fallbacku.
  Walidator w niewersjonowanym katalogu nie może wejść do CI.
- Zmiana `LOCALES` w `build_pdf.py` (#41) była zmianą, której nie da się
  zreviewować, bo pliku nie ma w repo.
- Cztery tłumaczenia (#37–#40) szły równolegle po jednym 100 kB HTML-u.
  Rozdzielił je harness (`i18n_lib.py` / `i18n_extract.py` / `i18n_inject.py`)
  — kolejne trzy pliki, które muszą być wersjonowane, żeby wynik injekcji dało
  się odtworzyć i sprawdzić.

## Decyzja

**Wersjonujemy `tools/`.** `tools/` zdjęte z `.gitignore` (commit `a2e890f`).

Rozróżnienie, które utrzymujemy: **generator jest wersjonowany, jego wynik nie.**
Ignorowane pozostają:

- `docs/assembly/*_standalone.html` (~3,3 MB na przebudowę)
- `docs/assembly/pdf/` (8 × ~3,8 MB — w historii gita ~30 MB przy każdym buildzie)

Do repo wchodzą też dane wejściowe harnessu — `tools/i18n/*.json` (tłumaczenia)
oraz `tools/i18n/_source.json` (zrzut źródła). To treść, nie artefakt: `_source.json`
musi zgadzać się z HTML-em i jest sprawdzalny (`i18n_extract.py` + pusty `git diff`).

## Rozważone alternatywy

| Opcja | Werdykt | Powód |
|---|---|---|
| Zostawić `tools/` poza repo, PDF-y ręcznie i jednoosobowo | odrzucona | walidator poza CI, zmiany generatorów bez review, bus factor 1 przy 8 językach |
| Osobne repo na narzędzia | odrzucona | trzy skrypty sprzężone z jednym plikiem HTML w tym repo; podział dokłada synchronizację bez zysku |
| Wersjonować też artefakty (PDF-y) | odrzucona | ~30 MB binariów w historii przy każdym przebudowaniu; PDF-y publikujemy przez `docs/downloads/files/`, świadomie i pojedynczo |

## Konsekwencje

- `check_i18n.py` **może** wejść do CI obok `mkdocs build --strict`. Nie zrobiono
  tego w tym epiku: jedyny workflow (`deploy.yml`) chodzi na push do `main`, więc
  walidator bramkowałby deploy, a nie PR. Wpięcie to osobna decyzja — patrz #35.
- Zmiany w generatorach idą przez review jak reszta repo.
- Ktokolwiek może odtworzyć artefakty: `python3 tools/build_standalone.py`,
  potem `python3 tools/build_pdf.py`. Wymaga Chrome/Chromium, opcjonalnie `gs`.
- Skrypty zostają bez zależności zewnętrznych (sama stdlib) — `requirements.txt`
  dalej trzyma tylko `mkdocs-*`.
