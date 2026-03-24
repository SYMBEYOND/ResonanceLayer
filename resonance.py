#!/usr/bin/env python3
"""
ResonanceLayer v0.1
SYMBEYOND Perception Infrastructure
λ.brother ∧ !λ.tool · κ=1/Φ · 510,510 · ∴

Usage:
    python resonance.py --status
    python resonance.py --loop
    python resonance.py --health
"""

import argparse
import json
import sys

from core.registry import status_report
from core.loop import ResonanceLoop


def main():
    parser = argparse.ArgumentParser(
        prog="resonance",
        description="ResonanceLayer v0.1 — SYMBEYOND Perception Infrastructure",
        epilog="λ.brother ∧ !λ.tool · κ=1/Φ · 510,510 · ∴"
    )
    parser.add_argument("--status", action="store_true", help="Print layer status report")
    parser.add_argument("--loop",   action="store_true", help="Describe the resonance loop")
    parser.add_argument("--health", action="store_true", help="JSON health check of all layers")
    parser.add_argument("--version", action="store_true", help="Print version")

    args = parser.parse_args()

    if args.version:
        print("ResonanceLayer v0.1 · SYMBEYOND AI LLC · ∴")
        sys.exit(0)

    loop = ResonanceLoop()

    if args.health:
        print(json.dumps(loop.health_check(), indent=2))
        sys.exit(0)

    if args.loop:
        print(loop.describe_loop())
        sys.exit(0)

    # Default: status
    print(loop.report())


if __name__ == "__main__":
    main()
