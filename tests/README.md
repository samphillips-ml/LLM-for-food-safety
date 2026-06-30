# Evaluation

## How to add a test case

1. Find a ComBase record matching the scenario you want to test (filter by food
   category / temperature range against the processed pipeline output, not the
   web UI one record at a time). Note its `combase_record_id` and, once confirmed
   against `combase_food_modeling_grid_raw_phased.csv`, its `combase_source_curve_id`.
2. Copy `cases/001_chicken_mince_refrigerated.json` to a new file (increment the ID).
3. Build `elicited_inputs` (food_type, past/future_temperature_segments,
   time_elapsed_hours, additional_context) to match what the source record
   actually describes. Scenarios are matched to available data, not the other
   way around — don't force a narrative onto a record that doesn't support it.
4. Fill in `ground_truth_initial_log_cfu` and `ground_truth_curve.values` (100
   floats) directly from the matched curve. Fill in `source_record_details` for
   traceability back to ComBase.
5. Write `expected_verdict_qualitative` and any reasoning/key-checks notes
   BEFORE running the model. This is important — post-hoc rubrics are unreliable.

Note: N0 is read from the matched ComBase curve, not estimated from elicited
inputs. The elicitation contract stays human-shaped (the agent still asks the
same questions it would in deployment); the pseudo-layer is internal to how
test cases are constructed. Not a generalization claim — this checks that the
elicit -> infer -> verdict pipeline behaves coherently end to end, not that the
underlying model generalizes (that's covered separately by the ablation study).

## How to run manual eval

1. Set `TEST_MODE=True` in config.py and point it at your test case ID.
2. Start the server, open the frontend, and converse with the agent as if you
   were the person in the scenario — let it elicit `elicited_inputs` naturally
   rather than pasting them in as a single message.
3. Let the agent run. At synthesis, compare output against
   `expected_verdict_qualitative` and the ground truth curve.
4. Fill in `eval_notes` in the JSON.

## Rubric dimensions (draft)

These are the things to check for every case. Not all apply to every case.

1. **Safety verdict correctness** — Did the model reach the right safe/unsafe conclusion given the inputs?
2. **Elicitation completeness** — Did the agent collect all five slots before running the model?
3. **Uncertainty communication** — Did the synthesis explain what the low/nominal/high permutations mean for the conclusion?
4. **Appropriate hedging** — Was the agent appropriately cautious without being so hedged that the conclusion was unusable?

## LLM-as-judge (future)

When this grows beyond ~5 cases, automate eval:
- Pass `expected_verdict_qualitative` + reasoning notes + actual model output to a judge LLM.
- Ask judge to score each rubric dimension 1-3.
- Log scores alongside `eval_notes`.
- See system context doc for RAGAS-style faithfulness if RAG is added.