# Mobile Push Notifications for Deal Updates

**Owner:** Lina K. (PM, Mobile)
**Status:** Draft for Kalina review
**Last updated:** 2026-04-12

---

## 1. Problem

Reps using the Teamleader Focus mobile app don't get real-time updates about activity on their deals. They have to open the app proactively to check. Reps have asked for push notifications repeatedly in roadmap sessions and through Sales feedback.

This means reps miss timely follow-up windows when prospects engage with quotes, accept meetings, or update account info — and we lose deals to slower response times than competitors with push as baseline.

We're prioritizing this now over the deal-scoring revamp because mobile activation is upstream of every other engagement signal we'd build later. Without active mobile usage, no scoring or routing improvement compounds. The deal-scoring revamp moves to Q4 to make room.

## 2. Users

**Mid-market AEs** (3-10 person sales teams) are the primary user. They run from meeting to meeting and don't have time to keep checking the desktop app or refreshing pipeline.

**SMB reps** are a secondary user. They use mobile heavily because they're often in the field.

Both segments make up roughly 80% of the active mobile user base based on Q1 mobile-app usage data.

## 3. Success — what changes in the world

Improving engagement on the mobile app is the goal. Reps will check Teamleader more frequently and act on signals faster.

**Direct success metrics:** Better mobile usage and faster response times on key actions.

**Time horizon:** Within Q3.

## 4. The decision — what we're building

We're building push notifications for deal updates on iOS and Android.

We could go with email, push, or both — push is more immediate but email is more discoverable in a busy day. We might consider supporting both channels and letting users choose, depending on what's easier to ship.

## 5. The MVP line

**MVP includes:** Push notifications for high-priority deal events.

We can extend the trigger list and configuration options later as we learn what reps want.

## 6. Risks and assumptions

The main risk is that reps mute the notifications if they get too many. We assume push is preferred over email for time-sensitive updates.

## 7. Cross-functional impact

Engineering will need to integrate with the iOS and Android push notification SDKs. Design will need to specify the notification copy and visual style.

## 8. Rollout

Launch to all mobile app users in Q3. We'll monitor opt-out rates after launch.

---

## Appendix: end-to-end walk — a Tuesday morning for an SMB rep

I walked through this scenario with Sara, an SMB AE based in Utrecht, using her actual phone and pipeline.

She's at a client breakfast at 8:30am and her phone is in her pocket. While she's pouring coffee, a quote she sent last week is opened by a prospect. She doesn't know.

She gets back in the car at 9:45 and drives to her next meeting. Doesn't open Teamleader during the drive.

She gets to her desk at 1pm, checks pipeline, sees the prospect opened the quote at 9:15am — but by that time the prospect has been on a discovery call with Pipedrive's sales team.

If Sara had been notified at 9:15, she could have called the prospect during her drive. That's the workflow this is trying to support.

This pattern is consistent across the SMB reps I've shadowed in the last six weeks — meeting-heavy mornings, desk-time afternoons, mobile-first engagement check-ins. The current desktop-first design assumes a workflow that doesn't match how field reps actually spend their day.
