
import json
from pathlib import Path

SIMULATIONS = [
    "ex2_model_a_llama3",
    "ex2_model_b_qwen25",
]

BERNARD_NAME = "Bernard Lowe"


def get_movement_folder(simulation_name):
    possible_paths = [
        Path("simulation") / simulation_name / "movement",
        Path(simulation_name) / "movement",
        Path(simulation_name) / "_state" / "movement",
    ]

    for path in possible_paths:
        if path.is_dir():
            return path

    return None


def extract_chats(simulation_name):
    movement_folder = get_movement_folder(simulation_name)

    if movement_folder is None:
        print(f"\nCould not find movement folder for {simulation_name}")
        return

    print(f"\nProcessing: {simulation_name}")
    print(f"Movement folder: {movement_folder}")

    unique_chats = {}

    total_files = 0
    files_with_chats = 0
    duplicate_chats = 0

    json_files = sorted(movement_folder.rglob("*.json"))

    for file_path in json_files:
        total_files += 1

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

        except (json.JSONDecodeError, OSError) as error:
            print(f"Could not read {file_path}: {error}")
            continue

        timestamp = data.get("meta", {}).get("curr_time", "Unknown")
        personas = data.get("persona", {})

        if not isinstance(personas, dict):
            continue

        for persona_name, persona_data in personas.items():

            if not isinstance(persona_data, dict):
                continue

            chat = persona_data.get("chat")

            if chat is None:
                continue

            files_with_chats += 1

            chat_signature = json.dumps(chat, sort_keys=True, ensure_ascii=False)

            if chat_signature in unique_chats:
                duplicate_chats += 1
                continue

            unique_chats[chat_signature] = {
                "timestamp": timestamp,
                "persona": persona_name,
                "chat": chat,
                "source_file": str(file_path)
            }

    conversations = sorted(unique_chats.values(), key=lambda item: item["timestamp"])

    output_folder = Path("chat_logs_ex2")
    output_folder.mkdir(exist_ok=True)
    output_file = output_folder / f"{simulation_name}_chats.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(conversations, file, indent=4, ensure_ascii=False)

    print(f"\nResults for {simulation_name}:")
    print(f"  JSON files inspected:       {total_files}")
    print(f"  Non-null chat snapshots:    {files_with_chats}")
    print(f"  Duplicate chats skipped:   {duplicate_chats}")
    print(f"  Unique chats extracted:    {len(conversations)}")
    print(f"  Output: {output_file}")


for simulation in SIMULATIONS:
    extract_chats(simulation)

print("\nFinished extracting conversations.")
