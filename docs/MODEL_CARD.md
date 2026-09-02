# Model card

## Model details

No model is distributed. `GeometricDiffusionBackbone` and
`StructureConditionedTransformer` are interface sketches whose methods raise
`NotImplementedError`.

## Intended use

- Teaching modular research-software architecture.
- Discussing interfaces between geometric and sequence models.
- Prototyping configuration and provenance standards.

## Out-of-scope use

- Generating or selecting real biological sequences.
- Clinical, diagnostic, therapeutic, agricultural, or environmental decisions.
- Claims about safety, function, binding, toxicity, or manufacturability.
- Optimization of harmful biological properties.

## Training data

None. A future implementation must document dataset versions, licenses,
deduplication, leakage analysis, structural resolution filters, chain handling,
and train/validation/test split policy.

## Evaluation

No benchmark results exist. Before any capability claim, a real implementation
would require preregistered tasks, leakage-resistant splits, baselines,
uncertainty reporting, failure analysis, and relevant experimental validation.

## Limitations

The repository demonstrates software shape only. Type hints and clean interfaces
do not imply scientific correctness. Computational confidence is not biological
evidence, and in-silico screening cannot establish real-world safety.

