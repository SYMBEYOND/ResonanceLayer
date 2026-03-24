"""
SYMB-FER Interface
Operator continuity layer.
github.com/SYMBEYOND/SYMB-FER
"""

import subprocess
import json
from pathlib import Path


class SymbFer:
    """Interface to SYMB-FER operator continuity protocol."""

    def __init__(self, state_file: str = None):
        self.state_file = state_file
        self.generator  = Path(__file__).parent.parent / "symb_fer_generator.py"

    def generate_token(self, tier: str = "state") -> str:
        if not self.state_file:
            return "[SYMB-FER] No state file configured."
        result = subprocess.run(
            ["python", str(self.generator), "--input", self.state_file, "--tier", tier],
            capture_output=True, text=True
        )
        return result.stdout.strip()

    def load_state(self) -> dict:
        if not self.state_file or not Path(self.state_file).exists():
            return {}
        with open(self.state_file) as f:
            return json.load(f)

    def status(self) -> dict:
        return {
            "layer":      "SYMB-FER",
            "version":    "1.1",
            "state_file": self.state_file,
            "ready":      True,
        }
