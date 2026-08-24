# Compliance and legal information

This page provides information about radio connectivity, safe use, and compliance of Apisense devices with European Union regulations (Radio Equipment Directive RED 2014/53/EU).

______________________________________________________________________

## Apisense VitalSensor

### Radio information

| Radio | Band | Max. transmit power |
|---|---|---|
| Bluetooth Low Energy 2.4 GHz | 2400–2483.5 MHz | 9 dBm EIRP |

Antenna: internal (integrated on the device PCB) — not replaceable.
The device meets electromagnetic field exposure requirements (EN IEC 62479) without any additional installation conditions.

### Safe use

- Power: 2× AA battery. At ambient temperatures above **+50 °C**, use lithium (FR6) batteries instead of alkaline (LR6).
- Operating temperature range: **−20…+55 °C**.
- The device does not charge batteries — use non-rechargeable batteries only.

______________________________________________________________________

## Apisense Scale

### Radio information

| Radio | Band | Max. transmit power |
|---|---|---|
| Bluetooth Low Energy 2.4 GHz | 2400–2483.5 MHz | 9 dBm EIRP |

Antenna: internal (integrated on the device PCB) — not replaceable.
The device meets electromagnetic field exposure requirements (EN IEC 62479) without any additional installation conditions.

### Safe use

- Power: 2× AA battery. At ambient temperatures above **+50 °C**, use lithium (FR6) batteries instead of alkaline (LR6).
- Operating temperature range: **−20…+55 °C**.
- The device does not charge batteries — use non-rechargeable batteries only.

______________________________________________________________________

## Apisense Hub

### Radio information

| Radio | Bands | Max. transmit power |
|---|---|---|
| Bluetooth Low Energy 2.4 GHz | 2400–2483.5 MHz | 17.3 dBm EIRP |
| LTE Cat 1 | B1 / B3 / B5 / B7 / B8 / B20 / B28 | 25 dBm (power class 3) |
| GSM (fallback) | 900 / 1800 MHz | 33.5 dBm / 29.5 dBm |
| GNSS | 1559–1610 MHz | receiver only — does not transmit |

WiFi is permanently disabled in the device firmware.

### Antennas — use ONLY the following

| Port (connector) | Antenna | Max. gain |
|---|---|---|
| RP-SMA (BLE) | Sunnyway SWE035-RP (P/N SW25156EB56) — included | 5.3 dBi |
| SMA (LTE) | Sunnyway SWE038 (P/N SZ20228WB56) — included | 5.0 dBi |

The GNSS antenna is internal (factory-fitted) and is not user-replaceable.

!!! warning "Important"
    Connecting a different antenna, or an antenna with higher gain, voids the device's compliance with EU radio regulations.

### Installation distance

Install the Hub so that it is located **at least 40 cm** away from places where people are permanently present.

### Location (GNSS)

The device periodically (a few times per day) determines the position of the **apiary** — the Hub installation site — in order to display it on the map in the app. The device is not designed to track the location of persons and does not process data that could identify the user.

### Safe use

- Power: built-in Li-Ion battery charged from the photovoltaic panel or the low-voltage connector. The battery is not intended for user replacement.
- Operating temperature range: **−10…+55 °C**; battery charging takes place within **0…+45 °C** (outside this range charging is automatically suspended).
- The device is designed for outdoor installation (IP65) — on a post or tree, as described in the manual.

______________________________________________________________________

## EU Declarations of Conformity

EU Declarations of Conformity for Apisense devices are published on this page.

<!-- TODO(compliance): after DoC signing, link the PDFs using raw HTML <a href> (i18n!):
     - VitalSensor (LAVANDULA-H1)
     - Scale (LONICERA-S1)
     - Hub (TILIA-G1)
     Files → docs/downloads/files/ or docs/compliance/files/ -->

You can also obtain a copy of the Declaration of Conformity for your device by contacting us via the [help section](../faq/index.md).
