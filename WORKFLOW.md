# Application workflow

Office Zoo by Harry Hein: user journeys, scoring, and browser storage behavior.

1. Landing page: browse eight animal cards; choose self assessment or assessment of another person. Switch English/Myanmar and light/dark theme.
2. Animal detail: read overview, six trait metrics, strengths, watchouts and guidance. Compare the animal with any of the eight types. A shared URL with ?sign=bee (or another animal ID) opens that detail page.
3. Quiz: 24 workplace scenarios, five options each. Self mode uses self wording; other mode uses other wording in Myanmar. English uses the shared question wording. Keys A/S/D/F/Space correspond to the five options. Answers map to animal IDs.
4. Participant step: optional name and job, consent, then completion. The completion handler has no active participant upload; it retains state locally.
5. Calculating screen: three-second transition to a self result or pair result.
6. Self result: winning animal, trait profile and guidance. Restart the quiz, assess a colleague, or compare with another type.
7. Assess another: requires your own type first; users may take their own quiz or pick a type directly. Another-person quiz leads to a pair comparison.
8. Pair/team comparison: fit percentage, verdict, relationship summary, complementary strengths, clashes, dos and donts, trait overlay. Add/remove comparison animals and optional names/jobs. Export a Markdown team profile. Sharing opens external share destinations.

## Scoring

Six dimensions: people, pace, assertiveness, analysis, visibility, adaptability. Compute each animal trait vector relative to the mean of all eight animals. Weight an answer inversely by the total frequency of its animal across all available answer options. Sum weighted centered trait vectors across answers; project onto each animal's normalized centered vector. Highest projection wins, with ties resolved by the fixed animal order. A secondary animal is shown when its gap from first is at most 12% of the full score range. See scoring-original.js for the exact scoring logic.

Compatibility is a fixed symmetric table of 36 unordered pairs including same-type pairs; a missing entry defaults to 50. Verdict thresholds: >=80 Near-perfect, >=65 Strong, >=50 Workable, >=40 Tense, otherwise High friction.

## Storage and services

Local storage includes zoo-my-animal, zoo-my-scores, zoo-participant, zoo-theme and the language preference key preserved in the bundle. Quiz answers are component state during a run. Google Fonts provides Figtree and Padauk. Vercel analytics receives client-side analytics events when available. The app runs from its frontend bundle.
