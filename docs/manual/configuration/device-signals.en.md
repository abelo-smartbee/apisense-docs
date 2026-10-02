# Device signals

Reference page: **what I see on the device → what it means → what to do**.

If you're looking for a solution to a specific problem (e.g. "device not reporting"), start with [Troubleshooting](troubleshooting.md). This page helps interpret the signals themselves — LED, button, startup sequence — regardless of whether something is broken.

!!! info "The LEDs only confirm actions"
    None of the devices shows battery level or errors on its LED.

---

## Apisense Hub

### LED

The Hub button holds two LEDs: **blue** and **red**. They only confirm the actions in the table. They stay off at all other times — also when the Hub works normally and sleeps between measurements.

| What I see | When | What it means | What to do |
|---|---|---|---|
| Blue blinks 3 times, then red blinks once | After the Hub starts or restarts | The Hub is starting up | Nothing — normal state |
| Blue blinks once | After a short press of the button (shorter than 3 s) | The Hub woke up | Nothing — normal state |
| Blue blinks 2 times | After you connect a USB charger | The Hub woke up and starts charging | Nothing — normal state |
| Blue blinks 3 times | On its own, when the panel gets enough light | The built-in solar panel starts charging | Nothing — there is nothing to connect |
| Blue blinks 4 times | After you connect an external 12 V charger | The Hub woke up and starts charging | Nothing — normal state |
| Blue blinks 3 times, slowly | While you hold the button longer than 10 s | No action | Nothing |
| LEDs are off | At all other times | The Hub works normally or sleeps | Nothing — normal state |

### Power button

The Hub reacts when you **release** the button. A very light touch is ignored.

| User action | Effect | Signal |
|---|---|---|
| Press shorter than 3 s | The Hub wakes up | Blue blinks once |
| Hold for 3 to 10 s | The Hub restarts | Startup sequence: blue 3 times, then red once. The LEDs light up only once the Hub comes back up |
| Hold longer than 10 s | No action | Blue blinks 3 times, slowly — while the button is still held |

### Startup sequence

After every start and every restart the Hub shows the same sequence: the blue LED blinks 3 times, then the red LED blinks once. Then the LEDs go off.

### Charging

The Hub confirms only the **start** of charging. The number of blue blinks tells you the power source:

- 2 blinks — USB charger,
- 3 blinks — built-in solar panel,
- 4 blinks — external 12 V charger.

The LED does not show that charging continues or that the battery is full.

### Low battery

The Hub does not signal a low battery on its LEDs.

### No LTE connectivity

The Hub does not signal a lost LTE connection on its LEDs.

### No BLE connectivity

The Hub does not signal a lost connection to a VitalSensor or Scale on its LEDs.

### Factory reset

The Hub has no factory reset function. Only a restart is available: hold the button for 3 to 10 s.

### Critical error state

The Hub does not signal errors on its LEDs.

---

## Apisense VitalSensor

### LED

The VitalSensor has one LED. You can see it through the housing.

| What I see | When | What it means | What to do |
|---|---|---|---|
| Fast blinking (about 5 times per second) | After you insert the batteries, usually for about 15 s | The VitalSensor started | Nothing — normal state |
| Slow blinking (about once per second), up to 2 minutes | After 12 hours without a connection to the Hub | The VitalSensor searches for a connection again | Nothing — the device does this on its own |
| LED is off | At all other times | The VitalSensor works normally and takes measurements | Nothing — normal state |

### Button

The VitalSensor has no button.

### Battery insertion sequence

After you insert 2× AA, the LED starts to blink fast. It usually blinks for about 15 s, then goes off. A dark LED means normal operation: the VitalSensor works and waits for the next measurement cycle.

### Low battery

The VitalSensor does not signal a low battery on its LED.

### Pairing / discovery with the Hub

The LED does not show whether the VitalSensor connected to the Hub.

### No BLE range

The LED does not show a lost connection as it happens. After 12 hours without a connection the VitalSensor searches again on its own — the LED then blinks slowly, for up to 2 minutes.

### Reset

The VitalSensor has no reset button.

### Sensor fault

The VitalSensor does not signal errors on its LED. Error information goes to the system together with the measurements.

---

## Apisense Scale

### LED

The Scale has one LED. The LED is **inside the black housing** — you must open the housing to see it.

| What I see | When | What it means | What to do |
|---|---|---|---|
| Fast blinking (about 5 times per second) | After you insert the batteries, usually for about 15 s | The Scale started | Nothing — normal state |
| Slow blinking (about once per second), up to 2 minutes | After 12 hours without a connection to the Hub | The Scale searches for a connection again | Nothing — the device does this on its own |
| LED is off | At all other times | The Scale works normally and takes measurements | Nothing — normal state |

### Button

The Scale has no button.

### Battery insertion sequence

After you insert 2× AA, before you close the housing, the LED starts to blink fast. It usually blinks for about 15 s, then goes off. A dark LED means normal operation: the Scale works and waits for the next measurement cycle.

### Calibration

The Scale has no button, so there is no tare on the device.

### Low battery

The Scale does not signal a low battery on its LED.

### No BLE range

The LED does not show a lost connection as it happens. After 12 hours without a connection the Scale searches again on its own — the LED then blinks slowly, for up to 2 minutes. You can see this only with the housing open.

### Reset

The Scale has no reset button.

### Error state

The Scale does not signal errors on its LED. Error information goes to the system together with the measurements.
