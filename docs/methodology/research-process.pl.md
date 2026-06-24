# Jak powstają nasze modele

Każdy model wykrywający chorobę przechodzi u nas **tę samą drogę** — od pierwszego pomysłu, przez badania w laboratorium, aż po wdrożenie w pasiekach na całym świecie. Dzięki temu, zanim alert trafi do Twojej aplikacji, dany model został wielokrotnie sprawdzony.

Na tej stronie pokazujemy ten proces krok po kroku. Jeśli szukasz wyjaśnienia, **jak działa samo wykrywanie** i co oznaczają poziomy zakażenia, zajrzyj na stronę [Jak działa wykrywanie chorób](disease-detection.md).

______________________________________________________________________

## Od pomysłu do wdrożenia

<p style="text-align:center;">
  <img src="../pictures/rd-lifecycle-pl.svg" alt="Cykl powstawania modeli Apisense: pomysł, faza laboratoryjna, pasieki eksperymentalne, wdrożenie z ciągłym re-treningiem" style="width:100%;max-width:780px;">
</p>

### 1. Pomysł i koncepcja

Wszystko zaczyna się od pytania **„co jeszcze warto monitorować?”**. Pomysły czerpiemy z:

- rozmów z pszczelarzami i ich codziennych problemów,
- przeglądu literatury naukowej,
- najnowszych doniesień i ciekawostek z branży.

Na tym etapie wybieramy zagrożenie, które realnie da się wykryć na podstawie zmian w powietrzu i mikroklimacie ula.

### 2. Faza laboratoryjna

Wybrany pomysł sprawdzamy w kontrolowanych warunkach. Pszczoły umieszczamy w **klateczkach laboratoryjnych razem z czujnikami**, tworząc:

- **grupy zarażone** — z kontrolowanym, zmierzonym poziomem choroby,
- **grupy kontrolne** — zdrowe, dla porównania.

Poziom zakażenia oznaczamy **badaniami laboratoryjnymi** (np. liczenie spor, flotacja), a następnie sprawdzamy, **czy odczyty czujników faktycznie odpowiadają wynikom z laboratorium**. Jeśli widać wyraźny związek, budujemy **pierwsze modele** i oceniamy, jak dobrze rozpoznają chorobę.

### 3. Pasieki eksperymentalne

Jeśli wyniki w laboratorium są obiecujące, **przenosimy eksperyment na większą skalę** — do pasiek działających w warunkach zbliżonych do rzeczywistych, pod stałą opieką pszczelarzy i naukowców.

Dane z tych pasiek są dużo bogatsze i bardziej zróżnicowane niż laboratoryjne (pogoda, pożytki, różne rodziny), dlatego **douczamy (re-trenujemy) modele** na tej większej próbce i ponownie sprawdzamy ich skuteczność.

### 4. Wdrożenie i ciągły re-trening

Gdy model utrzymuje skuteczność również w pasiekach eksperymentalnych, zwykle **na kolejny sezon wdrażamy go i udostępniamy globalnie** wszystkim użytkownikom.

Na tym jednak nie kończymy. Dane, które trafiają do aplikacji — **Twoje notatki, przeglądy i wyniki badań** — stają się naszymi nowymi oznaczeniami. Na ich podstawie **nieustannie douczamy modele**, dzięki czemu z każdym sezonem stają się dokładniejsze.

!!! tip "Dlaczego Twoje wpisy mają znaczenie"
    Każdy zaraportowany wynik flotacji, mikroskopii czy przeglądu pomaga uczyć modele. Im więcej rzetelnych oznaczeń od pszczelarzy, tym lepiej system rozpoznaje choroby — także w Twojej pasiece.

______________________________________________________________________

## Zgnilec amerykański — przypadek szczególny { #zgnilec-wyjatek }

Jedna choroba wymyka się powyższemu schematowi: **zgnilec amerykański (AFB)**. Jest to choroba **zwalczana z urzędu**, więc — w przeciwieństwie do warrozy czy nosemozy — **nie możemy jej wywołać ani „wyhodować” w pasiece** na potrzeby badań.

Dlatego dane o zgnilcu zbieraliśmy inaczej:

- czujniki w ulach zakładali **zaprzyjaźnieni pszczelarze i weterynarze**, gdy mieli **uzasadnione podejrzenie** wystąpienia zgnilca,
- dane rejestrowaliśmy, **czekając na potwierdzenie laboratoryjne**,
- po potwierdzeniu choroby **sprzęt był utylizowany**, zgodnie z zasadami bezpieczeństwa biologicznego.

Dzięki tej współpracy mogliśmy nauczyć model rozpoznawać sygnały zgnilca, nie narażając przy tym żadnej zdrowej rodziny.

______________________________________________________________________

## Zobacz też

- [Jak działa wykrywanie chorób](disease-detection.md) — co mierzy czujnik i co oznaczają poziomy zakażenia.
- [Procedury badań](../procedures/index.md) — jak wykonać i zaraportować badania, które zasilają nasze modele.
