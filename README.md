# Office Zoo

Office Zoo is a workplace personality quiz that helps people explore how they work and how they relate to colleagues. Answer 24 workplace scenarios to discover one of eight animal archetypes, read your trait profile, and compare working styles with others.

The app supports English and Myanmar, light and dark themes, shareable animal profiles, and Markdown exports of team comparisons.

**Office Zoo is a project by Harry Hein**, included here for learning and inspiration. Explore the [live app](https://office-zoo.vercel.app/) to see the experience in action.

## Overview

The eight archetypes are Bee, Hippo, Leopard, Peacock, Snake, Bull, Owl, and Sloth. Each profile describes strengths, watchouts, and working guidance across six traits:

- People focus
- Pace / speed
- Assertiveness
- Analysis
- Visibility
- Adaptability

Users can browse profiles directly, take a self assessment, assess another person, or compare multiple animal types. Comparisons include fit percentages, complementary strengths, potential clashes, and practical dos and don'ts.

## Run locally

Install Python 3, open PowerShell in the repository folder, and run:

```powershell
python -m http.server 8080 --bind 127.0.0.1 --directory site
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser. Keep the terminal running while using the app; press `Ctrl+C` to stop the server.

No dependency installation or build step is required to run the app. Serve the `site` directory over HTTP because opening `index.html` directly does not reliably load JavaScript modules.

## User workflow

### Discover your animal

1. Open the landing page and choose the self assessment.
2. Answer 24 workplace scenarios, each with five possible responses. You can select options with the mouse or use `A`, `S`, `D`, `F`, and `Space`.
3. Complete the participant step with optional name and job details and a consent choice.
4. After a three-second calculating screen, view your animal result, trait profile, and working guidance.
5. Restart the quiz, browse another animal, or continue to a colleague comparison.

### Explore animal profiles

Select any animal on the landing page to read its overview, strengths, watchouts, and trait metrics without taking the quiz. From the detail page, select another animal to compare working styles.

A shared link such as [/?sign=bee](https://office-zoo.vercel.app/?sign=bee) opens that animal's detail page. The same query parameter works on the local server.

### Assess and compare colleagues

1. Choose the assessment of another person. If your own type is not set, take your self assessment or pick your type directly first.
2. Answer the workplace scenarios for the other person, then complete the participant step.
3. Review the pair result: compatibility percentage, relationship summary, complementary strengths, clashes, and recommended actions.
4. Add more animal types to the comparison, optionally enter names and job titles, and inspect the trait overlay.
5. Export the team profile as Markdown or use the available sharing actions.

English uses shared scenario wording; Myanmar provides separate self and other-person wording.

## How results work

Quiz options map to animal archetypes. The scoring logic weights answers to account for how often each animal appears among the options, combines their six-trait vectors, and selects the closest matching animal by its projection score. Ties follow the fixed animal order.

Compatibility percentages come from a fixed table of 36 unordered animal pairs, including same-type pairs. They are separate from quiz scoring. Verdicts range from **High friction** to **Near-perfect**.

See [WORKFLOW.md](WORKFLOW.md) for scoring details, state transitions, and storage behavior. The question and scoring reference code is in [data/scoring-original.js](data/scoring-original.js).

## Repository contents

| Path | Purpose |
| --- | --- |
| `site/` | App HTML, JavaScript, CSS, cards, avatars, and icons |
| `data/animals.json` | Eight animal profiles, traits, strengths, and watchouts |
| `data/animalOrder.json` | Animal ordering used by the app |
| `data/questions.json` | All 24 questions and their answer options |
| `data/traits.json` | Trait labels and dimensions |
| `data/compatibilityScores.json` | The 36 compatibility scores |
| `data/bundled-constants.json` | Additional app constants, including bilingual text and relationship narratives |
| `data/scoring-original.js` | Question and scoring reference |
| `manifest.json` | Asset URLs, file sizes, and SHA-256 checksums |
| `WORKFLOW.md` | Detailed application workflow and scoring notes |

In `bundled-constants.json`, `mi` holds relationship narratives, `xf` holds animal guidance, and `ka` holds bilingual UI text. These use the variable names in the app bundle. The scoring reference depends on definitions in the main bundle and is not a standalone script.

## Data and runtime notes

Results, participant details, theme, and language preferences are stored in the browser's local storage for each origin. In-progress quiz answers live in component state. The participant completion handler has no active participant upload.

Google Fonts and Vercel analytics use external services, so full offline operation is not supported. The app runs from the JavaScript bundle in `site/assets/`. Editing JSON files in `data/` does not update the running app, and this repository does not include a source rebuild pipeline.

## Credits

Project by **Harry Hein**. Kept as a reference for others to learn from and find inspiration in its workplace quiz, bilingual experience, and team comparison workflow.
