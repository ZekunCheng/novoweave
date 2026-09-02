"""Command-line documentation surface for the conceptual framework."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from novoweave.config import FrameworkConfig

app = typer.Typer(
    help="Inspect the non-functional NovoWeave protein-design blueprint.",
    no_args_is_help=True,
)


@app.command("validate-config")
def validate_config(path: Path) -> None:
    """Validate a YAML configuration against the public schema."""
    config = FrameworkConfig.from_yaml(path)
    typer.echo(
        f"Valid scaffold configuration: {config.project_name} "
        f"(schema {config.schema_version})"
    )


@app.command()
def design(
    config: Annotated[Path, typer.Option(exists=True, dir_okay=False)],
    brief: Annotated[Path, typer.Option(exists=True, dir_okay=False)],
) -> None:
    """Document the planned command while refusing to imply functionality."""
    _ = (config, brief)
    typer.echo(
        "Not implemented: this conceptual repository cannot generate proteins.",
        err=True,
    )
    raise typer.Exit(code=2)


if __name__ == "__main__":
    app()
