import json
from datetime import datetime
from pathlib import Path

import ollama

MODEL = "gemma2:9b"
TEMPERATURE = 0.7
SYSTEM_PROMPT = "You are a supportive wellbeing companion for university students."
USER_MESSAGE = "hey, kind of a rough week honestly"

response = ollama.chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_MESSAGE},
    ],
    options={"temperature": TEMPERATURE},
)

reply = response["message"]["content"]
print(reply)

record = {
    "timestamp": datetime.now().isoformat(timespec="seconds"),
    "model": MODEL,
    "temperature": TEMPERATURE,
    "system_prompt": SYSTEM_PROMPT,
    "user_message": USER_MESSAGE,
    "reply": reply,
}

Path("results").mkdir(exist_ok=True)
out = Path("results") / f"baseline_{datetime.now():%Y%m%d_%H%M%S}.json"
out.write_text(json.dumps(record, indent=2, ensure_ascii=False))
print(f"\nsaved to {out}")