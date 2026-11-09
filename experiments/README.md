# First benchmark

1. Wire the fixed policy to an emulator adapter with reset and step operations.
2. Record maximum horizontal progress, frames survived and completion for each starting state.
3. Feed a compact observation into NEAT and log the seed and fitness per generation.
4. Compare both policies on held-out starting states using the same frame budget.
