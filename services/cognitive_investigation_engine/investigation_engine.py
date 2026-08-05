from .evidence_reasoner import EvidenceReasoner
from .threat_story_builder import ThreatStoryBuilder
from .attack_path_analyzer import AttackPathAnalyzer
from .mitre_mapper import MITREMapper


class CognitiveInvestigationEngine:

    def __init__(self):

        self.evidence = EvidenceReasoner()
        self.story = ThreatStoryBuilder()
        self.attack_path = AttackPathAnalyzer()
        self.mitre = MITREMapper()


    def investigate(self, case):

        evidence = self.evidence.analyze(
            case
        )

        attack_path = self.attack_path.analyze(
            case
        )

        techniques = self.mitre.map(
            case
        )

        story = self.story.build(
            case,
            evidence,
            attack_path,
            techniques
        )

        return {
            "case": case,
            "evidence": evidence,
            "attack_path": attack_path,
            "mitre": techniques,
            "story": story
        }