# Device signals

Reference page: **what I see on the device → what it means → what to do**.

If you're looking for a solution to a specific problem (e.g. "device not reporting"), start with [Troubleshooting](troubleshooting.md). This page helps interpret the signals themselves — LED, button, startup sequence — regardless of whether something is broken.

!!! note "Page status"
    Page in progress, to be filled in by the embedded team. Sections marked **TODO** need to be completed based on current firmware. If a given device does not have a particular signal (e.g. no buzzer), state that explicitly instead of skipping the section.

---

## Apisense Hub

### LED

!!! todo "TODO (embedded)"
    Fill in all LED states based on Hub firmware. Each row = one distinguishable pattern (color + blink sequence). If the LED is multi-color — list every combination. If a signal requires context (e.g. "only during boot") — note it in the *Context* column.

| What I see | Context | What it means | What to do |
|---|---|---|---|
| _e.g. green LED solid_ | _after pressing Power_ | _Hub running, connectivity OK_ | _nothing — normal state_ |
| TODO | TODO | TODO | TODO |

### Power button

!!! todo "TODO (embedded)"
    List every recognized button action. Cover: short press, long press (how many seconds), double press, combinations (e.g. holding while inserting power = factory reset?). If an action does not exist — state it explicitly.

| User action | Effect | Signal |
|---|---|---|
| _short press (<1s)_ | _wake / status check_ | _LED blinks green once_ |
| TODO | TODO | TODO |

### Startup sequence

!!! todo "TODO (embedded)"
    Describe what the user sees 0–60s after pressing Power or connecting power. Step by step: when the LED turns on, when it goes off, when the Hub is ready. Provide approximate timings.

### Charging

!!! todo "TODO (embedded)"
    How to recognize that the Hub is gaining energy (solar panel / USB-C / additional PV panel)? Does the LED show this, or only the app? How to distinguish "charging" vs "fully charged" vs "not charging despite a connected source"?

### Low battery

!!! todo "TODO (embedded)"
    Threshold for triggering the warning (e.g. <20%). How it's signaled locally (LED). What the Hub does at very low battery (sleep / shutdown).

### No LTE connectivity

!!! todo "TODO (embedded)"
    Does the LED distinguish: no SIM / no network registration / no signal / server unreachable? Is there any local signal at all, or only visible in the app?

### No BLE connectivity

!!! todo "TODO (embedded)"
    Signal when no Sensor/Scale connects to the Hub. Versus partial signal (some devices OK, some not).

### Factory reset

!!! todo "TODO (embedded)"
    Trigger procedure (button combination / hold time). What the user sees that confirms the reset went through. What exactly is wiped (network config, BLE pairings, certificates?).

### Critical error state

!!! todo "TODO (embedded)"
    Does the firmware have a "panic" / "cannot continue" state? How signaled. What the user should do (RMA, reset, contact support).

---

## Apisense VitalSensor

### LED

!!! todo "TODO (embedded)"
    All LED states for the VitalSensor. The [Configuration manual](index.md#3-first-start-up) only says *"the indicator LED should light up"* — expand: what color, how many seconds, blinking or solid.

| What I see | Context | What it means | What to do |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

### Button

!!! todo "TODO (embedded)"
    Does the VitalSensor have any user-accessible button at all? If not — state explicitly. If yes — list actions.

### Battery insertion sequence

!!! todo "TODO (embedded)"
    What the user sees 0–30s after inserting 2× AA. When the LED turns on, how long, when it goes off. When the VitalSensor starts looking for the Hub.

### Low battery

!!! todo "TODO (embedded)"
    Warning threshold, LED signal, when the device stops sending data.

### Pairing / discovery with the Hub

!!! todo "TODO (embedded)"
    How does the user know the VitalSensor is searching for the Hub? How long does first discovery take? Is the LED different when found vs when searching?

### No BLE range

!!! todo "TODO (embedded)"
    Local signal when the Hub is out of range / shielded. Whether the Sensor retries periodically and how that's visible.

### Reset

!!! todo "TODO (embedded)"
    Is there a user-accessible reset (e.g. removing batteries for 10s — this is described in `troubleshooting.md`)? Is there a full factory reset?

### Sensor fault

!!! todo "TODO (embedded)"
    Does the firmware distinguish a failure of a specific sensor (NOx, VOC, RH, T, microphone)? Is there a local signal, or only telemetry?

---

## Apisense Scale

### LED

!!! todo "TODO (embedded)"
    All LED states for the Scale. The [Configuration manual](index.md#3-first-start-up) mentions the LED lighting up at startup — expand as for Hub/VitalSensor.

| What I see | Context | What it means | What to do |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

### Button

!!! todo "TODO (embedded)"
    Does the Scale have any user-accessible button? If not — state explicitly.

### Battery insertion sequence

!!! todo "TODO (embedded)"
    What the user sees after inserting 2× AA, before closing the battery compartment. How long the LED stays on. When the Scale starts looking for the Hub and performs the first measurement.

### Calibration

!!! todo "TODO (embedded)"
    Does the Scale perform any auto-calibration at startup (load cell zeroing)? How does the user know it's running? Is there a user-triggered calibration? If not — state explicitly.

### Low battery

!!! todo "TODO (embedded)"
    Threshold, signal, behavior. The Scale has a 36-month battery life claim — also include roughly when the warning will appear before end of life.

### No BLE range

!!! todo "TODO (embedded)"
    Local signal when the Hub is out of range.

### Reset

!!! todo "TODO (embedded)"
    Procedure, signal, scope (does it wipe calibration?).

### Error state

!!! todo "TODO (embedded)"
    Does the firmware signal a load cell fault (e.g. damaged, disconnected, overloaded)? Local signal or only telemetry.

---

## Page conventions

To keep the page readable while it's being filled in:

- **One "What I see" cell = one distinguishable state.** Don't merge multiple patterns into a single row.
- **Non-technical language.** Not "code E001" — instead "the LED blinked yellow three times".
- **No firmware jargon.** A user does not know what a "watchdog reset" is — write "the device restarted itself".
- **If something does not exist — state it explicitly** (e.g. "the VitalSensor has no external button"). Absence of a feature is information.
- **Update on firmware changes.** Any change to signaling in firmware → PR to this page in the same sprint.
