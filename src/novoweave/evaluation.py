"""Conceptual evaluation and ranking policies."""

from __future__ import annotations

from novoweave.contracts import RankedCandidate, SequenceCandidate


class PlaceholderEvaluator:
    """Documents the scoring boundary without fabricating scientific metrics."""

    def score(self, candidate: SequenceCandidate) -> dict[str, float]:
        raise NotImplementedError(
            "No validated structure predictor or biological evaluator is included"
        )


def rank_candidates(
    candidates: list[SequenceCandidate],
    scorecards: list[dict[str, float]],
) -> list[RankedCandidate]:
    """Conceptual multi-objective ranking entry point.

    A real implementation must declare metric direction, normalization,
    uncertainty, tie behavior, rejection thresholds, and missing-value policy.
    It must not silently collapse incomparable metrics into one confidence value.
    """
    if len(candidates) != len(scorecards):
        raise ValueError("Each candidate must have exactly one scorecard")
    raise NotImplementedError(
        "Ranking policy requires an explicit validated specification"
    )
