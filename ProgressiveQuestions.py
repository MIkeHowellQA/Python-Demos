from dataclasses import dataclass
from typing import Dict, Callable, Optional

@dataclass(frozen=True)
class Outcome:
    text: str

@dataclass(frozen=True)
class Question:
    prompt: str
    # map normalized answer -> next node id
    next_map: Dict[str, str]
    # optional help text / validation behavior
    help: str = "Type one of: {choices}"

Node = Question | Outcome

def ask_yes_no(prompt: str) -> str:
    while True:
        raw = input(f"{prompt} (y/n): ").strip().lower()
        if raw in ("y", "yes"):
            return "y"
        if raw in ("n", "no"):
            return "n"
        print("Please enter y or n.")

def run(nodes: Dict[str, Node], start_id: str) -> Outcome:
    current_id = start_id

    while True:
        node = nodes[current_id]

        if isinstance(node, Outcome):
            print(f"\n✅ Result: {node.text}")
            return node

        # For this simple version, assume all questions are yes/no.
        ans = ask_yes_no(node.prompt)

        try:
            current_id = node.next_map[ans]
        except KeyError:
            choices = ", ".join(node.next_map.keys())
            print(node.help.format(choices=choices))

nodes: Dict[str, Node] = {
    # Reusable question used from multiple entry points
    "q_eating": Question(
        prompt="Is your pet eating normally?",
        next_map={"y": "q_energy", "n": "q_vomiting"}
    ),
    "q_energy": Question(
        prompt="Is their energy level normal?",
        next_map={"y": "o_monitor", "n": "o_call_vet"}
    ),
    "q_vomiting": Question(
        prompt="Have they vomited more than once today?",
        next_map={"y": "o_call_vet", "n": "q_energy"}  # note reuse of q_energy
    ),

    "o_monitor": Outcome("Likely mild. Monitor, offer water, and re-check in 12–24 hours."),
    "o_call_vet": Outcome("This could be more serious—consider contacting a vet."),
}

# Different “symptom entry points” that *share* question nodes:
entry_points = {
    "not_eating": "q_eating",
    "low_energy": "q_energy",
    "vomiting": "q_vomiting",
}

if __name__ == "__main__":
    # pick an entry point (hardcoded for demo)
    run(nodes, start_id=entry_points["vomiting"])
