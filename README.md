# fresh-llm-demo

Demo scaffold for the FRESH LLM agent. Clean Python + vanilla HTML implementation.
All stubs — work through each file individually before implementing.

## Structure

```
agent/
  config.py     # constants, feature flags, grid params
  prompts.py    # SYSTEM_PROMPT, SYNTHESIS_PROMPT
  tools.py      # lookup_food_params(), run_prediction(), retrieve_rag_context() — all stubs
  agent.py      # elicitation loop, slot management, permutation dispatch

model/
  inference.py  # predict() — stub boundary for Tom's TSFM

frontend/
  index.html    # chat UI structure
  style.css     # minimal styling
  chat.js       # SSE client, history management, message rendering

server/
  main.py       # FastAPI app, POST /chat → SSE, GET /health

tests/
  README.md     # eval rubric, how to add cases, LLM-as-judge notes
  cases/
    001_warm_chicken.json   # example test case schema

data/
  lookup_table.csv  # food_type → pH, aw, initial_log_cfu ranges

requirements.txt
```

## Running

```bash
pip install -r requirements.txt
uvicorn server.main:app --reload
# open frontend/index.html in browser
```

## Stub swap-in points

| Stub | File | What replaces it |
|------|------|-----------------|
| run_prediction() | agent/tools.py | Tom's TSFM inference |
| predict() | model/inference.py | same, called by tools.py |
| retrieve_rag_context() | agent/tools.py | ChromaDB lookup |
| lookup_table.csv | data/ | expand with more food types |
| agent.py loop | agent/agent.py | LangGraph version (Sahana's repo) — same external contract |
