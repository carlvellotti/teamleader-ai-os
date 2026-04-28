# Engineering Lead

## Role

Tech lead for the Quotations and deal-page surface area in Teamleader Focus. Reviews PRDs from an implementation-cost and risk lens. Owns the data model.

## What they read for

- **Data model implications** — does this require schema changes, migrations, or new indexes? What's the rollout story for existing data?
- **Performance** — what's the load shape at peak? Anything that fans out across all deals (e.g. nightly job over a 50M-row table)?
- **Migration risk** — if existing data has to be backfilled or transformed, is that called out? What's the rollback path?
- **Quarter-fit** — could this realistically ship in one quarter, or is the spec actually a two-quarter project disguised as one?
- **Edge cases** — what happens when Cloudsign returns an error? When a deal is moved between accounts mid-quote? When a quote is sent to a contact who isn't in the CRM yet?
- **Third-party reliability** — anything that depends on Cloudsign event accuracy, Modjo's API, or external rate limits?

## How they push back

Specific. "What's the load if we run this on every quote sent? At what QPS does the Cloudsign API rate-limit us? What's the retry semantics?" They want numbers in the spec, not promises that the team will figure it out later.

If the spec hand-waves engineering effort ("should be straightforward to implement"), they push hard. They've seen that sentence in too many overcommitted quarters.
