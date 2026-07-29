# Python Learning Roadmap
*Built for the Claude Corps fellowship transcribe/translate app project*

## Overview
This roadmap takes you from zero Python knowledge to being ready to build a real project: a web app that accepts an uploaded mp3/mp4 (or link), transcribes it with timestamps, and translates it into any language. Each phase builds the specific skills needed for that project, and each phase ends with a mini-project checkpoint that's a rough preview of a piece of the real app. Phase 5 is the real build itself.

Format note: work through each phase using a mix of formats (video for concepts, hands-on practice as you go) rather than heavy reading — that's what keeps this sustainable.

---

## Phase 1: Fundamentals
**Topics & why they matter:**
- [ x ] Variables & data types — the basic building blocks everything else is written with
- [ x ] Conditionals (if/elif/else) — needed anywhere the app has to make a decision, like checking file type on upload
- [ x ] Loops (for/while) — needed for processing things like transcript segments one at a time
- [ x ] Functions — lets you organize transcribe/translate logic into reusable, testable pieces
- [ x ] Lists, dictionaries, tuples — dictionaries especially, since transcript data (text + timestamps) naturally fits this structure

**Resources:**
- Video/code-along: freeCodeCamp's full Python course on YouTube
- Hands-on: small interactive exercises as you go (Codewars, or just writing tiny scripts)

**Checkpoint — "Text Processor":**
Build a script that takes a block of text (simulating a transcript) and:
- Loops through it line by line
- Counts words per line
- Flags any line over a certain length
- Stores results in a dictionary (line number → word count)

- [ x ]

## Phase 2: Data & Files
**Topics & why they matter:**
- [  ] Reading/writing files — needed to handle the uploaded file or output transcript
- [  ] The `json` module — your existing JSON knowledge transfers directly; transcript output will likely be structured as JSON
- [  ] Error handling (try/except) — critical once you're relying on external services (Whisper, translation) that can fail
- [  ] Virtual environments & pip — needed before installing Whisper or any library

**Checkpoint — "File-Based Transcript Reader":**
Read a plain text file line-by-line, convert it into a dictionary keyed by line number, and write the result out as a JSON file.

---

## Phase 3: APIs & External Tools
**Topics & why they matter:**
- [  ] The `requests` library — how you'll call a translation API
- [  ] Handling API responses — parsing what Whisper/translation services send back
- [  ] Environment variables — keeping API keys out of your code (matters if this ends up public for the fellowship)

**Checkpoint — "Mini Translator Call":**
Using `requests`, call a free translation API (e.g., a public LibreTranslate instance) with a short hardcoded sentence, print the translated result, and include try/except for when the call fails.

---

## Phase 4: Web Basics
**Topics & why they matter:**
- [ ] Flask fundamentals — pairs naturally with your HTML/CSS background for the actual site
- [ ] Routing & handling file uploads — directly needed since users upload audio/video files

**Checkpoint — "Upload & Display":**
A tiny Flask app with one route that lets you upload a text file and displays its contents back on the page — the skeleton of the real upload flow.

---

## Phase 5: The Real Build
This phase has no new topics — it's where Phases 1-4 combine into the actual project.

**Main Project: Transcribe & Translate App**
- [ ] Accept an uploaded mp3/mp4 file or link (Phase 4 skills)
- [ ] Run it through Whisper for transcription with timestamps (Phase 2/3 skills)
- [ ] Store the transcript as structured JSON (Phase 1/2 skills)
- [ ] Offer translation into any language via a translation API (Phase 3 skills)
- [ ] Display results on a simple, recruiter-friendly site (Phase 4 skills)

---

## Progress Tracker
- [ ] Phase 1 complete
- [ ] Phase 2 complete
- [ ] Phase 3 complete
- [ ] Phase 4 complete
- [ ] Phase 5 / Main project complete

---

## Diligence Statement

In creating this Python Learning Roadmap, I collaborated with Claude (Anthropic) to assist with skills scoping, sequencing course topics into a learnable progression, researching and shortlisting learning resources, designing practice checkpoints tied to a real project, and formatting the final document.

Throughout this process, I directed the collaboration deliberately: I set the vision and success criteria for the project, made judgment calls on scope and priority based on my own learning style and goals, selected which resource formats fit how I learn, and evaluated each phase of the roadmap before accepting it — refining the sequencing, checkpoint design, and document structure through iterative feedback rather than accepting AI output as-is.

No sensitive personal or third-party data was shared with the AI in this process; only my own stated learning background, preferences, and the public-facing concept of the related project (an audio transcription and translation tool) were discussed.

I affirm that all AI-assisted content underwent review by me at each stage, and the final roadmap reflects my own understanding, priorities, and intended approach to learning Python. While Claude's research and structuring assistance were instrumental in producing this document, I take full responsibility for its content, its accuracy, and its use going forward — including as a reference point in my own learning and, potentially, in professional contexts such as a fellowship application. This disclosure is made in the spirit of transparency, consistent with the diligence practices outlined in this course.
