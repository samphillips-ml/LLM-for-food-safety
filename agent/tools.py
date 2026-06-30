# tools.py
#
# Everything the agent can "call out" to. Three stub boundaries live here.
# Real implementations drop in without touching agent.py.
#
# --- STUB 1: lookup_food_params(food_type: str) -> dict ---
#   Reads data/lookup_table.csv (or an in-memory dict for now).
#   Returns: {pH_range, aw_range, initial_log_cfu_range} for the given food type.
#   If food_type not found, return None so agent can ask user to clarify.
#   This is yours to own and expand. Start with ~5 known foods.
#
# --- STUB 2: run_prediction(food_type, temp_array, pH, aw, initial_log_cfu, t_array) -> list[float] ---
#   This is the boundary with Tom's time series model.
#   Signature is fixed — do not change it when swapping in the real model.
#   Stub behavior:
#     - If TEST_MODE (from config.py): read synthetic_curve from the active test case and return it
#     - Otherwise: return a plausible fake sigmoid growth curve of length len(t_array)
#   Real model drops in here when Tom's ready. Agent logic never changes.
#
# --- STUB 3: retrieve_rag_context(query: str) -> str ---
#   Returns relevant text chunks from the paper corpus.
#   Stub returns "" (empty string).
#   Real implementation: embed query, hit ChromaDB, return top-3 chunks concatenated.
#   Synthesis prompt handles empty string gracefully (just omits the citations section).
#
# Note: run_prediction() will be called via asyncio.gather() for permutations.
# Make sure the stub is async-safe (or wrap it when the time comes).
