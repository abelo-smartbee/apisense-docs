# Zrzuty ekranu instrukcji montażu

Źródło paneli dla `tools/svg_build_panels.py`. Jeden katalog na locale:

```
shots/en/apiary_beehives.png
shots/de/apiary_beehives.png
```

Generator szuka zrzutu w trzech miejscach, w tej kolejności:

1. `shots/<locale>/` — zrzut w języku, dla którego budujemy,
2. `shots/en/` — fallback,
3. `docs/manual/pictures/` — wspólne źródło suite'u, dopóki jest jednojęzyczne.

Dzięki temu figura zbuduje się dla każdego locale od pierwszego dnia i poprawia
się w miarę, jak `shots/<locale>/` się zapełnia (issue #81). Generator wypisuje
na końcu, których zrzutów **nie** znalazł w danym locale — wariant złożony
w całości z fallbacku nie ma prawa wyglądać jak gotowe tłumaczenie.

Nazwy plików są wspólne dla wszystkich locale i muszą się zgadzać z tablicą
`FIGURES` w generatorze. Zrzut może mieć wklejoną obudowę telefonu albo nie —
`unframed()` to mierzy i przycina, bo suite jest pod tym względem niespójny.

Po zbudowaniu wariantu (`--locale de`) dopisz locale do `FIG_LOCALES`
w `docs/assembly/index.html`; dopiero wtedy przełącznik zacznie go podawać.
