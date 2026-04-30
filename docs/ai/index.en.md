# Assistant

The Assistant in Apisense is not a generic chatbot from the internet. It is a **dedicated assistant integrated with your entire Apisense system** — it knows your apiaries, hives, device status, scheduled inspections, and the weather above your apiary.

In other words: the Assistant **translates raw technical data from the IoT system into simple answers in plain language**. Instead of scanning a table of scale readings from the last 24 hours, you ask "is anything worrying happening in hive number 3?" and get a concrete answer.

You do not need to learn any commands or filters. Just ask the question the way you would ask a fellow beekeeper.

______________________________________________________________________

## 1. Why you want the Assistant

In day-to-day apiary work, you keep running into questions that are slow to answer:

- *"Is the scale in hive number 3 still connected?"*
- *"When did I last inspect the Linden apiary?"*
- *"What is tomorrow's forecast above my apiary?"*
- *"What should I do if I see bees with deformed wings?"*
- *"How do I set an alarm in the app for when a hive's mass suddenly drops?"*

Instead of clicking through several screens, reading documentation, or searching the internet — you ask the Assistant and get a concise answer in your language.

______________________________________________________________________

## 2. The Assistant translates technical sensor data

Your hive sends Apisense dozens of readings every day: mass, temperature, humidity, pressure, connection status, battery level. Raw numbers on their own do not say much — you need context, baselines, and trends. The Assistant takes that data and **turns it into a concise diagnosis in plain language**.

!!! example "Example — raw data → readable answer"
    **Raw data** in the Apisense database (which the beekeeper does not look at every day):

    > hive 4, Linden apiary: mass 38.2 kg (-0.4 kg / 24h), internal temperature 34.8°C, humidity 62%, sensor battery 88%, last reading 12 minutes ago

    **You:** What is going on in hive 4 in the Linden apiary?

    **Assistant:** Hive 4 (Linden) is doing well — internal temperature 34.8°C is normal for an active brood, humidity 62% is correct. The mass dropped by 0.4 kg in the last day, which is typical with the current weather (no nectar flow, light wind) — it does not point to swarming or a colony problem. The sensor connects regularly, battery 88%.

The same applies to gateways (Hub) and scales — the Assistant **does not leave you with the numbers**, it interprets them in the context of your apiary, the weather, and the history of your recent inspections.

______________________________________________________________________

## 3. What you can ask

Below are six groups of typical questions with concrete examples. **You can ask in your own words** — the Assistant understands natural phrasing, not just the exact wording shown here.

### 3.1 Your apiaries and hives

!!! example "Sample conversation"
    **You:** How many active hives do I have?

    **Assistant:** You have 12 active hives across 3 apiaries: Linden (5), Acacia (4), Heather (3).

!!! example "Sample conversation"
    **You:** Show the status of the Linden apiary.

    **Assistant:** Apiary **Linden** contains 5 hives. The gateway is online (LTE signal: good, last contact: 8 minutes ago, battery: 78%). Latest sensor readings are less than 24 hours old.

### 3.2 Devices and gateways

!!! example "Sample conversation"
    **You:** Does the gateway in the Acacia apiary have an LTE signal?

    **Assistant:** Yes. The gateway in the **Acacia** apiary has a good LTE signal and connected 3 minutes ago. Battery: 64%.

!!! example "Sample conversation"
    **You:** Which scales have a low battery?

    **Assistant:** Two scales have a battery level below 20%:

    - Apiary **Linden**, hive 2 — 17%
    - Apiary **Heather**, hive 1 — 12%

    Plan a replacement before your next apiary visit.

### 3.3 Calendar and inspections

!!! example "Sample conversation"
    **You:** What treatments do I have scheduled this week?

    **Assistant:** This week you have 2 scheduled treatments:

    - **Tuesday** — queen presence check, Linden apiary, hives 1–5
    - **Friday** — anti-Varroa treatment, Acacia apiary, hives 1–4

!!! example "Sample conversation"
    **You:** When did I last inspect hive 7 in the Heather apiary?

    **Assistant:** The last inspection of hive 7 in the Heather apiary was **12 days ago**. In your note you marked good colony condition and a noticeable honey gain.

### 3.4 Weather above the apiary

The Assistant automatically pulls weather for the location of your apiaries — you do not even need to give the city.

!!! example "Sample conversation"
    **You:** What is the weather at the Linden apiary today?

    **Assistant:** At the **Linden** apiary today: temperature 18°C, partial cloud cover, wind 12 km/h from the west. No rainfall. Good conditions for bee flight.

!!! example "Sample conversation"
    **You:** Will it rain tomorrow above my apiaries?

    **Assistant:** Yes — near the **Acacia** apiary, rain is expected from the afternoon onwards (5–8 mm). The other apiaries stay in the dry zone.

### 3.5 Beekeeping knowledge

!!! example "Sample conversation"
    **You:** How do I recognise Varroa?

    **Assistant:** Varroa is an infestation by the *Varroa destructor* parasite. The most common signs:

    - visible reddish-brown mites on bees or brood;
    - bees with deformed wings (DWV virus carried by Varroa);
    - a weakened colony that overwinters poorly.

    Diagnostics is most often done with a sugar-roll test or icing-sugar dusting. Apisense also records treatment recommendations — check the *Notifications* → *Issues* tab.

!!! example "Sample conversation"
    **You:** When should I start winter feeding?

    **Assistant:** Winter feeding usually starts at the turn of August and September — after the last honey harvest, before temperatures drop. Doses depend on the region and the colony's strength. For your apiaries I can check the most recent scale readings and suggest whether any colony urgently needs feeding.

### 3.6 Apisense system manuals and configuration

When you ask "how do I do this in the app" or "how do I configure a device" — the Assistant walks you through it step by step. When an **official Apisense YouTube video tutorial** matches your question, it adds a specific link to the film — in your language, if a localised version is available. It does not invent fake URLs: if no official video exists, no link will appear.

!!! example "Sample conversation — app instruction + video"
    **You:** How do I add a new hive in the app?

    **Assistant:** You add a new hive from the apiary view:

    1. In the *Apiaries* tab, open the apiary you want to add a hive to.
    2. In the *Hives* view, click the **+** icon in the top-right corner.
    3. Enter the hive name and (optionally) the sensor serial number.
    4. Confirm.

    Short video tutorial: [official Apisense YouTube channel](https://www.youtube.com/@Apisense.Global) *(the Assistant adds a specific film URL if one exists in your language)*.

!!! example "Sample conversation — device configuration"
    **You:** How do I set an alarm for when a hive's mass suddenly drops by 5 kg?

    **Assistant:** You set a threshold alarm for sudden mass change in *Hive settings* → *Alarms*:

    1. Pick the hive in the *Hives* view.
    2. Open *Hive settings* → *Alarms* tab.
    3. Enable "Mass drop alarm" and set the threshold (e.g. 5 kg / 24h).
    4. Choose how you want to be notified (push, email).
    5. Save.

    Once saved, the alarm starts working immediately — the system monitors each hive independently.

______________________________________________________________________

## 4. The conversation remembers context

You can follow up the way you would in normal conversation — the Assistant remembers what you just said.

!!! example "Sample conversation"
    **You:** What is the status of the Linden apiary?

    **Assistant:** Linden apiary: 5 hives, gateway online, last contact 4 minutes ago...

    **You:** And the Acacia apiary?

    **Assistant:** Acacia apiary: 4 hives, gateway online, last contact 8 minutes ago...

Every conversation is saved in your account — you can come back to it later or delete it from the settings. You can also start a **new conversation** from scratch if you want to switch topics without history.

______________________________________________________________________

## 5. Multiple languages

Write in English, Polish, German, Italian, or French — the Assistant **answers in the same language** you wrote your question in. The app's interface language does not have to match the language of your conversation: you can have the app in Polish and ask the Assistant in English.

______________________________________________________________________

## 6. What the Assistant will not do

The Assistant in Apisense is a helper — it does not perform actions in your apiary on your behalf:

- It does not change or delete data in the app (it will not remove a hive, add an inspection, or raise an alert).
- It does not analyse photos, audio, or video. It works on text only.
- It does not know information about other people's apiaries (see [Capabilities & Privacy](limits-privacy.md)).

The full list of limits and privacy rules is on a dedicated page.

______________________________________________________________________

## 7. Your privacy

The Assistant sees only **your** data (or apiaries you have access to). Your conversations are saved so you can come back to them — but you can delete them at any time. Your data is not used to train third-party models.

Details: [Capabilities & Privacy →](limits-privacy.md)

______________________________________________________________________

## 8. Getting started

The Assistant is built into the Apisense Pro AI app:

- In the mobile app and in the web version it is available under the **Your assistant** icon in the bottom menu.
- It works in the *Apiaries*, *Hives*, and *Hive* views, so help is at hand wherever you are working.
- Write in your own language — the Assistant answers in the same language you asked your question in.

<!-- TODO: screenshot - "Your assistant" tab with an empty conversation -->
