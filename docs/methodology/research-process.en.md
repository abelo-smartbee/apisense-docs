# How our models are built

Every disease-detection model follows **the same path** with us — from the first idea, through laboratory research, all the way to deployment in apiaries around the world. Thanks to this, by the time an alert reaches your app, the model behind it has been verified many times over.

On this page we show that process step by step. If you are looking for an explanation of **how the detection itself works** and what the infection levels mean, see [How disease detection works](disease-detection.md).

______________________________________________________________________

## From idea to deployment

<p style="text-align:center;">
  <img src="../pictures/rd-lifecycle-en.svg" alt="The lifecycle of Apisense models: idea, laboratory phase, experimental apiaries, deployment with continuous re-training" style="width:100%;max-width:780px;">
</p>

### 1. Idea & concept

It all starts with the question **"what else is worth monitoring?"**. We draw ideas from:

- conversations with beekeepers and their everyday problems,
- a review of the scientific literature,
- the latest reports and developments in the field.

At this stage we choose a threat that can realistically be detected from changes in the hive's air and microclimate.

### 2. Laboratory phase

We test the chosen idea under controlled conditions. We place bees in **laboratory cages together with sensors**, forming:

- **infected groups** — with a controlled, measured level of disease,
- **control groups** — healthy, for comparison.

We determine the infection level with **laboratory examinations** (e.g. spore counting, flotation), and then check **whether the sensor readings actually match the lab results**. If there is a clear relationship, we build the **first models** and assess how well they recognise the disease.

### 3. Experimental apiaries

If the laboratory results are promising, we **scale the experiment up** — to apiaries operating in near-real conditions, under the constant care of beekeepers and scientists.

The data from these apiaries is far richer and more varied than the laboratory data (weather, nectar flows, different colonies), so we **re-train the models** on this larger sample and re-check their performance.

### 4. Deployment & continuous re-training

When a model maintains its performance in the experimental apiaries too, we usually **deploy it for the next season and make it available globally** to all users.

But we do not stop there. The data that flows into the app — **your notes, inspections and examination results** — becomes our new set of labels. Based on it we **continuously re-train the models**, so they become more accurate with every season.

!!! tip "Why your entries matter"
    Every reported flotation, microscopy or inspection result helps teach the models. The more reliable labels we get from beekeepers, the better the system recognises diseases — including in your own apiary.

______________________________________________________________________

## American foulbrood — a special case { #foulbrood-exception }

One disease escapes the scheme above: **American foulbrood (AFB)**. It is a **notifiable disease**, so — unlike *Varroa* or *Nosema* — **we cannot induce it or "grow" it in an apiary** for research purposes.

That is why we collected foulbrood data differently:

- the sensors were installed in hives by **befriended beekeepers and vets** when they had a **well-founded suspicion** of foulbrood,
- we recorded the data **while awaiting laboratory confirmation**,
- once the disease was confirmed, the **equipment was disposed of**, in line with biosecurity rules.

Thanks to this cooperation we were able to teach the model to recognise the signals of foulbrood without putting any healthy colony at risk.

______________________________________________________________________

## See also

- [How disease detection works](disease-detection.md) — what the sensor measures and what the infection levels mean.
- [Lab procedures](../procedures/index.md) — how to perform and report the examinations that feed our models.
