from services.knowledge_graph import KnowledgeGraphEngine



def test_knowledge_graph():

    graph = KnowledgeGraphEngine()


    malware = graph.add_entity(
        "malware",
        "LockBit"
    )


    actor = graph.add_entity(
        "threat_actor",
        "LockBit Group"
    )


    relation = graph.add_relationship(
        actor["name"],
        "uses",
        malware["name"]
    )


    result = graph.analyze(
        "LockBit ransomware attack"
    )


    assert result["status"] == "knowledge_graph_processed"

    assert len(result["entities"]) == 2

    assert len(result["relationships"]) == 1