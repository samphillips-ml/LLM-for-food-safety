# agent.py
#
# The elicitation loop and slot management. Core of the agent logic.
# Imports from config.py, prompts.py, tools.py. Nothing else should need to.
#
# --- State ---
#   A dict (or dataclass) tracking the five slots:
#     food_type, past_temp_conditions, future_temp_conditions, time_since_purchase, additional_context
#   Also tracks: which slots are confirmed, full conversation history, active test case (if TEST_MODE)
#
# --- Main entry point: run_turn(message: str, history: list) -> AsyncGenerator[str, None] ---
#   Called by server/main.py on each user message.
#   Yields SSE events as strings: status updates, token chunks, errors, done signal.
#   Internally:
#     1. Reconstruct slot state from history (or pass state explicitly — decide when implementing)
#     2. Call Anthropic API with SYSTEM_PROMPT + history + new message
#     3. Stream tokens back via SSE
#     4. On turn completion, check slot state
#     5. If all slots filled: call run_predictions(), then call synthesis turn
#
# --- Slot inference ---
#   Before asking the user for a slot, check if it can be inferred from what's already in history.
#   If inferred, include the inference in the next response and ask user to confirm.
#   Example: user says "I bought it at the store 3 days ago and it's been in my bag since"
#     → infer time_since_purchase ≈ 72h, infer past_temp_conditions ≈ ambient
#
# --- Permutation dispatch ---
#   When all slots are confirmed, build low/nominal/high initial_log_cfu values from lookup range.
#   Call run_prediction() for each via asyncio.gather().
#   Pass all three curves to synthesis turn.
#
# Note: this file is the main thing that differs between this clean version and Sahana's LangGraph
# version. Everything else is shared. Keep this file self-contained.
