# config.py
#
# Central place for all configuration constants. Nothing else should hardcode these.
#
# Needs to contain:
#   - Anthropic model name (e.g. "claude-sonnet-4-6")
#   - max_tokens for elicitation turns vs synthesis turn (synthesis needs more)
#   - SSE event type strings ("status", "token", "error", "done") so they're defined once
#   - Feature flags: RAG_ENABLED (bool), TEST_MODE (bool — swaps in synthetic curves from test cases)
#   - Permutation settings: how many low/nominal/high runs, max total experiments
#   - Grid constants: N_STEPS=100, STEP_INTERVAL_H=15.1515, T_CEILING_H=1500
#     (these must match the ComBase pipeline exactly — do not change without coordinating)
#
# What does NOT go here:
#   - Prompts (those are in prompts.py)
#   - Lookup table data (that's in data/lookup_table.csv)
#   - Anything that changes per-request (that's agent state)
