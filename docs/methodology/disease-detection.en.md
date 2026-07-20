# How disease detection works

You increasingly ask us **how disease detection in Apisense actually works** and how the app "knows" that something is wrong with a colony. This page explains it in plain language — no formulas, no statistical tables.

If you are interested in **how our models are built step by step** (from the idea, through the laboratory, to deployment in apiaries), see [How our models are built](research-process.md).

______________________________________________________________________

## In a nutshell

The **VitalSensor**, placed between the frames, continuously **"smells" the air inside the hive**. Every colony has its own natural "scent" — a chemical fingerprint made up of many compounds. When a disease develops, this fingerprint **changes in a characteristic way**, usually long before you can see any symptoms with the naked eye.

Our **artificial intelligence (AI)** has learned to recognise these patterns and, based on them, assigns the colony a **health status and an infection level** — and you see the result in the Apisense Pro AI app.

!!! info "A complement, not a replacement"
    Detecting disease from hive air **supports** your observations and inspections — it does not replace them. Treat alerts as an early "take a closer look at this colony" signal, not as a final diagnosis.

______________________________________________________________________

## What the sensor "senses"

The VitalSensor measures more than a dozen parameters inside the hive. The most important are:

- **The chemical composition of the air** — volatile organic compounds (VOCs), i.e. the colony's chemical "scent",
- **Temperature and humidity** — the microclimate of the nest,
- **Other environmental parameters** — including carbon dioxide level and acoustic activity (the sounds of the colony).

You can compare it to a doctor who recognises an illness from a patient's breath or smell — except here the "nose" is a sensor and the "memory of experience" is artificial intelligence.

______________________________________________________________________

## How the AI knows what is sick

A sensor reading on its own would tell us nothing without a **reference to reality**. That is why our models learn from **thousands of labelled samples**, in which sensor readings are paired with the **actual examination result** for a given colony — e.g. the number of *Nosema* spores under a microscope or the *Varroa* infestation level.

We collect this data both in the **laboratory** (colonies in cages with sensors) and in **real apiaries**. Each disease leaves its own recognisable "signature" in the data, and the model learns to tell it apart from a healthy state.

We describe this whole process — from idea to global rollout — on the [How our models are built](research-process.md) page.

______________________________________________________________________

## Infection levels — what they mean

For some diseases the app shows not just "present / absent" but also a **level**: low, moderate or high. The values below are **approximate thresholds** we use to label our data — they are aligned with the standard examinations beekeepers perform every day, so they are easy to relate to your own apiary.

### Varroosis (*Varroa destructor*)

| Level | Flotation (alcohol wash) | Daily natural drop | What it means |
|---|---|---|---|
| **Low** | up to ~2% infestation | 2–3 mites per day | Acceptable and common — *Varroa* is present but does not yet threaten the colony. |
| **Moderate** | ~3–4% infestation | 4–10 mites per day | A disease — worth planning a treatment. |
| **High** | above ~5% infestation | above 11 mites per day | Advanced varroosis — the colony needs intervention. |

!!! note "Flotation: alcohol wash vs. sugar roll"
    The flotation thresholds above refer to the **alcohol wash** — the reference method (the most accurate, but it destroys the sample). For everyday monitoring we also describe the gentler, non-invasive [sugar roll](../procedures/varroa-sugar-roll.md), after which the bees go back to the hive. Both methods report infestation as a percentage, but the sugar roll usually recovers slightly fewer mites.

### Nosemosis (*Nosema* / *Vairimorpha* spp.)

| Level | Spore count (per 10 bees) | What it means |
|---|---|---|
| **Low** | 1–3 spores | Acceptable and common — nosemosis is present but does not yet pose a threat. |
| **Moderate** | 4–40 spores | A disease. |
| **High** | above 40 spores | Advanced disease. |

!!! note "Where this spore count comes from"
    The spore count is determined under a microscope — we describe it in the [Nosema/Vairimorpha microscopy](../procedures/nosema-microscopy.md) procedure. The values in the table are the average number of spores per 10 bees.

### American foulbrood and chalkbrood

For these diseases the model detects **presence**, not a level:

- **American foulbrood (AFB)** — a "foulbrood risk has appeared" signal. This is a **notifiable disease**, which is why we collect its data in a special way — described on the [How our models are built](research-process.md#foulbrood-exception) page.
- **Chalkbrood** — we distinguish a healthy state, mere exposure (contact without visible symptoms) and clear disease symptoms.

______________________________________________________________________

## More diseases on the way

We are constantly developing the system. We are working on detecting further threats, including **amoebiasis**, the **greater wax moth** and **viruses** transmitted by *Varroa* (e.g. deformed wing virus, DWV). Once the models pass our validation process, we will add them to the app.

______________________________________________________________________

## See also

- [How our models are built](research-process.md) — the journey from idea to deployment in apiaries.
- [Lab procedures](../procedures/index.md) — how to perform the flotation and microscopy yourself and report the results.
- [System overview](../overview/index.md) — what the VitalSensor, Hub, Scale and Apisense Pro AI app are.
