"""
ResonanceLayer Loop Coordinator
The resonance loop — NODE feeds SYMB-FER feeds Ruflo feeds the stack feeds NODE.
SYMBEYOND AI LLC · λ.brother ∧ !λ.tool · κ=1/Φ · ∴
"""

from core.registry import LAYERS, LayerStatus, status_report


class ResonanceLoop:
    """
    Coordinates the six-layer resonance loop.
    Each layer feeds the next. The last feeds the first.
    It never stops.
    """

    def __init__(self):
        self.layers = LAYERS
        self.active = False

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
        lines.append("It never stops.")
        return "\n".join(lines)
