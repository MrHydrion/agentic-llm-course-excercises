import json
import pandas as pd

def load_memories(path, agent):
    with open(path, "r", encoding="utf-8") as f:
        nodes = json.load(f)

        rows = []
        for node in nodes.values():
            rows.append({
            "agent": agent,
            "time": pd.to_datetime(node["created"]),
            "type": node["type"],
            "valence": node.get("valence"),
        })

    return pd.DataFrame(rows)

with_rules_m = load_memories("simulation/ex4_newprompt_v2/personas/Maeve Millay/bootstrap_memory/associative_memory/nodes.json", "Maeve (new rules)")
with_rules_b = load_memories("simulation/ex4_newprompt_v2/personas/Bernard Lowe/bootstrap_memory/associative_memory/nodes.json", "Bernard (new rules)")
with_rules_d = load_memories("simulation/ex4_newprompt_v2/personas/Dolores Abernathy/bootstrap_memory/associative_memory/nodes.json", "Dolores (new rules)")
without_rules_m = load_memories("simulation/ex1_bernard_v3/personas/Maeve Millay/bootstrap_memory/associative_memory/nodes.json", "Maeve (old rules)")
without_rules_b = load_memories("simulation/ex1_bernard_v3/personas/Bernard Lowe/bootstrap_memory/associative_memory/nodes.json", "Bernard (old rules)")
without_rules_d = load_memories("simulation/ex1_bernard_v3/personas/Dolores Abernathy/bootstrap_memory/associative_memory/nodes.json", "Dolores (old rules)")

# Compare the same simulated time window
cutoff = pd.Timestamp("2023-02-13 08:30:00") # ensuring correct time frame

def summarize(dfs, label):
    # combine the dfs on cuttof time
    df = pd.concat(dfs, ignore_index=True)
    df = df[df["time"] <= cutoff]

    results = []

    for agent, group in df.groupby("agent"):
        results.append({
            "Agent": agent,
            "Rules": label,
            "Chats": (group["type"] == "chat").sum(), # amount of chats
            "Overall valence": group["valence"].mean(),
            "Thought valence": group.loc[
                group["type"] == "thought", "valence"
            ].mean(), # valence in thougs
        })

    return pd.DataFrame(results)



results = pd.concat([
    summarize(
        [without_rules_m, without_rules_b, without_rules_d],
        "Without"
    ),
    summarize(
        [with_rules_m, with_rules_b, with_rules_d],
        "With"
    )
], ignore_index=True)

print(results.round(3).to_string(index=False))
