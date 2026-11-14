# Identified Research Gaps

## Purpose

This document organises the research gaps presented in the project's review material into a form that can guide implementation and evaluation. These are the project's research claims and design motivations; they must be supported by a systematic reading of the cited literature before being presented as established gaps across the entire field.

## Gap 1 — Absence of an explicit recovery-trust layer

**Problem statement:** Incident-response automation and recovery guidance address response actions and recovery processes, but the project identifies a need for an explicit layer that assesses the trustworthiness of candidate recovery points and supporting evidence.

**Proposed direction:** Introduce a recovery-trust assessment stage before restoration decisions are authorised.

**Evidence to examine:** NIST SP 800-184; ransomware recovery research; LLM-based incident-response papers.

**Evaluation question:** Does adding a recovery-trust stage improve selection of clean recovery points compared with a baseline that selects recovery points using simpler criteria?

## Gap 2 — Recovery-point trust needs a measurable representation

**Problem statement:** A recovery point may be available without being safe. Availability, recency, or successful restoration alone does not establish that the data is free from compromise.

**Proposed direction:** Define a Recovery Trust Score (RTS) using documented evidence features, a transparent scoring method, and explicit uncertainty handling.

**Design requirements:**
- define the evidence inputs and their provenance;
- explain normalisation and weighting;
- document missing-data handling;
- prevent a high score from overriding hard security constraints;
- calibrate thresholds using test data rather than arbitrary values.

**Evaluation question:** How accurately does RTS distinguish clean, uncertain, and compromised recovery points in controlled scenarios?

## Gap 3 — Trust must respond to changing or conflicting evidence

**Problem statement:** Evidence can be incomplete, stale, contradictory, or updated during investigation. A fixed score may not reflect new findings.

**Proposed direction:** Recompute or update trust when relevant evidence changes, while retaining an audit trail of score inputs and changes.

**Evidence to examine:** Multi-source evidence-fusion research and CTI-related sources.

**Evaluation question:** Does dynamic re-scoring respond correctly to injected evidence changes, stale indicators, and conflicting observations?

## Gap 4 — Plausible AI-generated actions still require independent authorisation

**Problem statement:** A generated response plan can be linguistically convincing while violating security, operational, or organisational constraints.

**Proposed direction:** Place a deterministic policy gate between planning and execution. Require human approval for actions classified as critical or high impact.

**Design requirements:**
- separate plan generation from action authorisation;
- define allow, deny, and approval-required outcomes;
- log the policy rule and evidence behind each decision;
- fail safely when required evidence is missing.

**Evaluation question:** Can the gate block prohibited actions and route high-risk actions for approval, including when the LLM recommends them?

## Gap 5 — Recovery must respect service and asset dependencies

**Problem statement:** Restoring systems in an arbitrary order can leave services unusable or reintroduce compromised dependencies. The recovery order should reflect the dependency graph and security state of components.

**Proposed direction:** Represent dependencies explicitly and generate a recovery sequence that respects prerequisites and trust conditions.

**Evaluation question:** Does dependency-aware ordering reduce failed restorations, service unavailability, and unsafe reconnection compared with a non-dependency-aware baseline?

## Gap 6 — Recovery quality must measure safety as well as speed

**Problem statement:** A short recovery time does not prove that the recovered environment is secure. A system could restore quickly while reintroducing compromised data or leaving residual attacker access.

**Proposed direction:** Evaluate recovery speed together with safety and correctness measures.

**Candidate metrics:**
- Mean Time to Recovery (MTTR);
- recovery-point selection accuracy;
- contaminated-recovery rate;
- unsafe-action rate;
- residual-compromise rate;
- dependency-order violation rate;
- post-recovery validation pass rate;
- human-approval rate and decision latency.

**Evaluation question:** Does the proposed approach improve safety without imposing unacceptable recovery delay?

## Gap-to-system mapping

| Gap | Proposed system component | Evidence needed |
|---|---|---|
| No explicit recovery-trust layer | Recovery Trust Assessment | Threat model and clean/compromised recovery-point test cases |
| Trust not measurable | Recovery Trust Score | Feature definitions, scoring rationale, calibration and accuracy |
| Static trust | Evidence update and re-scoring | Timestamped and conflicting evidence scenarios |
| Unsafe generated actions | Policy gate and human approval | Adversarial and prohibited-action test cases |
| Dependency blindness | Dependency-aware recovery planner | Dependency graph and restoration-order experiments |
| Speed-only evaluation | Safety-aware evaluation | Baselines and measurable recovery/safety metrics |
