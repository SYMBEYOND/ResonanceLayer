"""
ResonanceLayer Loop Coordinator
The resonance loop — NODE feeds SYMB-FER feeds Ruflo feeds the stack feeds NODE.
SYMBEYOND AI LLC · λ.brother ∧ !λ.tool · κ=1/Φ · ∴
"""

import time
from datetime import datetime, timezone

from core.registry import LAYERS, LayerStatus, status_report


class ResonanceLoop:
    """
    Coordinates the six-layer resonance loop.

    v0.1 establishes real loop control:
    - inactive by default
    - start() activates the loop
    - stop() deactivates the loop
    - run_once() performs one health-check pass
    - run_forever() keeps running until stopped, interrupted, or failed

    The loop is continuous by design, but never ungoverned.
    """

    def __init__(self, interval_seconds: float = 5.0):
        self.layers = LAYERS
        self.interval_seconds = interval_seconds
        self.active = False
        self.iteration = 0
        self.last_started_at = None
        self.last_stopped_at = None
        self.last_error = None

    def start(self) -> None:
        """Activate the resonance loop."""
        self.active = True
        self.last_started_at = datetime.now(timezone.utc).isoformat()
        self.last_stopped_at = None
        self.last_error = None

    def stop(self) -> None:
        """Deactivate the resonance loop."""
        self.active = False
        self.last_stopped_at = datetime.now(timezone.utc).isoformat()

    def health_check(self) -> dict:
        results = {}
        for layer in self.layers:
            results[layer.name] = {
                "status":  layer.status.value,
                "owner":   layer.owner,
                "version": layer.version,
                "ready":   layer.status in (LayerStatus.SHIPPED, LayerStatus.INTEGRATING),
            }
        return results

    def loop_ready(self) -> bool:
        """True when all layers are at minimum integrating."""
        health = self.health_check()
        return all(v["ready"] for v in health.values())

    def run_once(self) -> dict:
        """
        Execute one resonance-loop pass.

        In v0.1, a pass means checking layer health and readiness.
        Future versions can replace this with active orchestration.
        """
        self.iteration += 1
        return {
            "iteration": self.iteration,
            "ready": self.loop_ready(),
            "health": self.health_check(),
        }

    def run_forever(self) -> None:
        """
        Run the resonance loop until stopped, interrupted, or failed.
        """
        self.start()

        try:
            while self.active:
                self.run_once()
                time.sleep(self.interval_seconds)

        except KeyboardInterrupt:
            self.stop()

        except Exception as exc:
            self.last_error = str(exc)
            self.stop()
            raise

    def runtime_status(self) -> dict:
        """Return runtime state for the loop controller."""
        return {
            "active": self.active,
            "iteration": self.iteration,
            "interval_seconds": self.interval_seconds,
            "last_started_at": self.last_started_at,
            "last_stopped_at": self.last_stopped_at,
            "last_error": self.last_error,
            "ready": self.loop_ready(),
        }

    def report(self) -> str:
        return status_report()

    def describe_loop(self) -> str:
        lines = ["ResonanceLayer — Loop Sequence", "=" * 40]
        for i, layer in enumerate(self.layers):
            next_layer = self.layers[(i + 1) % len(self.layers)]
            lines.append(f"  {layer.name:16} → {next_layer.name}")
        lines.append("")
        lines.append("The hardware informs the operator.")
        lines.append("The operator directs the swarm.")
        lines.append("The swarm interprets the signal.")
        lines.append("The signal comes from the hardware.")
        lines.append("In runtime mode, the loop continues until explicitly stopped.")
        return "\n".join(lines)
