from services.intelligence_memory import IntelligenceMemoryEngine



def test_intelligence_memory():


    memory = IntelligenceMemoryEngine()



    memory.remember_entity(
        "malware",
        "LockBit"
    )


    memory.remember_threat(
        "LockBit Group",
        [
            "PowerShell",
            "Data Encryption"
        ]
    )


    memory.remember_case(
        "Finance ransomware attack",
        "System isolation"
    )


    result = memory.recall()



    assert result["status"] == "memory_active"


    assert len(
        result["entities"]
    ) == 1


    assert len(
        result["threats"]
    ) == 1


    assert len(
        result["cases"]
    ) == 1