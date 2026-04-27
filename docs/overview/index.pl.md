# Apisense – Tłumaczymy język pszczół na zrozumiałe dane

**Kompleksowe rozwiązanie IoT dla nowoczesnego pszczelarstwa**

## 1. Wprowadzenie

Apisense to zaawansowany system wczesnego ostrzegania, łączący nowoczesne czujniki Internetu Rzeczy (IoT) z algorytmami sztucznej inteligencji (AI). System umożliwia prewencyjne wykrywanie chorób ze skutecznością do **95% F1-score**, analizując poziom feromonów pszczół miodnych oraz akustyczne wzorce aktywności w ulu.

## 2. Specyfikacja sprzętowa

### **Apisense Hub**

*Hub, który agreguje dane z czujników i wag w obrębie pasieki oraz przesyła je do chmury.*

- **Zasilanie:** Wbudowany akumulator Li-Ion + zintegrowany panel fotowoltaiczny (solarny).
- **Czas pracy:** Do 2 tygodni bez dostępu do światła słonecznego; ciągła praca przy ekspozycji słonecznej. Obsługa ładowania sieciowego (standardowe niskonapięciowe złącze).
- **Łączność:**
    - **Chmura:** LTE (globalna karta SIM, w komplecie roczny pakiet transferu danych).
    - **Lokalnie:** Bluetooth Low Energy (BLE) – zasięg do 35 m do czujników i wag. Obsługa do 100 urządzeń.
- **Montaż:** Nieinwazyjny (słupek, drzewo), odporność na warunki atmosferyczne (IP65). Optymalny kąt nachylenia panelu: 20° do 50°.
- **Wymiary:** Kompaktowa obudowa zintegrowana z panelem solarnym (ok. 17,5 × 17,5 × 5 cm).

### **Apisense VitalSensor**

*Kluczowe urządzenie do wczesnej identyfikacji chorób — w sposób ciągły zbiera parametry środowiskowe z wnętrza ula, które zasilają modele detekcyjne AI.*

- **Czujniki:** NOx, VOC, wilgotność, temperatura, rezystancja gazowa, mikrofon akustyczny oraz dodatkowe parametry środowiskowe wewnątrz ula.
- **Zasilanie:** 2× baterie AA.
- **Żywotność baterii:** Do 12 miesięcy na jednym komplecie baterii.
- **Montaż:** Nieinwazyjny uchwyt na ramkę pszczelą (nie wymaga modyfikacji ula).
- **Wymiary:** Ultracienka konstrukcja mieszcząca się w przestrzeni międzyramkowej (ok. 13 × 3 × 2 cm).

### **Apisense Scale**

*Precyzyjny monitoring przybytku miodu i kondycji rodziny pszczelej.*

- **Czujniki:** Tensometr do pomiaru masy ula oraz wbudowany czujnik temperatury do odczytu temperatury otoczenia (na zewnątrz ula).
- **Zasilanie:** 2× baterie AA.
- **Żywotność baterii:** Do 36 miesięcy (3 lata) na jednym komplecie baterii.
- **Montaż:** Niski profil pod ulem; w zestawie drewniana belka poziomująca dla stabilności.
- **Wymiary:** Standardowa szerokość dopasowana do denek ula (ok. 40 × 5 × 4 cm).

## 3. Ekosystem cyfrowy (software)

- **Aplikacja mobilna:** Apisense Pro AI (iOS/Android/Web) – nowoczesny, responsywny interfejs z zaawansowaną analizą trendów i historycznymi danymi.
- **Sztuczna inteligencja:** Silnik AI analizuje dane, dostarczając praktyczne rekomendacje i alarmy (m.in. identyfikacja chorób: warrozy, nosemy, zgnilca).
- **Rekomendacje działań:** W oparciu o wszystkie dostępne systemowi dane wejściowe — notatki pszczelarza, przeglądy, zdjęcia, odczyty z czujników i wag, prognozy pogody oraz wiedzę ekspercką — Apisense generuje konkretne rekomendacje działań, które pomagają pszczelarzowi wzmocnić rodzinę pszczelą.
- **Powiadomienia:** System powiadomień push w czasie rzeczywistym o krytycznych zdarzeniach (np. nagły spadek masy, gwałtowny spadek temperatury, gwałtowny wzrost wilgotności).

## 4. Kluczowe korzyści

1. **100% bezprzewodowy:** Brak okablowania drastycznie obniża koszty instalacji i ryzyko uszkodzeń związanych z pogodą.
2. **Plug & Play:** Rejestracja urządzeń poprzez szybkie zeskanowanie kodu QR w aplikacji.
3. **Niska obsługa:** Standardowe baterie AA dostępne na całym świecie; solarny Hub eliminuje konieczność ręcznego ładowania.
4. **Trwałość:** Zaprojektowany do ekstremalnych warunków pasiecznych (wysoka wilgotność, zmienne temperatury).
5. **Precyzja:** Do 95% skuteczności w wczesnej identyfikacji chorób.

## 5. Apisense Pro AI – aplikacja

Aplikacja Apisense Pro AI zapewnia intuicyjny i nowoczesny interfejs do zarządzania pasiekami na iOS, Androidzie i w przeglądarce.

**Pobierz aplikację:** 
- [App Store](https://apps.apple.com/app/apisense/id6741760755)
- [Google Play](https://play.google.com/store/apps/details?id=ai.apisense)
- [Wersja webowa](https://app.apisense.ai/)

<div class="app-screenshots" markdown>

![Apisense Pro AI – ekran 1](pictures/2026_0276_Apisense_Grafika_1242x2688_Aplikacja_1_Ver.04.jpg)
![Apisense Pro AI – ekran 2](pictures/2026_0276_Apisense_Grafika_1242x2688_Aplikacja_2_Ver.04.jpg)
![Apisense Pro AI – ekran 3](pictures/2026_0276_Apisense_Grafika_1242x2688_Aplikacja_3_Ver.04.jpg)
![Apisense Pro AI – ekran 4](pictures/2026_0276_Apisense_Grafika_1242x2688_Aplikacja_4_Ver.04.jpg)
![Apisense Pro AI – ekran 5](pictures/2026_0276_Apisense_Grafika_1242x2688_Aplikacja_5_Ver.04.jpg)
![Apisense Pro AI – ekran 6](pictures/2026_0276_Apisense_Grafika_1242x2688_Aplikacja_6_Ver.04.jpg)

</div>

### Kluczowe funkcje aplikacji

- **Alerty w czasie rzeczywistym:** Powiadomienia push o ryzyku rojenia się oraz gwałtownych zmianach pogody.
- **Inteligentne rekomendacje:** Proaktywne porady generowane przez AI w celu optymalizacji zdrowia uli.
- **Zarządzanie pasiekami:** Organizacja wielu lokalizacji i setek uli w ramach jednego dashboardu.
- **Dostęp wielu użytkowników:** Udostępniaj dane zespołowi lub badaczom, zachowując pełną kontrolę właścicielską.

Pełne omówienie pracy w aplikacji — rejestracja, zarządzanie pasiekami i ulami, przeglądy, notatki, zadania, alarmy oraz udostępnianie pasiek — znajdziesz w [Instrukcji aplikacji](../manual/app-manual.md).
