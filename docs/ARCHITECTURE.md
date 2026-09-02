# Architecture

## System boundary

The framework begins with a human-authored design brief and ends with a ranked,
auditable set of computational hypotheses. It does not include synthesis,
laboratory automation, deployment, or autonomous decision-making.

## Component map

| Component | Input | Output | Responsibility |
|---|---|---|---|
| Constraint parser | YAML / API model | `DesignBrief` | Validate explicit software constraints |
| Backbone generator | Brief + seed | Backbone candidates | Propose geometric hypotheses |
| Sequence designer | Backbones + seed | Sequence candidates | Propose compatible sequences |
| Evaluator | Sequence candidate | Metric scorecard | Keep metrics separate and traceable |
| Ranker | Candidates + scorecards | Ranked candidates | Apply a declared selection policy |
| Manifest writer | Run context | Immutable manifest | Capture provenance and warnings |

All scientific components are dependency-injected behind protocols. A future
implementation can replace a model without changing the public orchestration
contract.

## Data flow and provenance

Every planned candidate should carry:

- a stable candidate identifier and parent identifiers;
- configuration digest, code revision, model revision, and random seed;
- dataset/license lineage for trained artifacts;
- every transformation applied after sampling;
- warnings and reviewer decisions.

## Failure model

The orchestrator should fail closed on schema mismatch, missing provenance,
unknown model revision, incomplete screening, or evaluation-service failure.
Scores must not be silently imputed. Partial results should be marked incomplete
and excluded from default ranking.

## Non-goals

- Reproducing a particular published model.
- Claiming biological function from computational output.
- Hiding uncertainty behind a single aggregate score.
- Connecting directly to laboratory automation.

