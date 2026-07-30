# ADR 0001: Automatyczna aktualizacja screenshotów manuala (Patrol + pipeline)

Data: 2026-07-30 · Status: zaakceptowany

## Kontekst

`docs/manual/app-manual.{pl,en}.md` używa ~120 wspólnych screenshotów z
`docs/manual/pictures/`, robionych dziś ręcznie. UI aplikacji zmienia się
szybciej niż obrazki. Potrzebny powtarzalny, selektywny (nie zawsze całość)
mechanizm odświeżania na żądanie.

## Decyzja

Screenshoty produkuje **suite Patrol** w `apisense-mobile`
(`integration_test/screenshots/`, osobno od e2e), uruchamiany na emulatorze
Android przeciw **QA** z istniejącym kontem testowym. Do `apisense-docs`
trafiają przez **pipeline** (`screenshots.yml`, workflow_dispatch) wzorowany na
`auto_docs.yml`: capture → postprocess → copy-if-changed → PR z visual diffem.
Merge = auto-deploy Pages.

## Rozważone alternatywy

| Opcja | Werdykt | Powód |
|---|---|---|
| Playwright po drzewie semantics (Flutter web) | odrzucona | CanvasKit bez DOM; semantics dziurawe; dwa źródła prawdy |
| Agent AI (Claude in Chrome) wg manifestu | odrzucona jako trwały mechanizm | godziny/tokeny na pełny przebieg, szum w diffach, brak CI; była kandydatem v1 dopóki nie odkryliśmy istniejącej infry Patrol |
| Skill Claude do synchronizacji między repo | odrzucona | sync jest w pełni deterministyczny — skill dodaje tylko niedeterminizm; `gh workflow run` wystarcza |
| Flutter web jako źródło UI | odrzucona | Patrol nie wspiera web; emulator daje ekrany 1:1 ze stylem obecnych obrazków |
| Konto demo na PROD | odrzucona | QA ma gotowe konto, sekrety i fixtures (`qa.dart`); zero nowej infry |

## Decision log

1. **Zakres**: ~120 obrazków manuala Apisense Pro AI; jeden wspólny zestaw dla PL i EN.
2. **Locale UI: EN** (zmiana — obecny zestaw jest PL; pierwszy pełny przebieg wymienia całość).
3. **Trigger ręczny**: `make screenshots TARGET=<sekcja>` lokalnie lub `gh workflow run screenshots.yml -f sections=<sekcje>`; selektywność per sekcja manuala (per plik testowy), pojedynczy ekran przez `--dart-define=SHOTS_FILTER=<nazwa>`.
4. **Ekrany tworzenia bez submitu**: formularze wypełniane i anulowane — zero mutacji danych, cleanup niepotrzebny; stany "po zapisie" siedzą na stałe w seedzie QA.
5. **Środowisko QA**, konto z `E2E_TEST_EMAIL/PASSWORD`; dane seed do doszlifowania, by wyglądały realistycznie.
6. **`SCREENSHOT_MODE=true`** (dart-define) chowa QA-only debug UI (sekcja w `account_settings_screen.dart:276`); ribbon "QA" już nie istnieje (usunięty PR #293, 2026-07-24).
7. **Deterministyczny kadr**: stały profil emulatora, status bar w demo mode (9:30, pełna bateria), `pumpAndSettle`, bez focusa w polach.
8. **Postprocess wg manifestu**: `frame: phone` dostaje ramkę telefonu; hash-compare przed kopiowaniem — do gita trafiają tylko realnie zmienione piksele.
9. **Manifest** `integration_test/screenshots/manifest.yaml` w apisense-mobile — jedno źródło prawdy (czytane przez testy Dart i skrypty pipeline); klucz = nazwa pliku w `docs/manual/pictures/`.
10. **Wyjście: PR do apisense-docs** (PAT `DOCS_REPO_TOKEN`, `peter-evans/create-pull-request`) — human review przed publikacją.

## Konsekwencje

- Utrzymanie flow w Darcie spada na zespół mobile — zmiana UI wysypuje test widocznie, poprawka w tej samej codebase.
- Manual PL pokazuje angielskie UI (świadomy kompromis za jeden zestaw).
- Plany implementacyjne: `apisense-mobile/screenshot-suite.md` i
  `apisense-mobile/screenshot-sync-pipeline.md`.
