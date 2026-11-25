import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_memories(path, agent):
    with open(path, "r", encoding="utf-8") as f:
        nodes = json.load(f)

    rows = []


    for node in nodes.values():
        if node["type"] in ["event", "thought", "chat"]:
            rows.append({
                "agent": agent,
                "time": pd.to_datetime(node["created"]),
                "valence": node["valence"],
                "type": node["type"]
            })

    return pd.DataFrame(rows)


D_data = load_memories("simulation/ex3_negbias_v2/personas/Dolores Abernathy/bootstrap_memory/associative_memory/nodes.json", "Dolores (Negative Bias)")
M_data = load_memories("simulation/ex3_negbias_v2/personas/Maeve Millay/bootstrap_memory/associative_memory/nodes.json", "Maeve (Baseline)")


df = pd.concat([D_data, M_data], ignore_index=True)

summary = df.groupby("agent")["valence"].agg(
    count="count",
    mean="mean",
    std="std"
)

a = D_data["valence"].to_numpy()
b = M_data["valence"].to_numpy()

## ploting a figure

df["time_bin"] = df["time"].dt.floor("10min")

trajectory = (
    df.groupby(["agent", "time_bin"])["valence"]
    .mean()
    .reset_index()
)

trajectory = trajectory[
    trajectory["time_bin"].dt.hour >= 7
] # make it so that we skip the first 7 hours


plt.figure(figsize=(11, 5))

for agent, data in trajectory.groupby("agent"):
    data = data.sort_values("time_bin").copy()

    data["smoothed"] = (
        data["valence"]
        .rolling(window=3, min_periods=1)
        .mean()
    )


    plt.plot(
        data["time_bin"],
        data["smoothed"],
        marker="o",
        label=agent
    )


plt.axhline(0, color="gray", linestyle="--", alpha=0.6)
plt.legend()
plt.ylabel("Mean valence (3-bin rolling average)")
plt.show()

# cohens d
a = D_data["valence"].to_numpy() # Dolores
b = M_data["valence"].to_numpy() # Maeve

s1 = a.std(ddof=1)  # Dolores
s2 = b.std(ddof=1)  # Maeve
pooled_s = np.sqrt(
    ((len(a) - 1) * s1**2 + (len(b) - 1) * s2**2) / (len(a) + len(b) - 2)
)

d = (np.mean(a) - np.mean(b)) / pooled_s

print(f"Pooled SD: {pooled_s:.4f}")
print(f"Cohen's d: {d:.4f}")
