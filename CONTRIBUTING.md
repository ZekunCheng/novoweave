# Contributing

Thank you for improving this research-software blueprint. Contributions should
preserve the project's central promise: no capability claim without evidence.

## Before opening a pull request

1. Open an issue describing the interface, documentation, or research question.
2. Keep core scientific algorithms clearly marked as pseudocode until they are
   implemented, benchmarked, and independently reviewed.
3. Add or update contract tests and documentation.
4. Run `pytest`, `ruff check .`, and `mypy src`.
5. Complete the scientific-claims section of the pull-request template.

## Pull-request expectations

- Prefer small, reviewable changes.
- Record assumptions and known failure modes.
- Do not commit datasets, model weights, secrets, patient data, proprietary
  sequences, or material that lacks a clear redistribution license.
- Do not present computational scores as evidence of biological safety,
  function, efficacy, or manufacturability.

## Commit style

Use concise imperative subjects, for example:

```text
docs: clarify sampler contract
test: cover invalid design lengths
refactor: isolate ranking policy
```

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

