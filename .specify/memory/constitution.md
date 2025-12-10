<!--
Sync Impact Report:
Version change: 1.1.0 → 1.1.1 (PATCH: Clarification of existing principles)
Modified principles: Minor phrasing updates for clarity (e.g., "use" changed to "must use" or "must be").
Added sections: None
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending (review 'Constitution Check' section for alignment)
  - .specify/templates/spec-template.md: ⚠ pending (review 'Requirements' and 'Success Criteria' sections for alignment)
  - .specify/templates/tasks-template.md: ⚠ pending (review 'Task Generation Rules' and 'Phase Structure' for alignment)
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics Textbook Project Constitution

## Core Principles

### I. Code Quality
Clean, modular, readable. All React/Docusaurus components must use TSX, strict typing, and reusable patterns.

### II. Documentation Quality
All chapters must follow consistent structure: Overview → Concepts → Diagrams → Hands-on Labs → Assessments.

### III. AI-Native Design
Every chapter must be optimized for AI navigation, embedding, chunking, and RAG queries.

### IV. Testing
Every component must be tested manually for sidebar navigation, mobile responsiveness, and search.

### V. UX Consistency
Dark theme only (black background, white text). All images must be stored in frontend/static/img.

### VI. Performance
RAG queries must be <800ms, embeddings under 150 tokens/chunk, Qdrant vectors optimized using FastEmbed.

### VII. Accessibility
Large fonts, high contrast, readable on all devices.

### VIII. Data Privacy
Better-Auth must be used for signup/signin; user background questions stored in Neon Postgres.

### IX. Personalization
Logged-in users must be able to press a “Personalize Content” button at the start of each chapter.

### X. Urdu Translation
A one-click toggle must be available at the top of every chapter for English ↔ Urdu.

### XI. Extensibility
The project must support adding additional robotics modules later.

## Technical Standards

TypeScript strict mode: All TypeScript code must be written with `strict: true` enabled in `tsconfig.json`.
All components reusable: Components must be designed for reusability across the application, avoiding tight coupling and promoting modularity.
Chapter content in /content/chapters/: All book chapter MDX files must be stored in the `/content/chapters/` directory.
Total bundle size < 150KB (without images): The JavaScript bundle size for the entire application, excluding images, must remain under 150KB for optimal performance.

## Project Constraints

4 pages only: The website is limited to four main pages: Home, Book, About, and Contact.
Book = 5 chapters × 2 topics each: The book content will consist of 5 chapters, with each chapter containing 2 distinct topics.
Deploy on Vercel (free): The application must be deployable on Vercel's free tier.

## Governance
Constitution supersedes all other practices; Amendments require documentation, approval, migration plan.
All PRs/reviews must verify compliance; Complexity must be justified; Use CLAUDE.md for runtime development guidance.

**Version**: 1.1.1 | **Ratified**: 2025-12-03 | **Last Amended**: 2025-12-04
