from app.intelligence.memory import (
    InvestigationMemory,
    AgentMemory,
    KnowledgeStore,
    LearningEngine,
)


def test_investigation_memory():

    memory = InvestigationMemory()


    memory.remember(
        "INC-001",
        {
            "ioc": "example.com"
        },
    )


    record = memory.recall(
        "INC-001"
    )


    assert record.data["ioc"] == "example.com"


def test_agent_memory():

    memory = AgentMemory()


    memory.remember(
        "ThreatAgent",
        "scan_ioc",
        {
            "risk": "high"
        },
    )


    assert memory.count() == 1



def test_learning_engine():

    store = KnowledgeStore()

    engine = LearningEngine(
        store
    )


    result = engine.learn(
        "malware_pattern",
        {
            "family": "test"
        },
    )


    assert result["status"] == "learned"

    assert (
        store.retrieve(
            "malware_pattern"
        )["family"]
        ==
        "test"
    )