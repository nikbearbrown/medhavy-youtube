# Medhavy — CLI Video Ideas ("X with Claude")

**Lane classification:** RESEARCH (Claude assistant) — Medhavy is an EdTech/AI-in-education book. Its topics are pedagogical frameworks, policy evidence synthesis, and instructional design decisions. No computable mathematical artifact. Cards use Claude as a research/synthesis partner, not a code runner.

## Candidate 01 — "Research the Performance-Learning Gap with Claude: What the Bastani Study Actually Shows"
- Source: medhavy/chapters/01-the-failure-that-looks-like-success.md
- Lane: RESEARCH (Claude assistant)
- Hook: Students who used unguarded GPT scored 48% higher during practice and 17 points lower on the exam — the gap between in-session performance and actual learning is measurable, and most institutions are tracking the wrong number.
- The artifact: A sourced 4-column comparison brief: Condition | In-session performance | Unassisted exam score | Mechanism — populated from the Bastani 2025 PNAS study plus the Bjork performance-learning distinction literature, rendered as an annotated slate for the video.
- Prompt seed: `claude "Research the Bastani 2025 PNAS study (doi: 10.1073/pnas.2422633122) on AI tutoring and math learning. Summarize: (1) the three experimental conditions and their in-session vs. exam outcomes, (2) the Bjork performance-learning distinction that explains the result, (3) the ASSISTments contrast case. Produce a 4-column comparison table and a 200-word synthesis. Flag any finding you cannot verify."`
- Read / check: Cross-check the 17-percentage-point exam gap and the 48% in-session improvement against the abstract; verify that the Bjork distinction (storage vs. retrieval strength) is attributed to 1992; confirm ASSISTments effect size (≈0.75 grade levels) is not overstated.
- Human supplies: Access to the Bastani 2025 PNAS paper (doi provided) for verification pass; the Bjork 1992 chapter for the storage/retrieval distinction quote. A screen-recording of Claude generating the synthesis table would be the video's CLI output beat.
- Output medium: screen-recording mp4 (Claude conversation in terminal/chat producing the sourced brief; terminal shows prompts and table output)
- The change: Add a second prompt asking Claude to identify the one architectural change (the system prompt wrapper) that separated harm from no-harm, and to assess what "minimum viable guardrail" looks like based on the study design.
- Teardown angle: The dashboard was honest — it measured what it measured. The failure is categorical: engagement metrics and learning metrics are different categories of measurement with unreliable correlation. Adopting AI based on in-session metrics is optimizing the wrong signal.
- Exclusions: Full LLM fine-tuning architecture; unrelated educational technology history; Atkinson 1968 mainframe context beyond a sentence.
- Score: 9/10

## Candidate 02 — "Research the Seven Signals of Genuine Learning with Claude: What Canvas Can't See"
- Source: medhavy/chapters/08-the-seven-signals.md
- Lane: RESEARCH (Claude assistant)
- Hook: Canvas shows clicks, time-on-page, and quiz scores. These are engagement metrics. Genuine learning leaves seven different kinds of behavioral evidence — and the forgery requires all of them.
- The artifact: A sourced 7-row synthesis brief: Signal | Mechanism | Primary research source | What strong vs. weak looks like — compiled from Schultz/Dayan/Montague 1997 (dopamine/prediction error), Bjork 1992 (storage/retrieval), Bransford/Schwartz 1999 (transfer), Karpicke/Roediger 2008 (retrieval practice), and Ericsson 1993 (deliberate practice). Rendered as an annotated slate.
- Prompt seed: `claude "For each of the seven Medhavy learning signals — Temporal Engagement (Y1), Error Trajectory Coherence (Y2), Cross-Context Transfer (Y3), Uncertainty Calibration (Y4), Social Knowledge Texture (Y5), Retrieval Strength Decay (Y6), Scaffolding Response Curve (Y7) — identify the primary cognitive-science mechanism and the best available empirical source. Produce a table: Signal | Mechanism | Key source | What detection looks like. Flag any signal where the composite-system evidence is weaker than the individual-component evidence."`
- Read / check: Verify that Schultz/Dayan/Montague 1997 is correctly attributed to Science; confirm Karpicke/Roediger 2008 finding (test-once beats restudy-four-times at 1-week delay); check that Y5 (Social Knowledge Texture) is correctly flagged as the least standardized signal.
- Human supplies: Access to the Schultz 1997 Science paper and Karpicke/Roediger 2008 paper for source verification; screen-recording of the Claude research session for the video output beat.
- Output medium: screen-recording mp4
- The change: Follow-up prompt: ask Claude to identify which two signals could be proxied by a faculty observer without Medhavy's measurement layer, and which require the system to be present — producing the "buy vs. build" evidence base for the adoption brief.
- Teardown angle: Each signal has strong individual-component evidence; the seven-signal composite as a deployed measurement system has theoretical motivation but not yet large-scale validation. The distinction between "components have evidence" and "integration is a bet" is the honest adoption frame.
- Exclusions: Vygotsky ZPD history beyond one sentence; Ericsson deliberate-practice full framework; GLP score algorithm details.
- Score: 8/10

## Candidate 03 — "Research the Multi-Armed Bandit in Education with Claude: When Adaptive Learning Actually Adapts"
- Source: medhavy/chapters/09-the-loop.md
- Lane: RESEARCH (Claude assistant)
- Hook: Robbins' 1952 paper on slot machines is now the algorithm deciding which teaching intervention a student gets. The difference between a bandit optimizing for immediate accuracy vs. delayed retrieval is the difference between Bastani's two outcomes.
- The artifact: A sourced 3-panel research brief: (1) The bandit algorithm class — LinUCB vs. Thompson Sampling, regret bounds, deployment history at Yahoo News/Netflix/Spotify; (2) Educational deployments — Lan/Baraniuk, Liu/Koedinger, Williams AXIS 2016 — with effect-size estimates and reward-signal choices; (3) The reward-signal distinction: immediate accuracy vs. delayed retrieval, and why they produce opposite outcomes per the Bastani mechanism.
- Prompt seed: `claude "Research contextual bandit algorithms in adaptive learning systems. Summarize: (1) LinUCB and Thompson Sampling — regret guarantees and deployment scale; (2) three peer-reviewed educational deployments using bandit selection with their reported learning gains; (3) why the choice of reward signal (immediate accuracy vs. delayed retrieval) determines whether the bandit optimizes for performance or for durable learning. Produce a 3-section brief with citable sources. Flag any effect-size claim you cannot verify."`
- Read / check: Verify the Lan/Baraniuk citation exists (they published on knowledge tracing); confirm Thompson Sampling 1933 origin; check that the Bastani reward-signal mechanism is not overstated beyond what the study's design can support.
- Human supplies: Screen-recording of the Claude research session; the AXIS 2016 conference paper for effect-size verification. The synthesized brief is the output beat.
- Output medium: screen-recording mp4
- The change: Follow-up prompt: ask Claude to identify the equity risk — a bandit that adapts to early signal signatures could entrench disadvantage for students whose patterns differ from the training population — and find any published evidence on adaptive-system equity effects.
- Teardown angle: The bandit is classical statistics from 1952, not cutting-edge AI. What is novel in Medhavy is not the algorithm class — it is the choice of reward signal. Optimizing for immediate performance produces Bastani's failure mode; optimizing for delayed retrieval is the bet the architecture is built around.
- Exclusions: Full bandit regret-bound proofs; Cowork/technical integration; LTI Canvas setup details.
- Score: 8/10

## Candidate 04 — "Research AI Fluency in Learning with Claude: The Bjork Storage-Retrieval Distinction Explained"
- Source: medhavy/chapters/01-the-failure-that-looks-like-success.md + chapters/08-the-seven-signals.md
- Lane: RESEARCH (Claude assistant)
- Hook: A student can score 88% on a quiz using borrowed AI output, and six weeks later remember nothing. The Bjork 1992 framework explains exactly why — and it predicts the forgetting before the exam reveals it.
- The artifact: A sourced 2-panel synthesis: (1) Storage strength vs. retrieval strength — the Bjork distinction with the experimental basis (Karpicke/Roediger 2008 testing effect; Bahrick 1984 fifty-year retention study); (2) A Student A vs. Student B comparison table showing which of the seven signals distinguishes them at mid-term vs. week 6, with the Canvas data showing both as identical.
- Prompt seed: `claude "Explain the Bjork storage-strength vs. retrieval-strength distinction and its experimental basis. Then produce a side-by-side table: for a student who learned genuinely (Student A) vs. one who offloaded to AI (Student B), predict what each of the seven Medhavy signals (Y1-Y7) would show at mid-term and at a 6-week delayed retention check. Cite Karpicke/Roediger 2008 and Bahrick 1984. Flag any prediction that is theoretically motivated rather than directly observed."`
- Read / check: Verify Bahrick 1984 is a real study (Spanish vocabulary 50-year follow-up); confirm Karpicke/Roediger 2008 in Science (testing beats restudy); check that Student B predictions are labeled as theoretically derived, not validated by the composite system.
- Human supplies: Screen-recording of Claude generating the table; access to the Karpicke/Roediger 2008 Science paper for source check.
- Output medium: screen-recording mp4
- The change: Add a follow-up prompt asking Claude to design the single cheapest institutional intervention — a delayed retention quiz at 6 weeks — that would distinguish Student A from Student B without requiring Medhavy, and assess what that costs in faculty time.
- Teardown angle: Storage strength is permanent; retrieval strength decays. Genuine learning builds storage strength through prediction errors. AI-offloaded learning builds retrieval strength on loan — available as long as the tool is in the loop, gone when the exam removes it. The seven signals are designed to see this distinction before the exam reveals it.
- Exclusions: Medhavy's specific GLP scoring algorithm; Canvas LTI integration details; full neuroscience of BDNF and dendritic-spine formation.
- Score: 7/10

## Candidate 05 — "Research the Adoption Decision Framework with Claude: What a Budget Committee Needs to Know"
- Source: medhavy/chapters/13-the-adoption-decision.md + chapters/11-when-kindle-is-enough.md
- Lane: RESEARCH (Claude assistant)
- Hook: Medhavy costs money. A simpler tool might solve the actual problem. The chapter's honest test: if your institution cannot or will not act on what the loop reveals, you have bought expensive Canvas analytics.
- The artifact: A sourced decision-tree brief with three branches: (1) When Kindle is enough — cases where adaptive measurement adds no value because the institution lacks the response capacity; (2) When Canvas + deliberate design is enough — faculty-actionable signal without platform overhead; (3) When the full loop is warranted — the threshold of student population, concept complexity, and response-time requirements that justify the bandit + seven-signal architecture.
- Prompt seed: `claude "Research institutional EdTech adoption decision frameworks. Produce a structured brief covering: (1) what problem a simpler, cheaper tool solves vs. what Medhavy-style measurement adds; (2) the conditions (scale, response time, measurement complexity) under which adaptive bandit selection is justified vs. overkill; (3) the three questions from the Bastani framework a vendor must answer before a pilot is approved. Synthesize from educational technology adoption literature. Flag all claims that are opinion vs. evidence."`
- Read / check: Verify the ASSISTments 0.75-grade-level effect size; cross-check the Atkinson 1968 failure mode (worked pedagogically, failed commercially for cost/politics reasons); confirm the three Bastani questions (architectural commitment, measurement type, grounding source) are faithfully represented.
- Human supplies: Screen-recording of the Claude research session. The brief is the output beat.
- Output medium: screen-recording mp4
- The change: Follow-up prompt: ask Claude to generate the two questions the curriculum committee should ask that cannot be answered with a feature sheet — requiring the vendor to describe an architectural commitment and a measurement approach — as a concrete deliverable the video viewer can use.
- Teardown angle: The adoption decision is not "is AI good for learning?" That question has a clear answer (it depends entirely on the wrapper). The decision is "does this specific platform make architectural commitments that the literature says produce durable learning — and how would we know if it failed?" Most feature sheets cannot answer this.
- Exclusions: Medhavy Canvas LTI technical setup; pricing model; vendor comparison.
- Score: 7/10

## Candidate 06 — "Research the Irreducibly Human Taxonomy with Claude: What the 56% Wage Premium is Buying"
- Source: medhavy/chapters/97-fundamental-themes.md
- Lane: RESEARCH (Claude assistant)
- Hook: AI-skilled workers command a 56% wage premium in 2024 — doubled from the year before. But the premium does not go to career-switchers who become generic technologists. It goes to domain experts who kept their domain and added AI. The seven-tier taxonomy explains exactly what they kept.
- The artifact: A sourced 4-row synthesis brief: Tier | What AI cannot do reliably | Primary evidence | Educational implication — covering Tier 4 (metacognitive/supervisory), Tier 5 (causal/counterfactual), Tier 6 (collective/distributed intelligence), and Tier 7 (wisdom/accountability), drawn from the PwC 2025 Global AI Jobs Barometer and Kahneman/Pearl causal-reasoning literature.
- Prompt seed: `claude "Research the PwC 2025 Global AI Jobs Barometer finding on the 56% wage premium for AI-skilled workers. Then synthesize evidence for each of Tiers 4-7 in the Irreducibly Human taxonomy: (Tier 4) metacognitive auditing, (Tier 5) causal reasoning, (Tier 6) collective intelligence, (Tier 7) wisdom/accountability. For each tier: what is the evidence that AI is weak here, and what is the educational implication? Cite Pearl 2018 for Tier 5. Flag any tier where the evidence is primarily theoretical rather than empirical."`
- Read / check: Verify the PwC 2025 barometer exists and the 56% figure is current; confirm Pearl 2018 (The Book of Why) for causal reasoning; check that Tier 4 weakness (models cannot audit their own outputs reliably) is grounded in documented model failure modes, not just theoretical.
- Human supplies: Access to the PwC 2025 report for the wage premium figure; screen-recording of the research session.
- Output medium: screen-recording mp4
- The change: Follow-up: ask Claude to produce a domain-specific version of the taxonomy for one domain (medicine, law, or design) — which Tier 4-7 capacities are most at risk of being delegated in that field, and what a phase-gate curriculum would protect.
- Teardown angle: The market is not rewarding AI knowledge in the abstract. It is rewarding AI-fluent domain experts who can do the Tier 4-7 work AI cannot — and who know where the gate is. The taxonomy makes the gate explicit.
- Exclusions: Boondoggling/Brutalist project details; full Gru tool walkthrough; residential vs. online degree structure details.
- Score: 7/10

## Candidate 07 — "Research the Frictional Principle with Claude: Why Cognitive Struggle Is the Mechanism, Not the Cost"
- Source: medhavy/chapters/97-fundamental-themes.md + chapters/01-the-failure-that-looks-like-success.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Kosmyna EEG study shows up to 55% reduction in functional brain connectivity during AI-assisted writing vs. brain-only writing. The students borrowed cognitive capability from the machine — and built none of their own.
- The artifact: A sourced 3-section research brief: (1) The neurobiological mechanism — Schultz dopamine prediction-error signal, BDNF upregulation, Kosmyna EEG connectivity reduction; (2) The pedagogical consequence — Bastani's 17-point gap, Bjork's storage/retrieval split; (3) Design implications — what "making the struggle more productive" looks like vs. "eliminating the struggle" with concrete examples from the four Medhavy modes.
- Prompt seed: `claude "Research the neurobiology of learning through cognitive struggle. Summarize: (1) Schultz/Dayan/Montague 1997 prediction-error dopamine signal and its role in memory consolidation; (2) the Kosmyna 2023 EEG study on brain connectivity during AI-assisted vs. brain-only writing; (3) how the Bastani 2025 study operationalizes the consequence. Produce a 3-section brief. For each section, state whether the evidence directly supports the 'struggle is the mechanism' claim or is a supporting correlate."`
- Read / check: Verify Schultz/Dayan/Montague 1997 in Science; locate the Kosmyna EEG study citation (it may be Kosmyna et al., MIT Media Lab); confirm the 55% connectivity reduction figure and sample size; check the Bastani 17-point figure against the corrected doi.
- Human supplies: The Kosmyna EEG paper for verification (it may require library access); screen-recording of the research session.
- Output medium: screen-recording mp4
- The change: Follow-up: ask Claude to identify two Medhavy modes that "make the struggle more productive" (Ask AI and Case Study) vs. one that could remove struggle if misused (Ask AI without guardrails), explaining the architectural commitment that separates them.
- Teardown angle: Cognitive struggle is not the price of learning — it is the mechanism. The prediction-error signal requires the student to make a prediction, fail, and repair. AI that hands the answer bypasses the biological event. The design question is not "less struggle" but "productive struggle" — friction that triggers encoding without overwhelming working memory.
- Exclusions: Full neuroscience of BDNF and synaptic plasticity; Koedinger/Aleven assistance dilemma full framework; psychopharmacology of dopamine.
- Score: 7/10

## Candidate 08 — "Research Phase-Gate Design with Claude: How to Specify Where AI Stops"
- Source: medhavy/chapters/97-fundamental-themes.md
- Lane: RESEARCH (Claude assistant)
- Hook: "Use AI responsibly" is not an architectural commitment. A phase gate is: AI handles X, human handles Y, the gate is at Z — and the gate must be specified precisely enough that you could tell if it failed.
- The artifact: A sourced 2-column operational brief: Domain | Phase gate specification — covering (1) teaching (AI handles preparation, human does the teaching), (2) student learning (AI handles scaffolding, human does the thinking), (3) software engineering (Boondoggling: Claude handles the Minion Part, human handles the Gru Part with five labeled supervisory capacities), and (4) creative work (Brutalist: AI handles technical execution, human handles Tier 4-7 creative judgment). Each gate includes a concrete "violated when" condition.
- Prompt seed: `claude "Research phase-gate design in human-AI collaborative systems. For four domains — teaching, student learning, software engineering, and creative production — identify: (1) what AI handles, (2) what the human handles, (3) where exactly the gate falls, and (4) a concrete 'violated when' condition that would indicate the gate has failed. Draw on the Medhavy, Boondoggling, and Brutalist frameworks. Produce a 4-row table. Flag any gate specification that is still underspecified."`
- Read / check: Verify that the Snickerdoodle/Boondoggling five supervisory capacities are correctly named (PA, PF, TO, IJ, EI); confirm that the Brutalist "Refusal Behavior" principle is the behavioral commitment that enforces the gate; check that "violated when" conditions are testable, not vague.
- Human supplies: Screen-recording of the research session.
- Output medium: screen-recording mp4
- The change: Follow-up: ask Claude to draft a 2-sentence phase-gate specification for one additional domain the viewer works in (medicine, law, or finance), with a testable violated-when condition — a concrete deliverable the viewer can adapt.
- Teardown angle: The gate is not where you trust AI less. It is where the human cognitive work is irreplaceable. Without an explicit, testable gate, the path of least resistance is to let AI do more until the human is a reviewer of AI output rather than a practitioner of a discipline.
- Exclusions: Full Gru tool walkthrough; Brutalist six-principles deep dive; Canvas LTI integration.
- Score: 6/10
