# Quote Behavior Analysis — Amplitude Data
Date: 2026-04-30
Source: data/amplitude/quote-events.csv
Period: 2026-01-08 to 2026-03-25
Dataset: 72 quotes sent, 50 deals, 27 deals won

---

## 1. Do quotes with more views close at higher rates?

Yes — and the jump is dramatic at 3+ views.

| Views | Closed / Total | Close Rate |
|-------|---------------|------------|
| 0 | 6 / 18 | 33.3% |
| 1 | 5 / 17 | 29.4% |
| 2 | 5 / 12 | 41.7% |
| 3+ | 20 / 25 | **80.0%** |

One view is not meaningfully different from zero views (29.4% vs 33.3%). The signal doesn't start until the buyer comes back — repeated engagement is the indicator, not first contact. The 3+ threshold is where the close rate more than doubles.

## 2. Are downloads and feedback stronger signals?

Both are stronger than views alone, but the sample sizes are small.

| Signal | Closed / Total | Close Rate |
|--------|---------------|------------|
| Downloaded (among viewed) | 6 / 7 | **85.7%** |
| Not downloaded | 24 / 47 | 51.1% |
| Feedback sent (among viewed) | 5 / 6 | **83.3%** |
| No feedback | 25 / 48 | 52.1% |

A buyer who downloads the PDF or sends feedback is almost certainly closing. But these are rare events (7 downloads, 6 feedback instances out of 54 viewed quotes) — they're strong confirming signals, not the primary triage metric.

## 3. Combined engagement tiers

The clearest decision boundary is between "low engagement" and "3+ views."

| Tier | Closed / Total | Close Rate |
|------|---------------|------------|
| No engagement (0 views) | 6 / 18 | 33.3% |
| Low (1-2 views only) | 10 / 29 | 34.5% |
| Medium-high (3+ views, no download/feedback) | 9 / 12 | 75.0% |
| High (3+ views + download/feedback) | 11 / 13 | **84.6%** |

The bottom two tiers are functionally identical (33-34%). This means the data reps currently can't see — repeated views — is exactly what separates a probable close from a coin flip.

## 4. Multi-quote deals: views predict the winner

In deals where multiple quotes were sent:
- Single-quote deals close at 57.1% (20/35)
- Multi-quote deals close at 46.7% (7/15)

But the critical finding: **in all 7 won multi-quote deals, the winning quote had the most views of any sibling.** 7/7, no exceptions. View count doesn't just predict whether a deal closes — it predicts which option the buyer picks.

This directly validates qualitative Code 4 ("Which quote did they actually read?"). Anna's customer Dennis opened option B "meerdere keren" and never opened option C — the Amplitude data confirms this pattern scales: the most-viewed option is the one that wins.

## 5. Time to first view does not predict close rate

| First View Timing | Closed / Total | Close Rate |
|-------------------|---------------|------------|
| Within 24 hours | 7 / 14 | 50.0% |
| After 24 hours | 23 / 40 | 57.5% |

Speed of first view is noise. It doesn't matter when they first look — it matters how many times they come back. This is important for design: a "last opened" timestamp is useful context, but view count is the actionable metric.

## 6. Rep behavior: cloudsign_activity_clicked

How often reps click "View activity" relative to quotes they send:

| Rep | Clicks / Quotes Sent | Ratio |
|-----|---------------------|-------|
| Mark Devos | 4 / 6 | 0.67 |
| David O'Connor | 5 / 9 | 0.56 |
| Maaike de Vries | 5 / 9 | 0.56 |
| Eric Larsson | 3 / 7 | 0.43 |
| Sara van den Berg | 3 / 7 | 0.43 |
| Anna Smit | 1 / 5 | 0.20 |
| Sofia Klein | 1 / 7 | 0.14 |
| Lisa Hofmann | 1 / 7 | 0.14 |
| Tom Bakker | 1 / 7 | 0.14 |
| Pieter Janssens | 1 / 8 | **0.12** |

Cross-referencing with qualitative data:

- **Pieter Janssens** (lowest ratio, 0.12): "I always call about 48 hours after sending a quote... the tracking isn't always reliable." He's abandoned the panel entirely. The data confirms it.
- **Mark Devos** (highest ratio, 0.67): His VP Sales Ops (Marcia) says he "keeps a separate spreadsheet because he doesn't trust it." He clicks the most — but supplements with a parallel system because what he finds is unreliable.
- **Maaike de Vries** (0.56): "I wish I could just see a simple view count... Instead I'm kind of guessing." She's checking frequently but not getting actionable signal.

The reps who click most aren't the ones who trust the data — they're the ones trying hardest to extract signal from a broken tool.

---

## Key Takeaways

1. **View count is the single strongest engagement signal** for predicting close. The threshold is 3+ views (80% close rate vs ~33% for 0-1 views).
2. **Downloads and feedback are confirming signals**, not discovery signals. They're rarer but near-certain indicators of close.
3. **In multi-quote deals, views predict the winner** — 7/7 in this dataset. Surfacing per-quote view counts would eliminate the blind triage reps describe.
4. **First-view timing is not predictive.** Design should prioritize view count over recency.
5. **Rep click behavior correlates with qualitative codes**: lowest clickers have abandoned the panel (Code 6), highest clickers are working around it (Code 3).

---

## 7. How often do reps click "View activity"?

Across all 10 reps in the dataset, there were **25 total cloudsign_activity_clicked events** against **72 quotes sent** — a global ratio of **0.35 clicks per quote**. Most quotes are never checked.

### Per-rep breakdown

| Rep | Tenure | Quotes Sent | Clicks | Ratio | Deals Won | Win Rate |
|-----|--------|-------------|--------|-------|-----------|----------|
| Mark Devos | 30mo | 6 | 4 | 0.67 | 4/5 | 80.0% |
| David O'Connor | 36mo | 9 | 5 | 0.56 | 1/5 | 20.0% |
| Maaike de Vries | 20mo | 9 | 5 | 0.56 | 4/5 | 80.0% |
| Eric Larsson | 48mo | 7 | 3 | 0.43 | 3/5 | 60.0% |
| Sara van den Berg | 24mo | 7 | 3 | 0.43 | 4/5 | 80.0% |
| Anna Smit | 4mo | 5 | 1 | 0.20 | 3/5 | 60.0% |
| Sofia Klein | 7mo | 7 | 1 | 0.14 | 3/5 | 60.0% |
| Lisa Hofmann | 6mo | 7 | 1 | 0.14 | 1/5 | 20.0% |
| Tom Bakker | 10mo | 7 | 1 | 0.14 | 2/5 | 40.0% |
| Pieter Janssens | 8mo | 8 | 1 | **0.12** | 2/5 | 40.0% |

## 8. Do senior reps check more than junior reps?

Yes — 3.5x more often.

| Cohort | Reps | Clicks / Quotes | Ratio | Deal Win Rate |
|--------|------|-----------------|-------|---------------|
| Junior (≤10 months) | 5 | 5 / 34 | **0.15** | 44.0% (11/25) |
| Senior (>10 months) | 5 | 20 / 38 | **0.53** | 64.0% (16/25) |

Junior reps barely touch the activity panel. Every rep under 10 months tenure has a click ratio of 0.20 or below. Senior reps click 3.5x more frequently. This aligns with the qualitative data in two ways:

- **Code 6 ("They told me to just ignore it")**: junior reps at Axis SaaS take the data at face value and wait, or get told to ignore it entirely. They don't develop a habit of checking because the first few checks produce "Offline" and they learn to stop.
- **Code 3 ("That spreadsheet shouldn't need to exist")**: senior reps like Mark Devos (highest ratio, 0.67) check more because they've learned to triangulate — click the panel, check email, call the customer, log it in a spreadsheet. They click more, but not because they trust the data more.

## 9. Do reps who check regularly close at higher rates?

The relationship is positive but not linear.

| Click Frequency | Reps | Deals Won | Win Rate |
|----------------|------|-----------|----------|
| Low (<0.3 ratio) | Anna, Lisa, Sofia, Pieter, Tom | 11/25 | 44.0% |
| Medium (0.3-0.5 ratio) | Eric, Sara | 7/10 | **70.0%** |
| High (>0.5 ratio) | David, Mark, Maaike | 9/15 | 60.0% |

Medium clickers (0.3-0.5) actually have the highest win rate, not the highest clickers. The high-click group is pulled down by David O'Connor (36 months tenure, 5 clicks, but only 1/5 deals won). David is the CSM who discovered Rachel's quote showing "Offline" in call-002 — he's checking frequently because he's doing damage control, not because checking helps him close.

At the deal level, the signal is cleaner:

| | Deals Won / Total | Win Rate |
|---|---|---|
| Rep clicked View Activity at least once | 12 / 18 | **66.7%** |
| Rep never clicked | 15 / 32 | 46.9% |

Deals where the rep checked the activity panel at any point close at a 20-point higher rate. But caution: this likely reflects confounders (more engaged reps check more AND do other things that help close) rather than the click itself causing the close.

## 10. Rep click ratio vs. buyer engagement on their quotes

| Rep | Click Ratio | Avg Buyer Views | Median Buyer Views |
|-----|------------|-----------------|-------------------|
| Sara van den Berg | 0.43 | 3.9 | 5 |
| Maaike de Vries | 0.56 | 3.7 | 4 |
| Anna Smit | 0.20 | 3.4 | 3 |
| Mark Devos | 0.67 | 3.2 | 4 |
| Eric Larsson | 0.43 | 2.6 | 1 |
| David O'Connor | 0.56 | 2.3 | 1 |
| Tom Bakker | 0.14 | 2.1 | 1 |
| Pieter Janssens | 0.12 | 1.9 | 1 |
| Lisa Hofmann | 0.14 | 1.1 | 1 |
| Sofia Klein | 0.14 | 1.0 | 1 |

Reps whose buyers view more also tend to click the activity panel more — but this doesn't mean checking causes engagement. More likely: reps who send better quotes (generating more buyer views) are also the ones who try to use every available signal. The tool doesn't reward them for checking; they check despite it being broken.

---

## Updated Key Takeaways

6. **Senior reps check the activity panel 3.5x more than juniors** (0.53 vs 0.15 ratio), but not because it works — because they've learned to triangulate around unreliable data.
7. **Deals where the rep checks close at a 20-point higher rate** (66.7% vs 46.9%), but the relationship is likely confounded by rep quality, not caused by the check itself.
8. **The activity panel's biggest failure is with junior reps**: they check least, trust it most when they do check, and have the lowest win rate. The tool should be most helpful to them but is most harmful.
