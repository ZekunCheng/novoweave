"""Pseudocode model adapters.

These classes document expected responsibilities. They do not implement tensor
operations, trainable networks, or biologically meaningful sampling.
"""

from __future__ import annotations

from novoweave.config import BackboneConfig, SequenceConfig
from novoweave.contracts import (
    BackboneCandidate,
    DesignBrief,
    SequenceCandidate,
)


class GeometricDiffusionBackbone:
    """Conceptual SE(3)-aware diffusion backbone generator."""

    def __init__(self, config: BackboneConfig) -> None:
        self.config = config

    def sample(self, brief: DesignBrief, *, seed: int) -> list[BackboneCandidate]:
        """Describe, but intentionally do not execute, reverse diffusion.

        Intended algorithm:
        1. Encode length, symmetry, motifs, and masks from ``brief``.
        2. Initialize a noisy rigid-frame representation.
        3. Repeatedly predict translation and rotation denoising updates.
        4. Project updates through geometric and constraint masks.
        5. Decode frames into backbone atom coordinates with provenance.
        """
        raise NotImplementedError(
            "Conceptual adapter only: no backbone model or sampler is included"
        )


class StructureConditionedTransformer:
    """Conceptual inverse-folding sequence designer."""

    def __init__(self, config: SequenceConfig) -> None:
        self.config = config

    def design(
        self, backbones: list[BackboneCandidate], *, seed: int
    ) -> list[SequenceCandidate]:
        """Describe, but intentionally do not execute, sequence decoding.

        Intended algorithm:
        1. Build a residue graph from each backbone.
        2. Encode local frames, distances, and chain relationships.
        3. Decode masked residues under user constraints.
        4. Record sampling temperature, seed, and model revision.
        """
        raise NotImplementedError(
            "Conceptual adapter only: no sequence model or decoder is included"
        )
