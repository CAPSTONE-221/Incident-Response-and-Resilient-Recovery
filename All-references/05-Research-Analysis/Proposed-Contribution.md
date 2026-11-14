# Proposed Project Contribution

## Project title

**Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery**

## Problem motivation

An incident-response agent may identify threats and recommend response actions, but safe recovery requires additional checks. A backup or recovery point can be recent and technically restorable while still containing malicious persistence, compromised identities, or corrupted data. Likewise, a plausible AI-generated action should not automatically be executed if it violates security or operational policy.

The project therefore focuses on connecting incident evidence, recovery-point trust, policy enforcement, dependency-aware restoration, and post-recovery validation.

## Proposed workflow

```text
Incident and asset evidence
          |
          v
Evidence collection and normalisation
          |
          v
Threat / compromise context
          |
          v
Recovery Trust Assessment
          |
          v
Recovery Trust Score (RTS)
          |
          v
Trust state classification
(TRUSTED / UNCERTAIN / UNTRUSTED)
          |
          v
Deterministic policy gate
          |
          +------> Deny / isolate
          |
          +------> Human approval required
          |
          v
Dependency-aware recovery planning
          |
          v
Controlled restoration
          |
          v
Post-recovery validation
          |
          v
Evidence update and RTS re-scoring
```

## 1. Evidence collection and normalisation

Collect relevant evidence from the sources available in the system. Depending on the implemented prototype, these may include:
- backup metadata and timestamps;
- integrity-check results;
- endpoint or system telemetry;
- indicators of compromise;
- vulnerability and asset information;
- identity and access-state observations;
- CTI records and ATT&CK technique mappings.

Each evidence item should retain its source, timestamp, confidence, and relationship to the asset or recovery point. Do not imply that a source is integrated unless it is implemented and tested.

## 2. Recovery Trust Score (RTS)

The RTS is a project-defined measure intended to summarise the trustworthiness of a candidate recovery point.

The implementation must document:
- input features;
- feature normalisation;
- scoring formula and weights;
- treatment of missing or stale evidence;
- uncertainty representation;
- threshold selection and calibration;
- hard rejection conditions.

A score should support a decision; it must not replace mandatory integrity checks or security policy.

## 3. Trust-state classification

The proposed states are:

| State | Meaning | Example policy |
|---|---|---|
| TRUSTED | Evidence satisfies defined trust criteria and no hard rejection condition is present | Eligible for recovery planning, subject to policy checks |
| UNCERTAIN | Evidence is incomplete, conflicting, stale, or below the trusted threshold | Hold for additional validation or human approval |
| UNTRUSTED | Evidence indicates compromise or a hard rejection condition is met | Reject as a recovery candidate and investigate |

Thresholds and exact state transitions must be defined in the implementation and justified through evaluation. Do not select thresholds solely for convenient demonstration results.

## 4. Deterministic policy gate

The policy gate evaluates whether a proposed action is allowed, denied, or requires human approval.

It should:
- enforce hard security constraints;
- distinguish low-risk and high-impact actions;
- reject actions based on untrusted recovery points;
- require approval for configured critical actions;
- log the action, evidence, rule, decision, and approver where applicable.

The language model may propose a plan, but the policy gate—not the model's natural-language confidence—determines whether execution is permitted.

## 5. Dependency-aware recovery

Represent relevant assets and services as a dependency graph. The planner should:
- identify prerequisites;
- avoid restoring a dependent service before required dependencies are ready;
- consider the trust state of each component;
- detect cycles or unresolved dependencies;
- produce an auditable restoration order.

The project should define the graph model and demonstrate it using representative test scenarios.

## 6. Post-recovery validation and re-scoring

After restoration:
- run the configured integrity and security checks;
- verify service health and dependency availability;
- check for known indicators of compromise;
- record validation results;
- update evidence and recompute trust where appropriate;
- prevent completion from being reported if required checks fail.

## 7. Evaluation plan

Use controlled scenarios with known ground truth, including clean, compromised, stale, incomplete, and conflicting recovery evidence.

| Evaluation dimension | Candidate metric |
|---|---|
| Recovery speed | Mean Time to Recovery (MTTR) |
| Recovery-point selection | Accuracy, precision, recall, or F1 for clean-point identification |
| Recovery safety | Contaminated-recovery rate |
| Policy enforcement | Unsafe-action rate and policy violation count |
| Dependency planning | Dependency-order violation rate |
| Validation | Post-recovery validation pass rate |
| Human oversight | Approval rate and approval latency |

Compare the proposed system with clearly described baselines, such as a recency-only recovery-point selector or a planner without the trust/policy layer. Keep test data and assumptions consistent across comparisons.

## Contribution statement

The intended contribution is a prototype recovery workflow that combines evidence-based recovery-point assessment, an explicit Recovery Trust Score, trust-state classification, deterministic policy enforcement, dependency-aware restoration planning, and post-recovery validation. The contribution should be claimed only to the extent that these components are implemented and experimentally evaluated.

## Related references

- NIST SP 800-184: https://www.nist.gov/publications/guide-cybersecurity-event-recovery
- NIST SP 800-61 Rev. 3: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- MITRE ATT&CK: https://attack.mitre.org/
- STIX 2.1: https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html
- TAXII 2.1: https://docs.oasis-open.org/cti/taxii/v2.1/os/stix-v2.1-os.html
