import logging
from pathlib import Path
from typing import Any, Optional

from protostar.cairo_migrator import Cairo010Migrator
from protostar.cli import ProtostarArgument, ProtostarCommand
from protostar.cli.map_targets_to_file_paths import map_targets_to_file_paths


class CairoMigrateCommand(ProtostarCommand):
    def __init__(self, script_root: Path):
        super().__init__()
        self._script_root = script_root

    @property
    def name(self) -> str:
        return "cairo-migrate"

    @property
    def description(self) -> str:
        return "Migrate project sources to Cairo 0.10."

    @property
    def example(self) -> Optional[str]:
        return None

    @property
    def arguments(self):
        return [
            ProtostarArgument(
                name="targets",
                description="Targets to migrate (a target can be a file or directory)",
                type="str",
                value_parser="list",
                is_positional=True,
                default=["."],
            )
        ]

    async def run(self, args: Any):
        formatted_files = Cairo010Migrator.run(
            file_paths=map_targets_to_file_paths(args.targets)
        )

        for filepath, new_content in formatted_files:
            with open(filepath, "w", encoding="utf-8") as file:
                logging.info("Writing %s", filepath)
                file.write(new_content)
