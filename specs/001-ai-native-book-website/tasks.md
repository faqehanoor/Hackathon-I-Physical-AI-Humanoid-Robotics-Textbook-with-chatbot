# Tasks: AI-Native Textbook

**Input**: Design documents from `/specs/001-ai-native-book-website/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: The feature specification does not explicitly request tests to be written first, but manual testing is mentioned in the constitution. I will focus on implementation tasks, with consideration for eventual testing.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below assume this web app structure.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize Docusaurus project in `frontend/`
- [ ] T002 Configure Docusaurus v3 with React + TSX in `frontend/`
- [ ] T003 Initialize Python project for FastAPI backend in `backend/`
- [ ] T004 Install primary backend dependencies (FastAPI, uvicorn, etc.) in `backend/`
- [ ] T005 [P] Configure linting and formatting for frontend (ESLint, Prettier) in `frontend/`
- [ ] T006 [P] Configure linting and formatting for backend (Flake8, Black, isort) in `backend/`
- [ ] T007 Create initial `.gitignore` in repository root, including `node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `.env*`
- [ ] T008 [P] Create `frontend/static/img/` directory for images

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T009 Setup Neon Serverless Postgres connection and base configuration in `backend/src/db/`
- [ ] T010 Implement Better-Auth for signup/signin in `backend/src/services/auth_service.py`
- [ ] T011 Create initial user data models for Better-Auth in `backend/src/models/user.py`
- [ ] T012 Implement user background questionnaire fields (software/hardware) in `backend/src/models/user.py` and `backend/src/api/auth.py`
- [ ] T013 Setup Qdrant Cloud client and basic vector collection management in `backend/src/services/qdrant_service.py`
- [ ] T014 Configure FastEmbed for local embeddings in `backend/src/services/embedding_service.py`
- [ ] T015 Setup environment variable management for sensitive credentials (`.env` files) in `backend/` and `frontend/`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Read Textbook Content (Priority: P1) 🎯 MVP

**Goal**: Learners can access and read textbook chapters online.

**Independent Test**: A user can navigate to the book, select a chapter (e.g., ROS 2), and view its content.

### Implementation for User Story 1

- [ ] T016 [P] [US1] Create Docusaurus `Home` page in `frontend/src/pages/index.tsx`
- [ ] T017 [P] [US1] Create Docusaurus `Book` page in `frontend/src/pages/book.tsx`
- [ ] T018 [US1] Implement Docusaurus sidebar configuration for chapters in `frontend/docusaurus.config.js`
- [ ] T019 [P] [US1] Create placeholder MDX files for ROS 2 chapter in `frontend/docs/ros2/index.mdx`
- [ ] T020 [P] [US1] Create placeholder MDX files for Gazebo chapter in `frontend/docs/gazebo/index.mdx`
- [ ] T021 [P] [US1] Create placeholder MDX files for Unity chapter in `frontend/docs/unity/index.mdx`
- [ ] T022 [P] [US1] Create placeholder MDX files for NVIDIA Isaac chapter in `frontend/docs/nvidia-isaac/index.mdx`
- [ ] T023 [P] [US1] Create placeholder MDX files for VLA chapter in `frontend/docs/vla/index.mdx`
- [ ] T024 [P] [US1] Create placeholder MDX files for SLAM chapter in `frontend/docs/slam/index.mdx`
- [ ] T025 [P] [US1] Create placeholder MDX files for Humanoid kinematics chapter in `frontend/docs/humanoid-kinematics/index.mdx`
- [ ] T026 [P] [US1] Create placeholder MDX files for Conversational Robotics chapter in `frontend/docs/conversational-robotics/index.mdx`
- [ ] T027 [P] [US1] Create placeholder MDX files for Capstone Project chapter in `frontend/docs/capstone-project/index.mdx`
- [ ] T028 [US1] Apply custom dark theme (black background, white text) in `frontend/src/theme/custom.css`
- [ ] T029 [US1] Ensure all images are correctly referenced and stored in `frontend/static/img/` within the Docusaurus content

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Interact with RAG Chatbot (Priority: P1)

**Goal**: Learners can use an integrated RAG chatbot to ask questions and receive cited answers.

**Independent Test**: A user can ask a question related to a chapter, and the chatbot provides a relevant answer with correct paragraph citations.

### Implementation for User Story 2

- [ ] T030 [US2] Implement backend API endpoint for RAG queries in `backend/src/api/rag.py`
- [ ] T031 [US2] Integrate OpenAI Agents/ChatKit SDK for RAG inference in `backend/src/services/rag_service.py`
- [ ] T032 [US2] Implement embedding generation and storage (Qdrant) logic for book content updates in `backend/src/services/embedding_update_service.py`
- [ ] T033 [P] [US2] Create an admin video upload endpoint in `backend/src/api/admin.py`
- [ ] T034 [P] [US2] Develop frontend RAG chatbot UI component in `frontend/src/components/RAGChatbot.tsx`
- [ ] T035 [US2] Integrate chatbot component into Docusaurus layout (e.g., global sidebar or per-chapter) in `frontend/src/theme/Layout/index.tsx`
- [ ] T036 [US2] Implement client-side logic for sending questions and displaying answers with paragraph ID citations in `frontend/src/services/rag_client.ts`
- [ ] T037 [US2] Implement linking/scrolling to cited paragraph IDs in Docusaurus content from chatbot responses in `frontend/src/services/citation_navigator.ts`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Navigate Chapters (Priority: P2)

**Goal**: Learners can easily navigate between chapters and topics.

**Independent Test**: A user can move from one chapter to the next and back using navigation controls.

### Implementation for User Story 3

- [ ] T038 [US3] Enhance Docusaurus sidebar navigation for better chapter organization in `frontend/docusaurus.config.js`
- [ ] T039 [P] [US3] Implement "Next Chapter" and "Previous Chapter" navigation buttons within chapter content in `frontend/src/components/ChapterNavigation.tsx`
- [ ] T040 [US3] Ensure mobile responsiveness for chapter navigation components in `frontend/src/theme/styles/mobile.css`

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T041 Code cleanup and refactoring across frontend and backend
- [ ] T042 Performance optimization for Docusaurus build and initial load in `frontend/docusaurus.config.js`
- [ ] T043 Performance optimization for backend API response times in `backend/src/api/`
- [ ] T044 Security hardening for authentication and API endpoints
- [ ] T045 Final review of `frontend/static/img/` usage and optimization
- [ ] T046 Ensure total frontend bundle size remains under 150KB (without images)
- [ ] T047 Verify deployment configurations for Vercel and Render/Railway
- [ ] T048 Create ADR for the chapter count discrepancy (if not already done) in `history/adr/chapter-count-discrepancy.md`
- [ ] T049 Update agent context with new technology (`.specify/scripts/bash/update-agent-context.sh claude`)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Many frontend component tasks within a story can be developed in parallel
- Backend API endpoints and related services can be developed in parallel (if careful with shared models/services)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Frontend setup within US1
Task: "Create Docusaurus `Home` page in frontend/src/pages/index.tsx"
Task: "Create Docusaurus `Book` page in frontend/src/pages/book.tsx"
# ... (other frontend content/page tasks)

# Creating multiple chapter placeholder files
Task: "Create placeholder MDX files for ROS 2 chapter in frontend/docs/ros2/index.mdx"
Task: "Create placeholder MDX files for Gazebo chapter in frontend/docs/gazebo/index.mdx"
# ... (other chapter placeholder tasks)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Frontend Docusaurus content/structure)
   - Developer B: User Story 2 (Backend RAG chatbot + Frontend integration)
   - Developer C: User Story 3 (Frontend navigation enhancements)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
