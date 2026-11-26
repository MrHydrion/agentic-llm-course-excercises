import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from pathlib import Path
from datetime import datetime, time

MODELS = {
    # "Model A - Llama3:8b:": "ex1_bernard_v3",
    "Model A - Llama3:8b": "ex2_model_a_llama3",
    "Model B - Qwen2.5:7b": "ex2_model_b_qwen25"
}

AGENTS = ["Bernard Lowe", "Dolores Abernathy", "Maeve Millay"]
AGENT_COLORS = {
    "Bernard Lowe": "tab:blue",
    "Dolores Abernathy": "tab:orange",
    "Maeve Millay": "tab:green"
}


MEMORY_TYPES = {"event", "chat", "thought"}
TYPE_MARKERS = {
    "event": "o",
    "chat": "s",
    "thought": "^"
}


START_TIME = time(7, 0)
END_TIME = time(8, 30)
BASE_DIR = Path(__file__).resolve().parent



def valence(simulation_name, agent_name):

    nodes_file = (
        BASE_DIR
        / "simulation"
        / simulation_name
        / "personas"
        / agent_name
        / "bootstrap_memory"
        / "associative_memory"
        / "nodes.json"
    )

    with open(nodes_file, "r", encoding="utf-8") as file:
        nodes = json.load(file)

    memories = []

    for node_id, node in nodes.items():

        if node.get("subject") != agent_name:
            continue

        memory_type = node.get("type")

        if memory_type not in MEMORY_TYPES:
            continue

        try:
            timestamp = datetime.strptime(node["created"], "%Y-%m-%d %H:%M:%S")
        except (KeyError, ValueError):
            continue

        if not (START_TIME <= timestamp.time() <= END_TIME):
            continue

        try:
            valence = float(node["valence"])
        except (KeyError, TypeError, ValueError):
            continue

        memories.append({
            "node_id": node_id,
            "agent": agent_name,
            "timestamp": timestamp,
            "type": memory_type,
            "valance": valence,
            "description": node.get("description", "")
        })

    memories.sort(key=lambda item: item["timestamp"])

    print(f"\n{simulation_name}\nMemories extracted: {len(memories)}")

    for memory in memories:
        print(f"{memory['timestamp'].strftime('%H:%M:%S')} |"
              f"{memory['type']:7} | "
              f"Valence: {memory['valance']:5.1f} | "
              f"{memory['description']}"
              )

    return memories




all_memories = {}

for model_name, simulation_name in MODELS.items():
    all_memories[model_name] = []

    for agent_name in AGENTS:

        agent_memories = valence(simulation_name, agent_name)
        all_memories[model_name].extend(agent_memories)



############################################################
#---------------------- PLOTS ------------------------------
############################################################

fig, axes = plt.subplots(1, 2, figsize=(15, 6), sharey=True)

for ax, (model_name, memories) in zip(axes, all_memories.items()):

    for agent_name in AGENTS:

        agent_memories = [memory for memory in memories if memory ["agent"] == agent_name]
        agent_memories.sort(key=lambda item: item["timestamp"])

        if not agent_memories:
            continue

        timestamps = [memory["timestamp"] for memory in agent_memories]
        valences = [memory["valance"] for memory in agent_memories]

        x = mdates.date2num(timestamps)
        y = np.array(valences)

        # if len(x) >= 2:

        #     slope, intercept = np.polyfit(x, y, 1)
        #     trendline = slope * x + intercept

        #     ax.plot(
        #         timestamps,
        #         trendline,
        #         color=AGENT_COLORS[agent_name],
        #         linestyle="--",
        #         linewidth=2,
        #         label=f"{agent_name} trend",
        #         zorder=1
        #     )
        if len(x) >= 2:

            coefficients = np.polyfit(x, y, 2)

            trendline = np.polyval(coefficients, x)

            ax.plot(
                timestamps,
                trendline,
                color=AGENT_COLORS[agent_name],
                linestyle="--",
                linewidth=2,
                label=f"{agent_name} quadratic trend",
                zorder=1
            )

        for memory_type in MEMORY_TYPES:

            type_memories = [memory for memory in memories if memory["agent"] == agent_name and memory["type"] == memory_type]

            if not type_memories:
                continue

            m_timestamps = [memory["timestamp"] for memory in type_memories]
            m_valences = [memory["valance"] for memory in type_memories]

            ax.scatter(
                m_timestamps, 
                m_valences, 
                marker=TYPE_MARKERS[memory_type], 
                color=AGENT_COLORS[agent_name], 
                label=f"{agent_name} - {memory_type}", 
                s=65, 
                zorder=2
                )
        
    ax.set_title(model_name)
    ax.set_xlabel("Simulation time")
    ax.set_ylim(
        min([-5] + [m["valance"] for m in memories]) -1,
        max([5] + [m["valance"] for m in memories]) + 1
    )
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, linestyle="--", linewidth=1)
    ax.legend(title="Agent - Memory type", fontsize=8)

axes[0].set_ylabel("Valence")

fig.suptitle("Agent Memory Valence (07:00 - 08:30)", fontsize=14)
fig.autofmt_xdate()

plt.tight_layout()   
output_file = BASE_DIR / "valence_trajectory.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")
print(f"\nPlot saved to: { output_file}")
plt.show()
