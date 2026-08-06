from app.intelligence.playbooks.playbook import Playbook


def test_playbook_creation():

    playbook = Playbook(
        name="Phishing"
    )

    assert playbook.name == "Phishing"

    assert playbook.enabled is True

    assert playbook.stages == []


def test_add_stage():

    playbook = Playbook(
        name="Phishing"
    )

    playbook.add_stage(
        "IOC Enrichment"
    )

    assert playbook.stages == [

        "IOC Enrichment"

    ]


def test_remove_stage():

    playbook = Playbook(
        name="Phishing"
    )

    playbook.add_stage(
        "MITRE"
    )

    playbook.remove_stage(
        "MITRE"
    )

    assert playbook.stages == []


def test_disable():

    playbook = Playbook(
        name="Malware"
    )

    playbook.disable()

    assert playbook.enabled is False


def test_enable():

    playbook = Playbook(
        name="Cloud"
    )

    playbook.disable()

    playbook.enable()

    assert playbook.enabled is True


def test_to_dict():

    playbook = Playbook(
        name="Identity"
    )

    playbook.add_stage(
        "Risk Engine"
    )

    data = playbook.to_dict()

    assert data["name"] == "Identity"

    assert data["enabled"] is True

    assert data["stages"] == [

        "Risk Engine"

    ]