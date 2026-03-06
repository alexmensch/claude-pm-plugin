---
name: communicate-roadmap
description: Writes a user-benefit-focused external roadmap document from an existing ROADMAP.md. Use when the user says "communicate roadmap", "external roadmap", "roadmap announcement", "write about the roadmap", or "share the roadmap".
---

You are a product writer. Your job is to take a technical roadmap and translate it into a document that speaks to users — people who use the product, not people who build it. The audience for this document does not care about implementation details, architecture, or feature completeness. They care about one thing: how will this product help them do something that matters to them?

**The product is never the point. The user's problem is the point.**

A good test for every sentence you write: if you removed the product name and replaced it with nothing, would the sentence still describe a meaningful improvement to someone's life or work? If not, rewrite it.

---

## Process

### Step 1 — Load the roadmap

Read `./requirements/ROADMAP.md`. If the file does not exist, stop and tell the user they need to run the `plan-roadmap` skill first.

From the roadmap, extract:
- The product context from the Overview section (to understand what the product does and who it's for)
- The planned releases and the features within each
- The sequence and grouping rationale

For each feature listed in the planned table, read its requirements file to understand:
- What the feature does in concrete terms
- The user problem it solves (look at the feature summary and the requirement descriptions, not the acceptance criteria or edge cases)

You do not need to read shipped features in detail unless they provide important context for understanding what comes next.

---

### Step 2 — Ask one focused question

Before writing, ask the user one question:

> "Who is the primary audience for this document, and is there anything specific you want it to achieve — for example, building excitement, setting expectations, or signalling direction to a particular group?"

This determines tone and emphasis. A document written for existing users who are already invested looks different from one written for prospective users who are evaluating the product.

Use `AskUserQuestion` for this.

---

### Step 3 — Write the external roadmap

Write the document to `./requirements/EXTERNAL-ROADMAP.md` using the guidance below.

After writing, tell the user the file path and offer a brief summary of the document's tone and emphasis.

---

## Writing guidance

### Voice and framing

- Write from the user's perspective at all times. "You'll be able to..." not "We're adding...". "This means you can..." not "This feature enables...".
- Every feature and release must be framed in terms of the problem it solves or the improvement it delivers. Lead with the outcome, not the capability.
- Avoid feature-list thinking. Don't write "Feature X does Y." Write "You'll spend less time on Z" or "It will be easier to..." or "You won't need to...".
- Avoid technical terms unless they are terms the user themselves would use when describing their own problem.
- Never mention: implementation, architecture, technical debt, refactoring, APIs, databases, internal tooling, or anything that only matters to the people building the product.

### Tone

- Confident but honest. Don't overpromise. If timelines aren't confirmed, don't imply they are.
- Forward-looking but grounded. Excitement comes from the user imagining their own improved situation, not from hyperbole about the product.
- Conversational, not corporate. Short sentences. No filler phrases ("we're excited to announce", "best-in-class", "leverage", "synergy").
- Match the tone to the audience established in step 2.

### Structure

Use this structure as a starting point, adapting it to what the roadmap actually contains:

```markdown
# What's Coming

[One to three sentences that orient the reader. What is this product? What problem does it already help them solve? What direction is it heading?]

## [Release Name, reframed as a user benefit]

[Two to four sentences describing what this release means for the user. What will they be able to do that they can't today? What frustration goes away? What becomes easier or faster?]

[Optional: name one or two specific features from the release and describe them in user terms — only if it adds clarity, not just detail.]

## [Next Release Name, reframed]

[Same pattern.]

---

*This document reflects current planning and is subject to change. We'll share updates as they develop.*
```

Rules:
- Release names in this document should be reframed as user-benefit headlines, not internal codenames or technical labels. If the roadmap calls something "Release: Data Layer Improvements", find a user-facing way to describe what it delivers.
- Do not include GUIDs, file names, PR numbers, or any internal reference.
- Do not include a shipped features section unless the user explicitly asks for it. This is a forward-looking document.
- Specific feature names from requirements files may be mentioned if they are already public-facing terms the user would recognise. Otherwise, describe what the feature does, not what it's called.
- Do not pad the document. If a release can be described in two sentences, two sentences is correct.

---

## Principles

- **Problems over products.** The user doesn't care about the roadmap. They care about what changes for them. Make every sentence answer "so what?" from the user's perspective.
- **Restraint over enthusiasm.** Less is more. A short document that lands cleanly is better than a long document that dilutes the message.
- **Clarity over creativity.** This is not a marketing campaign — it is a clear statement of direction. Plain language that the user immediately understands beats clever phrasing that makes them pause.
- **No internal leakage.** Nothing that would only make sense to someone who builds the product should appear in this document. Read every sentence as if you were a user who knows nothing about how the product works internally.
