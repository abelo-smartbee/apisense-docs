# Troubleshooting

## 1. Problem List and Suggested Solutions

| No. | Problem | Device | Suggested Solution |
| --- | ------- | ------ | ------------------ |
| 1 | Device inactive (never checked in) | VitalSensor | 1. Check battery installation. Remove and reinsert the battery, observing polarity. 2. Check that the battery is not depleted; replace if so. **Note:** after correct battery installation the LED should light up. 3. If the problem persists or wires are damaged, contact Apisense support. |
| 2 | Depleted / very low battery | VitalSensor | Replace the battery, observing polarity. **Note:** after correct battery installation the LED should light up. If the problem persists or wires are damaged, contact Apisense support. |
| 3 | No communication with Apisense Hub despite correct power supply (no BLE range) | VitalSensor | Move the sensor closer to the Apisense Hub. Within 12 hours the sensor should appear in the system. If the problem persists, contact Apisense support. |
| 4 | Weak BLE signal (below −90 dBm) | VitalSensor | Rotate the sensor in the frame or the entire frame by 180° (LED in sensor facing the Apisense Hub). Signal level should rise above −90 dBm. If the problem persists, consider relocating the Hub closer to the sensor, taking care not to degrade range for other devices. Contact Apisense support if needed. |
| 5 | No communication with Apisense Hub (no BLE range) | Scale | Move the scale closer to the Apisense Hub. Within 12 hours the device should appear in the dashboard. If the problem persists, contact Apisense support. |
| 6 | Weak BLE signal (below −90 dBm) | Scale | Ensure the scale electronics face the Apisense Hub. Consider relocating the Apisense Hub closer to the scale while maintaining range for other devices. Signal level should rise above −90 dBm. Contact Apisense support if needed. |
| 7 | LED does not light up after pressing the Power button | Hub | Check power supply — if the Hub is not receiving enough light, consider changing its position (tilt, height) or use external power. Allow the Hub to charge (approx. 3 hours), then press the Power button — the LED should light up and within 90 minutes the Hub should appear in the dashboard. If the Hub has not been charged for an extended period, see problem "No charging". |
| 8 | No charging | Hub | Check the connection of the solar panel to the Apisense Hub. Verify the panel position is correct (no shading, facing the sun, minimum 20° tilt). The dashboard should show the Hub charging. If the problem persists, contact Apisense support. |
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
