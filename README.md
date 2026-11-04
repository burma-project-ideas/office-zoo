# Office Zoo public deployment copy

Source: https://office-zoo.vercel.app/
Captured: 2026-11-04

## Run locally

Open PowerShell in this folder and run:

    python -m http.server 8080 --directory site

Then open http://localhost:8080 . Use an HTTP server; opening index.html directly is insufficient for JavaScript modules.

## Contents

- site/: original published HTML, JavaScript, CSS, card images, avatars and icons.
- data/: readable JSON extracted from the published JavaScript.
- data/bundled-constants.json: additional original data constants, retaining their deployed variable names. mi contains relationship narratives; xf contains animal guidance; ka contains bilingual UI text; other constants contain additional supporting copy.
- data/scoring-original.js: original question and scoring section, for reference; depends on traits and animals defined in the main bundle.
- manifest.json: downloaded URLs, sizes and SHA-256 checksums.
- WORKFLOW.md: observed workflow and scoring logic from the deployed code.

## Limits

This is a copy of the public deployment, not the original development repository. Original React source files, package manifests, Git history, private databases, secrets and CI/CD workflows cannot be recovered from this URL. The original minified bundle is preserved and can run without rebuilding.

Personal quiz results and participant information live in the original browser's localStorage; they are not supplied by the URL and are not included. The local copy starts with its own browser storage. Google Fonts and Vercel analytics still reference external services, so this is not a fully offline archive. No live quizzes or personal submissions were made. No source license was visible in the fetched HTML; verify reuse rights before publishing.
