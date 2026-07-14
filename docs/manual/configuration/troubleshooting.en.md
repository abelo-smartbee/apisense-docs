# Troubleshooting

## 1. Problem List and Suggested Solutions

| No. | Problem | Device | Suggested Solution |
| --- | ------- | ------ | ------------------ |
| 1 | Device inactive (never checked in) | VitalSensor | 1. Check battery installation. Remove and reinsert the battery, observing polarity. 2. Check that the battery is not depleted; replace if so. **Note:** after correct battery installation the LED should light up. 3. If the problem persists or wires are damaged, contact Apisense support. |
| 2 | Depleted / very low battery | VitalSensor | Replace the batteries, observing polarity. **Note:** after correct battery installation the LED should light up. After replacing the batteries you do not need to re-pair the device, change app settings, or reset the Hub — simply place the device within the Hub's range and wait for synchronisation (details: [FAQ — after battery replacement](../../faq/index.md#after-battery-replacement)). If the problem persists or wires are damaged, contact Apisense support. |
| 3 | No communication with Apisense Hub despite correct power supply (no BLE range) | VitalSensor | Move the VitalSensor closer to the Apisense Hub. Within 12 hours the VitalSensor should appear in the system. If the problem persists, contact Apisense support. |
| 4 | Weak BLE signal (below −90 dBm) | VitalSensor | Rotate the VitalSensor in the frame or the entire frame by 180° (LED in VitalSensor facing the Apisense Hub). Signal level should rise above −90 dBm. If the problem persists, consider relocating the Hub closer to the VitalSensor, taking care not to degrade range for other devices. Contact Apisense support if needed. |
| 5 | No communication with Apisense Hub (no BLE range) | Scale | Move the Scale closer to the Apisense Hub. Within 12 hours the device should appear in the dashboard. If the problem persists, contact Apisense support. |
| 6 | Weak BLE signal (below −90 dBm) | Scale | Ensure the Scale electronics face the Apisense Hub. Consider relocating the Apisense Hub closer to the Scale while maintaining range for other devices. Signal level should rise above −90 dBm. Contact Apisense support if needed. |
| 7 | LED does not light up after pressing the Power button | Hub | Check power supply — if the Hub is not receiving enough light, consider changing its position (tilt, height) or use external power. Allow the Hub to charge (approx. 3 hours), then press the Power button — the LED should light up and within 90 minutes the Hub should appear in the dashboard. If the Hub has not been charged for an extended period, see problem "No charging". |
| 8 | No charging | Hub | Check the connection of the solar panel to the Apisense Hub. Verify the panel position is correct (no shading, facing the sun, minimum 20° tilt). The dashboard should show the Hub charging. If the problem persists, contact Apisense support. |
| 8a | Hub charges slowly / discharges quickly / battery stuck at a low % on external power (DC adapter) | Hub | The most common cause is a voltage drop at the DC connector, not the adapter itself. Check that you use the correct DC plug (pin **2.1 mm**, outer diameter **5.5 mm**) and that it is pushed all the way in. Work through the checklist in [External power diagnostics (DC adapter)](#3-external-power-diagnostics-dc-adapter) below. If there is no improvement, contact Apisense support. |
| 9 | Frequent "Apiary inactive" status / no Hub coverage | Hub | Walk through the checklist in [Hub diagnostics — no coverage](#2-hub-diagnostics-no-coverage) below. If the issue persists, contact Apisense support. |
| 10 | Weak signal to devices (BLE below −90 dBm) | Hub | Rotate the Apisense Hub 90° on its vertical axis. After 12 hours check the signal level in the dashboard; repeat if needed. If the problem persists, consider relocating the Hub; check for obstacles (metal, power lines). Contact Apisense support if there is no improvement. |
| 11 | Other problems | — | Contact Apisense: **[bee@apisense.ai](mailto:bee@apisense.ai)**. |

## 2. Hub diagnostics — no coverage

If the Hub is not reporting data or shows the "Apiary inactive" status, work through the checklist below in order.

1. **Antennas tightened** — check that both antennas (BLE and LTE) are firmly screwed into the Hub sockets.
2. **Antennas pointing vertically upwards** — antennas must point straight up, never horizontally or downwards.
3. **Hub outdoors** — the device must not be under a roof or indoors (required for GPS and cellular coverage).
4. **No obstacles nearby** — check that there are no large metal objects or power lines next to the Hub.
5. **Solar panel** — facing the sun, tilted at least 20°, with no shading. The app should show the Hub charging.
6. **Cellular coverage at the location** — verify with a phone on-site that LTE/GSM signal is available. Without coverage the Hub cannot transmit data.

If the issue persists after the checklist, email us at **[bee@apisense.ai](mailto:bee@apisense.ai)** and **attach a photo of the Hub installation site** (showing surroundings, solar panel, antennas) — it speeds up diagnosis.

## 3. External power diagnostics (DC adapter)

If the Hub is powered by an external DC adapter but still charges slowly, discharges quickly, or its battery stays at a low level, the most common cause is a **voltage drop at the DC connector**, not the adapter itself. Work through the checklist below in order.

1. **Measure the voltage at the Hub input** — measure the voltage at the plug inserted into the Hub, not at the adapter. A 12 V adapter reading about 12.3 V is correct; the problem is when the voltage at the Hub input is noticeably lower (e.g. around 11 V) — this indicates a drop at the connector.
2. **Plug pin diameter** — the Hub requires a DC plug with a **2.1 mm** pin (**5.5 mm** outer diameter). A **2.5 mm** plug does not make proper contact and is a frequent cause of this symptom.
3. **Plug housing diameter** — the black plastic housing of the plug should be **at most 9 mm** in diameter. A thicker housing will not seat fully in the Hub's socket recess and will not press the contact properly.
4. **Plug fully inserted** — make sure the plug is pushed all the way in.

Recommended plug: **DC 2.1 / 5.5 mm**, male, with cable.

If the issue persists after the checklist, email us at **[bee@apisense.ai](mailto:bee@apisense.ai)**.

## 4. After replacing the batteries in a Scale or VitalSensor

After a routine battery replacement (2× AA) in a Scale or VitalSensor, **no additional steps** are required in the app or on the Hub, Scale or VitalSensor device. Do not re-pair devices, add them to the hive again, or press the RESET button.

After replacing the batteries:

- place the device back in its target location,
- make sure it is within range of the Hub (maximum approximately 35 m),
- wait for the next measurement cycle.

Updated data will appear in the app automatically, which may take up to several hours, provided that the Hub device is communicating properly with the system (it is not offline — discharged battery/no connectivity).

Detailed battery replacement instructions and answers to common questions: [FAQ — after battery replacement](../../faq/index.md#after-battery-replacement).

After the Hub has discharged and you reconnect it to charging or expose it to the sun, the Hub will automatically resume operation — **do not press** the RESET button.
