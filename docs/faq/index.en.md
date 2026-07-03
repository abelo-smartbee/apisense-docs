# Frequently Asked Questions (FAQ)

Questions and answers collected during the **Apisense 2026 Global Field Validation Study**.

## VitalSensor & placement

### Does the colour of the NFC/QR tag attached to the VitalSensor matter?

No. Colour is irrelevant — the VitalSensor–tag pairing is what matters.

### Where exactly should the VitalSensor be placed?

Vertically, on a brood frame in the nest part of the hive — ideally in the centre or next to the centre.

### Can I move VitalSensors up/down when adding boxes?

Yes, within the nest. Always add a note about such an action in the app (preferably along with a photo).

### Can VitalSensors be installed on non-standard frames?

Yes, using zip ties. Please add a note (and preferably a photo) of the VitalSensor after installation.

### Can VitalSensors be used in nucs (and other smaller hives) and then moved to bigger ones later?

It is recommended to wait with VitalSensor installation until the hive is in its final size (unless you want to use a small size, e.g. mini plus, through the whole season — in such case contact us first).

### How do I replace the batteries in the VitalSensor?

The VitalSensor is powered by **2× AA alkaline** batteries.

1. Open the cover.
2. Replace the batteries with **2× AA alkaline**.
3. Close the cover.

## Hub & connectivity

### Can the Hub be installed indoors or under a roof?

No. It must be outdoors for GPS and proper connectivity.

### Can I power the Hub permanently via electricity?

Yes, you can power it via USB-C, as long as it remains outdoors and is uncovered.

### Does the Hub need a battery replacement?

No. The Hub charges from a solar panel (PV). If sunlight is insufficient, you can top it up via USB-C.

### The Hub isn't charging despite full sun — why?

This is correct behaviour — a battery safety protection has kicked in. The Hub only charges when the temperature inside the device stays below **50°C**. With a south-facing installation during hot weather, the internal temperature can reach about **70°C**, so charging is suspended for safety. Paradoxically, the all-day full sun is the reason charging stops here — the device is working correctly. Once the temperature drops, charging resumes automatically.

### How far can the Hub be from the hives?

Up to approx. 30–40 metres.

### The Hub is not appearing in the app — what should I do?

Follow the instructions in the user manual; you can also ask the assistant in the app for instructions. The general recommendations are:

- Check orientation (logo readable, antennas pointing vertically upwards).
- Leave it outdoors for ~15 minutes.
- Try USB-C charging.

If it still does not work, contact [bee@apisense.ai](mailto:bee@apisense.ai).

### A VitalSensor or Scale won't connect to the Hub — what should I do?

Devices reach the server through the Hub (VitalSensor/Scale → Bluetooth → Hub → LTE → server), so the order matters:

1. **The Hub must connect first.** No VitalSensor or Scale can connect until the Hub is online. The Hub is solar-powered — its first contact after power-on takes from ~30 minutes (charged) up to 24 hours (discharged, in bad weather). In the app, pick the start-up scenario to see the estimated time.
2. **Once the Hub is connected**, each VitalSensor and Scale has its own first-connection window. During it the app shows *"awaiting connection"* — this is normal, please wait.
3. If a device still hasn't connected after that window, the app shows *"out of range"* — the Hub is online but cannot see the device over Bluetooth. Most common causes: the device is too far from the Hub, or an issue with the device itself (e.g. power).

If some devices connect and others don't (e.g. one VitalSensor works, the rest don't), the problem is with those specific devices, not the Hub.

If the problem persists, contact [bee@apisense.ai](mailto:bee@apisense.ai).

## Scale

### Does the Scale need batteries or charging?

Yes. The Scale is powered by **2× AA alkaline** batteries. Once installed and added to the app (QR code) it works automatically — you only replace the batteries when they run out.

### How do I replace the batteries in the Scale?

You will need a **4 mm** Allen (hex) key (for the brackets) and a **T6** Torx key (for the black housing).

1. Unscrew the brackets with the 4 mm Allen key — undo the two screws.
2. Undo the two T6 Torx screws on the black housing.
3. Replace the batteries with **2× AA alkaline**.
4. Screw the black housing back on.
5. Screw the brackets back on.

### Which hive should be on the Scale?

Any VitalSensor-equipped hive — trends matter more than the exact weight of a particular hive.

## Data entry & Apisense app usage

### Do notes have to be added in the field?

No. You can add them later with the correct date.

### Can multiple people access the same app data?

Not confirmed yet — Apisense will follow up by email.

## Tests & samples

### Do I need to do the Varroa sugar roll in the Global Field Validation Study tests?

Yes — always. The Varroa sugar roll is **mandatory in every scheduled test** (Test 1, 2 and 3), for every monitored colony. You run it every time, regardless of the time of season, sensor readings or the absence of visible Varroa symptoms. Each test covers the full set of **both procedures**: the Varroa sugar roll **and** Nosema/Vairimorpha microscopy. Details: [Lab procedures](../procedures/index.md).

### Can you freeze bee samples for Nosema testing?

Yes — **freezing bees is accepted only** for *Nosema* tests.

- Each frozen sample must be **clearly and easily identified** with the hive it comes from.
- Storage temperature: **at least −8 °C**.
- Bee samples can be stored in the freezer for approximately **3–5 months** before testing or shipping to the lab.
- Samples **must not be thawed and frozen again**.

Details: [Nosema/Vairimorpha microscopy](../procedures/nosema-microscopy.md#storage-before-testing), [Registering a sample](../manual/app-manual.md#rejestrowanie-probki).

## Beekeeping practices

### Can I use oxalic or formic acid treatments?

Yes. Please add a note in the app once doing so.

### Can VitalSensors be moved if a colony dies or is lost?

Do not move VitalSensors without letting the Apisense team know first! To prevent the risk of disease spread and for data integrity reasons, in such a situation always contact us directly and wait for further instructions.

### I'm moving a VitalSensor to another colony (e.g. after a colony died) — how do I reflect this in the app?

A new colony = a new hive in the app. Do it in three steps:

1. **Create a new hive** in the app — the old hive stays unchanged.
2. **Unbind the devices from the old hive** and **bind them to the new one** (after disinfecting the VitalSensor).
3. From now on new measurements go to the new hive.

Measurement history is **not** transferred between hives — it was a different colony, so the old hive's data does not describe the new one. That is why the data starts fresh with the new hive. You don't need to let us know — once you create the new hive and re-assign the devices to it, we have the full picture.

### What about splitting colonies or adding/removing supers?

Always add a note on such activities — it supports correct data interpretation.

### What if I transport my hives?

Transport all hives + Hub + Scale together and add a note in the app.
