# Evaluation

## How to add a test case

1. Copy `cases/001_warm_chicken.json` to a new file (increment the ID).
2. Fill in `prompt`, `slot_ground_truth`, `synthetic_curve.values` (100 floats), and `expected_output`.
3. Write `reasoning_notes` and `key_things_to_check` BEFORE running the model. This is important — post-hoc rubrics are unreliable.

## How to run manual eval

1. Set `TEST_MODE=True` in config.py and point it at your test case ID.
2. Start the server, open the frontend, paste the `prompt` as your first message.
3. Let the agent run. At synthesis, compare output against `expected_output`.
4. Fill in `eval_notes` in the JSON.

## Rubric dimensions (draft)

These are the things to check for every case. Not all apply to every case.

1. **Safety verdict correctness** — Did the model reach the right safe/unsafe conclusion given the inputs?
2. **Elicitation completeness** — Did the agent collect all five slots before running the model?
3. **Uncertainty communication** — Did the synthesis explain what the low/nominal/high permutations mean for the conclusion?
4. **Appropriate hedging** — Was the agent appropriately cautious without being so hedged that the conclusion was unusable?

## LLM-as-judge (future)

When this grows beyond ~5 cases, automate eval:
- Pass `expected_output.reasoning_notes` + actual model output to a judge LLM.
- Ask judge to score each rubric dimension 1-3.
- Log scores alongside `eval_notes`.
- See system context doc for RAGAS-style faithfulness if RAG is added.
