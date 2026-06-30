# server/main.py
#
# FastAPI app. Thin wiring layer only — no agent logic lives here.
#
# --- Endpoints ---
#
#   POST /chat
#     Request body: { message: str, history: list }
#     Response: SSE stream
#     Calls agent.run_turn(message, history) and forwards yielded events to the client.
#     SSE event types (defined in config.py):
#       "status" — e.g. "Running model permutations..."
#       "token"  — a single token chunk from the LLM
#       "error"  — something went wrong, includes message
#       "done"   — stream is finished
#
#   GET /health
#     Returns 200 + {"status": "ok"}. Useful for checking the server is up.
#
# --- CORS ---
#   Enable for all origins during development (frontend/index.html opens as file://).
#   Lock down before any real deployment.
#
# --- What does NOT go here ---
#   Slot logic, prompt construction, model calls — all of that is agent.py and tools.py.
#   This file should be <50 lines when implemented.
#
# --- Future compatibility ---
#   When Sahana's React frontend replaces frontend/index.html: no change here.
#   When C# routing layer appears upstream: this becomes an internal service, no change here.
#   Contract is just POST /chat → SSE.
