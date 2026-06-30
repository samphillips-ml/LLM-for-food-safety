# model/inference.py
#
# The time series model boundary. This is the only file Tom's real model touches.
# Agent calls tools.py/run_prediction(), which calls this. Two layers of indirection
# so the agent never imports from here directly.
#
# --- Function: predict(food_type, temp_array, pH, aw, initial_log_cfu, t_array) -> list[float] ---
#
#   Inputs:
#     food_type       : str, e.g. "cooked_chicken" (matches lookup table keys)
#     temp_array      : list[float], temperature (°C) at each timestep, length = len(t_array)
#     pH              : float, constant for this food type (from lookup)
#     aw              : float, constant for this food type (from lookup)
#     initial_log_cfu : float, log10 CFU/g at t=0 (t_i), from lookup range (low/nominal/high)
#     t_array         : list[float], 100-step grid, 15.1515h intervals, 1500h ceiling
#
#   Output:
#     list[float], length 100 — predicted log10 CFU/g at each timestep
#
#   Stub behavior (until Tom's model is ready):
#     Return a synthetic sigmoid curve starting at initial_log_cfu, rising to ~8-9 log CFU.
#     Shape can be crude. Purpose is to let the agent and frontend run end-to-end.
#     If TEST_MODE: caller (tools.py) intercepts before this is called and returns
#     the synthetic_curve from the test case JSON instead.
#
#   Real model drops in here:
#     Load weights, run inference, return curve. Same signature, same return type.
#     No other file changes.
