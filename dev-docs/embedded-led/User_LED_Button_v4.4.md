# Button and LED behaviour — user manual input (hardware v4.3 / v4.4)

Describes what the user sees and does on PWR board **v4.3 / v4.4**, the
revisions with the two-colour LED in the button. Newer hardware (v4.6) has a
five-LED bar and is documented separately in `LED_indication.md`.

The button carries two LEDs the user can see: **BLUE** and **RED**.

## Button and LED reference

| Action | LED behaviour | What happens | Comment |
| :--- | :--- | :--- | :--- |
| Device cold start | BLUE blinks 3 times, then RED blinks once | The device starts up | Same sequence after every reset and after leaving ship mode (device fully switched off) |
| Press the button, shorter than 3 s | BLUE blinks once | The device wakes up | — |
| Press the button, 3 to 10 s | The cold start sequence: BLUE 3 times, then RED once | The device restarts | The LEDs show the restart only once the device comes back up |
| Press the button, longer than 10 s | BLUE blinks 3 times, slowly | No action | Reserved for future use |
| Connect a USB charger | BLUE blinks 2 times | The device wakes up and starts charging | — |
| The built-in solar panel starts charging | BLUE blinks 3 times | The device wakes up and starts charging | Happens on its own once there is enough light — nothing to connect |
| Connect an external 12 V charger | BLUE blinks 4 times | The device wakes up and starts charging | — |

## Notes for the manual

- The press is evaluated **when the button is released**, except for the
  press longer than 10 s, which is recognised while the button is still held.
- Presses shorter than about 30 ms are ignored, so a light touch does
  nothing.
- There is **no battery level and no error indication** on this hardware.
  The LEDs only confirm the actions listed above.
- The LEDs stay off at all other times, including while the device sleeps.
