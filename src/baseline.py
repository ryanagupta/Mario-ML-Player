"""Deterministic action policy for a future emulator adapter."""


def action_for_frame(frame: int) -> tuple[str, ...]:
    """Hold right and jump for the first eight frames of each 40-frame cycle."""
    return ("right", "jump") if frame % 40 < 8 else ("right",)


if __name__ == "__main__":
    for frame in (0, 7, 8, 39, 40):
        print(f"{frame}: {', '.join(action_for_frame(frame))}")
