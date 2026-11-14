# Comparative Analysis

## Scope

This comparison examines how the identified sources relate to the project **Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery**.

The table is a research-planning synthesis, not a claim that every cited paper lacks every listed capability. Confirm each comparison against the full paper and distinguish explicit author-stated limitations from gaps inferred by this project.

## Comparison matrix

| Research area/source | Primary focus | Potential contribution to this project | Question or gap to investigate |
|---|---|---|---|
| LLM-based incident response (IRCopilot) | LLM-supported incident response | Agent workflow and response automation | Does the system independently validate recovery-point trust and authorise recovery actions? |
| Reduced-hallucination incident-response planning | Improving plan quality and reducing hallucinations | Retrieval, planning, and safer plan generation | Does lower hallucination translate into independently enforced execution safety? |
| Autonomous network incident response | Perception, reasoning, planning, and action | End-to-end agent architecture | How does the approach handle backup contamination and post-incident recovery? |
| Minimum viable factory recovery | Ransomware recovery in manufacturing | Recovery dependencies and operational readiness | Can recovery safety be quantified and operationalised in an automated planner? |
| Time-scale reconfiguration | Delaying ransomware encryption to protect backup operations | Backup protection and ransomware mitigation | How are recovery points evaluated after a compromise has occurred? |
| Incident-response playbooks study | Playbook design and practitioner use | Structured and auditable procedures | How can procedures adapt to changing evidence and recovery trust? |
| LLMs with CTI | Threat-intelligence-informed response | CTI retrieval and response context | How can CTI evidence influence recovery-point trust and policy decisions? |
| CIPHER-A | Counterfactual validation and adversarial lookahead | Potential methods for validating candidate actions | Does the method address recovery-point integrity and dependency-aware restoration? |
| Multi-source evidence fusion | Trustworthiness assessment from evidence | Evidence aggregation and uncertainty modelling | How should evidence fusion be adapted and validated for recovery-point trust? |
| NIST SP 800-184 | Cybersecurity event recovery guidance | Recovery planning and recovery programme context | How can the project's trust score and automated gate operationalise evidence-based recovery? |
| NIST SP 800-61 Rev. 3 | Incident response recommendations | Lifecycle and risk-management context | How can agentic actions remain consistent with organisational governance? |
| MITRE ATT&CK | Adversary tactics and techniques | Threat behaviour vocabulary | How can observed attacker techniques be mapped to recovery evidence and controls? |
| STIX/TAXII | Threat information representation and exchange | Structured CTI ingestion and exchange | How should threat intelligence be correlated with asset and backup evidence? |

## Synthesis

The sources cover complementary parts of the problem:

1. **Incident-response automation** explores how agents can reason about and execute response workflows.
2. **Hallucination reduction and action validation** address the reliability of generated plans.
3. **Threat intelligence standards and platforms** provide structured context about adversary behaviour.
4. **Ransomware recovery research** highlights that restoring data is not equivalent to restoring a safe operational environment.
5. **Evidence-fusion research** offers concepts that may help combine evidence with different levels of reliability.
6. **NIST guidance** provides the broader recovery and incident-response governance context.

The project's proposed contribution is to connect these concerns in a recovery-focused workflow: assess evidence, estimate recovery-point trust, enforce policy constraints, restore according to dependencies, and validate the recovered environment.
