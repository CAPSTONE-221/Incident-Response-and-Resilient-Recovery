# Multi-Stage APT Attack Simulation & Dependency Graph

## Overview
This dataset supports testing the **Blast Radius Assessment**, **Incident Correlation**, and **Dependency-Aware Resilient Recovery** components of the project.

In an enterprise compromise, services cannot be restored at random or merely based on newest timestamps. Systems have strict dependencies:
- A payment API cannot function if the relational database is down.
- A database cannot authenticate connections if the directory service (Active Directory / Kerberos) is unavailable.
- Restoring an upstream service before downstream security policies are applied can re-infect the recovered machine.

## Service Dependency DAG Schema
The topology in `service_dependency_dag.json` models a canonical 4-tier enterprise system:
$$\text{SVC\_AUTH\_AD} \longrightarrow \text{SVC\_CORE\_DB} \longrightarrow \text{SVC\_BACKEND\_API} \longrightarrow \text{SVC\_WEB\_FRONTEND}$$

## Optimization Problem Modeled
$$\min_{\pi} \left[ \alpha \cdot \text{SecurityRisk}(\pi) + \beta \cdot \text{BusinessDowntime}(\pi) + \gamma \cdot \text{RecoveryCost}(\pi) + \delta \cdot \text{ResidualRisk}(\pi) \right]$$

**Subject to:**
1. $\text{RTS}(\text{RP}_i) \ge \tau$ (Recovery point trust threshold)
2. Topological dependency ordering: If $S_A \to S_B$, $S_A$ must achieve `VALIDATED_ONLINE` before $S_B$ restore begins.
3. Policy gates: High-impact nodes (Tier-1) require operator approval before network un-quarantine.
4. Blast radius constraint: No restorative action may trigger unverified routing across compromised subnet boundaries.
