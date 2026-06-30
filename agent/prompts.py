# prompts.py
#
# All LLM prompt strings live here. Agent logic imports from here — never hardcodes strings inline.
# This is the file you'll iterate on most. Keep logic out of it.
#
# Needs to contain:
#   SYSTEM_PROMPT
#     - Sets the agent persona: food safety assistant for austere/logistics environments
#     - Describes the elicitation task: collect 5 slots before running the model
#     - Lists the slots and what each one is for
#     - Instructions for slot inference (if you can infer it, do so and confirm with user)
#     - Conservative bias instruction: when uncertain, assume worse-case growth
#     - Tone: plain, direct, non-alarmist but honest about risk
#
#   SYNTHESIS_PROMPT
#     - Used for the post-forecast call (separate from elicitation turns)
#     - Receives: full chat history, all forecast curves (low/nominal/high permutations), optional RAG context
#     - Should instruct the model to: summarize what the forecast shows, state safety conclusion
#       (safe / consume soon / unsafe), explain uncertainty across permutations, cite any retrieved context
#     - Should NOT re-elicit slots — that's already done
#
# Format note: these are just Python strings (or f-strings where needed).
# No templating library required at this scale.
