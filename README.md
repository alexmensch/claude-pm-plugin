# Software Development Life Cycle (SDLC) Plugins for Claude Code

A collection of Claude Code plugins for product managers and developers who want structured, disciplined workflows across the full product lifecycle — from defining an idea, to planning what to build next, to shipping it, assessing compliance, and marketing it.

## Installation

Add this repository as a plugin marketplace, then install the plugins you want:

```
/plugin marketplace add alexmensch/claude-sdlc-plugins
/plugin install feature-definition@claude-sdlc-plugins
/plugin install feature-development@claude-sdlc-plugins
/plugin install roadmap@claude-sdlc-plugins
/plugin install debugging@claude-sdlc-plugins
/plugin install documentation@claude-sdlc-plugins
/plugin install legal@claude-sdlc-plugins
/plugin install marketing@claude-sdlc-plugins
```

## Plugins

### feature-definition

**Skills:** `define-feature`

Define a feature precisely before building it. Takes any unstructured idea — a sentence, a rough description, a half-formed thought — and turns it into a clean requirements table through structured brainstorming.

Invoke it with `/define-feature` inside Claude Code and describe what you want to build. The skill acts as a sparring partner: it challenges whether the feature is necessary, surfaces edge cases you may not have considered, questions whether the proposed approach is the right one, and pushes back on anything vague or speculative. The goal is to arrive at the best outcome for users, not just to rubber-stamp ideas.

The output is a Markdown requirements file saved to `requirements/` and ready to be passed directly to the `new-feature` skill in the `feature-development` plugin. When it is, `new-feature` will have no clarifying questions — the feature is already fully defined.

#### When to use this

Use `define-feature` before `new-feature` when:

- The feature idea is still rough or unvalidated
- You want a second perspective before committing to implementation
- You want to ensure edge cases and scope are explicit before writing a technical spec

---

### feature-development

**Skills:** `new-feature`, `pull-request`, `semver`

Build new product features with a strict development workflow anchored on test-driven acceptance and disciplined coding practices.

Invoke it with `/new-feature` inside Claude Code and pass it a requirements file or describe the feature in chat. The plugin orchestrates the entire process end-to-end using three specialised agents:

- **technical-spec** — Analyses the existing codebase in depth, produces a structured technical specification with acceptance criteria and edge cases, and confirms it with you before any code is written.
- **test-writer** — Takes the approved spec and writes comprehensive tests covering all acceptance criteria and edge cases. Runs in the background in an isolated worktree so tests and implementation happen in parallel.
- **code-reviewer** — Reviews all branch changes before a PR is opened. Checks for DRY violations, unnecessary complexity, duplicated patterns, and unnecessary dependencies. Presents findings for your approval before committing fixes.

#### Workflow

1. A new branch is created from the default branch.
2. You provide a requirements file or describe the feature in chat. The plugin clarifies any ambiguity, then hands the requirements to **technical-spec** which produces a detailed spec for your approval.
3. Once the spec is approved, **test-writer** starts writing tests in the background while implementation code is written in parallel against the same spec.
4. Tests are merged in and the full suite is run. Test failures are treated as implementation bugs, not test bugs — tests are never changed without your confirmation.
5. **code-reviewer** reviews all changes and presents findings. You decide which fixes to apply.
6. Linting, build verification, documentation updates, and semver versioning are handled.
7. You are prompted to commit and open a PR.
8. If a `requirements/ROADMAP.md` exists, the shipped feature is automatically moved from the planned table to the shipped table with the PR number recorded.

---

### roadmap

**Skills:** `plan-roadmap`, `communicate-roadmap`

Organise defined feature requirements into a sequenced, release-grouped plan, and communicate it in language that speaks to users rather than engineers.

#### plan-roadmap

Invoke it with `/plan-roadmap` inside Claude Code. The skill reads all requirements files in `requirements/` and helps you think through how to sequence and group them into coherent releases. It acts as a planning partner, not an order-taker: it challenges groupings that don't tell a coherent story, asks about technical dependencies, and ensures that each release delivers real incremental value to the user.

The output is `requirements/ROADMAP.md`, which contains:

- An **overview** written for a fresh LLM context — capturing the rationale and principles behind the sequencing so any future planning session can load it quickly
- A **planned table** grouped into named releases, with global sequence numbers, links to requirements files, and GUIDs
- A **shipped table** listing released features with their PR numbers

This file is also updated automatically by `new-feature` when a feature ships.

#### communicate-roadmap

Invoke it with `/communicate-roadmap` inside Claude Code. The skill reads `requirements/ROADMAP.md` and the referenced requirements files, then writes `requirements/EXTERNAL-ROADMAP.md` — a user-facing document that describes what is coming in terms of problems solved and outcomes delivered, not features built.

The voice is user-benefit first: every sentence answers "so what?" from the perspective of someone who uses the product.

#### What the roadmap plugin does not do

- It does not create or modify requirements files. Use `define-feature` for that.
- It does not implement features. Use `new-feature` for that.
- If planning surfaces an incompatibility between requirements, it flags it and directs you back to `define-feature` to resolve it.

---

### debugging

**Skills:** `blame`

Investigate code and trace changes back through the development history to their original requirements.

#### blame

Invoke it with `/blame` inside Claude Code. The skill asks for a file, whether to scope to specific lines or examine the whole file, and how far back to trace (just the last change per line, or the full commit history). It then follows a strict chain of custody:

`git blame` → commit hash → PR → requirements GUID → spec file

The output is a structured chain-of-custody table for each unique commit found. Where the chain is complete, the original requirement text is surfaced directly. Where a link is broken — a direct push with no PR, a PR with no requirements reference, a GUID with no matching spec file — the trace shows how far it reached and explains exactly what is missing.

---

### documentation

**Skills:** `write-changelog`

Write brief, user-facing changelog entries from PRs or requirements files.

#### write-changelog

Invoke it with `/write-changelog` inside Claude Code and provide one or more PR IDs or requirements file paths. The skill resolves each PR to its requirements GUID, reads the corresponding spec file for context, and writes a concise changelog entry in a consistent house style.

Each entry contains a title, date, and 2–4 sentences of prose that describe what changed and why it matters — written entirely from the user's perspective, with no implementation details. The embedded style guide enforces a consistent voice: confident, direct, and brief.

After presenting the entry, the skill asks whether you want it saved to disk as a Markdown file or if you're done.

---

### legal

**Skills:** `search-trademark`, `assess-compliance`

Research trademark conflicts and assess regulatory compliance for software products. The legal plugin helps you make informed decisions about naming and regulatory obligations — it provides research and analysis, not legal advice.

#### search-trademark

Invoke it with `/search-trademark` inside Claude Code and provide a proposed product or marketing name along with what the product does and the market it operates in. The skill invokes a research agent that searches trademark registries (USPTO, EUIPO, WIPO), existing products and brands, domain availability, SEO competition for the name, and linguistic/cultural concerns.

The output is a structured report covering trademark registry findings, existing products and brands using the same or similar names, an SEO assessment of how hard it would be to own the name in search results, and an overall risk assessment (low/moderate/high). The skill then offers to brainstorm and research alternative names if the original has significant conflicts.

#### assess-compliance

Invoke it with `/assess-compliance` inside Claude Code. The skill scans the codebase for data-handling patterns (authentication, database schemas, third-party integrations, logging), reads product strategy and roadmap documents for context, asks clarifying questions about user geography and data types, then invokes a research agent to investigate applicable regulations.

The output is a unified compliance report covering all applicable frameworks — GDPR, ePrivacy, EU AI Act, CCPA/CPRA, US state privacy laws, CAN-SPAM, COPPA, accessibility requirements, SOC 2, PCI DSS, and others identified during research. HIPAA is excluded by design. For each framework, the report presents three compliance levels (minimum viable, pragmatic, full) with honest trade-offs, enforcement context, and effort estimates so you can make informed decisions about where to invest.

---

### marketing

**Skills:** `build-marketing-site`, `build-landing-page`, `evaluate-seo`

Build user-focused marketing websites and landing pages, and evaluate SEO/GEO performance. The marketing plugin reads your product's strategy, roadmap, requirements, and codebase to generate compelling pages that talk about what the user gets — not what the product does.

#### build-marketing-site

Invoke it with `/build-marketing-site` inside Claude Code. The skill gathers context from your strategy, roadmap, requirements files, README, and codebase, then proposes a site structure (typically a single landing page). It auto-detects the project's framework (Next.js, Astro, Hugo, etc.) and generates pages accordingly, or falls back to standalone static HTML if no framework is found.

The skill writes copy first and presents it for your approval before generating any code. Every sentence is tested against the question: "does this tell the reader something about their experience, or something about our technology?" Buzzwords are banned — every claim must be specific and concrete. After the site is generated, the skill offers to run `evaluate-seo` for search optimisation recommendations.

#### build-landing-page

Invoke it with `/build-landing-page` inside Claude Code and describe the page's purpose — a product comparison, a migration guide, a specific use case, or a campaign page. The skill follows the same user-focused principles as `build-marketing-site` but with a narrower scope: each landing page has one clear purpose and one clear action for the reader.

For comparison pages, the skill takes a fair approach: it includes areas where the alternative is genuinely stronger, because honest comparisons build trust and perform better in search. For migration guides, it focuses on reducing the reader's anxiety about switching by being specific about what migration involves. The skill matches the style of any existing marketing site if one exists.

#### evaluate-seo

Invoke it with `/evaluate-seo` inside Claude Code. The skill can also be invoked automatically by `build-marketing-site` and `build-landing-page` after page generation. It evaluates pages for both traditional SEO and GEO (Generative Engine Optimisation — how content performs in AI-powered search engines like Google AI Overviews, Perplexity, and similar).

The skill researches the competitive search landscape for your product's terms, analyses content quality and technical SEO, assesses GEO-specific factors (structured extractable answers, specificity, authoritative framing), and delivers 5–10 prioritised recommendations ranked by expected impact. It can implement changes directly, let you pick which recommendations to apply, or save the evaluation as a report.

---

## Naming conventions

Plugins and skills follow distinct naming conventions because they serve different purposes:

- **Plugins** are installation and grouping units. Their names are **nouns or noun phrases** that describe a domain or workflow phase (`feature-definition`, `feature-development`, `roadmap`). Users install plugins once; the name is organisational metadata.
- **Skills** are invocable actions within a plugin. Their names are **verb phrases** that describe what they do (`define-feature`, `new-feature`, `plan-roadmap`, `communicate-roadmap`). Users invoke skills by name in conversation; clarity here matters most.

A plugin name and a skill name should never be the same, even when a plugin contains only one skill. This keeps the hierarchy unambiguous as plugins grow.

## License

[CC BY 4.0](LICENSE)
