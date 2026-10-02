# Button and LED behaviour — user manual input (Scale Ver < V4.2 and Vital Ver < 4.2)

## LED reference (device states)

| Device state | LED behaviour | What happens | Comment |
| :--- | :--- | :--- | :--- |
| Start-up (Main task starts) | OFF (dark) | The device boots and enters the Service state | After it, the LED follows the Service state below |
| Service | Fast blinking, 5 Hz (toggle every 100 ms) | Full advertising, CLI/service commands available | Lasts 15 s if no client sends a login/CLI command, otherwise up to 300 s. Then the device goes to Connection-ready. On leaving Service the LED is left OFF (dark) |
| Advertising | Blinking, 1 Hz (toggle every 500 ms) | Full BLE advertising, device can be found and connected | Lasts up to 120 s or until a connection is made, then the device goes to Sleep |
| Connection-ready | LED keeps the state it had before (no change) | Normal (slower) advertising, waiting for a client command | Lasts up to 300 s, or ends earlier when a command was received and the client disconnected. Then the device goes to Sleep |
| Sleep | OFF (dark) | Advertising off, measurements are made by the device tasks | Default 600 s, then back to Connection-ready. The LED stays dark in this state |
| OTA wait | OFF (dark) | Waiting for firmware update to continue | Same wait time as Sleep, then back to Connection-ready |

## Button reference

### **IMPORTANT NOTE: The boards in production does not came with presoldered button**

The press length is measured from press to release and evaluated **when the
button is released**.

| Action (press length) | LED behaviour | What happens | Sensor variant |
| :--- | :--- | :--- | :--- |
| Shorter than 0.1 s | None | Ignored (debounce) | Both |
| 0.1 s to 2 s ("short") | Advertising blink starts (1 Hz) | Device goes to Advertising and forces a new measurement | Both |
| 2 s to 5 s | None | No action (code for a mode change is disabled) | Both |
| 5 s to 10 s | **Scale:** LED lights up, goes dark 4 times briefly (100 ms dark / 100 ms lit), then goes OFF (dark) | Scale is **tared** (both channels: zero point set) | Scale |
| 5 s to 10 s | None | BME sensor settings are reset to default (`Hive_setDefaultBME`) | Hive |
| 10 s to 20 s | Service blink starts (5 Hz) | Device goes to Service state | Both |
| Longer than 20 s | None | All BLE bondings (paired clients) are deleted | Both |

## Notes for the manual

- Press lengths are approximate; the button is checked by the button task
  every 500 ms, so the reaction can be delayed by up to about 0.5 s.
- Hold the scale button for 5–10 s only with an **empty platform** — the
  tare takes the current load as zero. The LED lighting up, showing 4 quick dark gaps and going out confirms the tare.
- There is **no battery level and no error indication** on the LED. Errors
  (for example bootloader CRC or soft-watchdog errors) are reported via the
  BLE message flags, not via the LED.
- If the device stays without a BLE connection for 12 h (soft watchdog) it
  returns by itself to the Advertising state (LED 1 Hz blink).
- The LED is dark during Sleep, so a dark LED means the device is running
  normally and waiting for the next measurement cycle.
- In the firmware source the Sleep state calls "LED on", but on the hardware
  this shows as a dark LED (physical polarity is inverted relative to the
  firmware naming). This manual describes what the user sees.

## Sequence overview

```
power up -> Service (5 Hz blink, 15-300 s) -> Connection-ready (LED dark, <=300 s)
         -> Sleep (LED dark, 600 s) -> Connection-ready -> Sleep -> ...

short press (0.1-2 s)  -> Advertising (1 Hz blink, <=120 s) -> Sleep
long press (10-20 s)   -> Service (5 Hz blink)
```
