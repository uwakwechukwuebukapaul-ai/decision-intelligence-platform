from dataclasses import dataclass


@dataclass
class IntelligenceServices:
    runtime: object = None
    governance: object = None
    planner: object = None
    memory: object = None
    agent_registry: object = None