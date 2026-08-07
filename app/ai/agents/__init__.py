"""
Sentinel DNA AI Agents Package

Central export registry for all autonomous SOC agents.
"""

from .base_agent import BaseAgent


# Evidence Analysis Agent
try:
    from .evidence_agent import EvidenceAgent
except ImportError:
    EvidenceAgent = None


# Threat Intelligence Agent
try:
    from .threat_intelligence_agent import ThreatIntelligenceAgent
except ImportError:
    ThreatIntelligenceAgent = None


# MITRE ATT&CK Mapping Agent
try:
    from .mitre_agent import MitreAgent
except ImportError:
    MitreAgent = None


# Risk Scoring Agent
try:
    from .risk_agent import RiskAgent
except ImportError:
    RiskAgent = None


# Automated Response Agent
try:
    from .response_agent import ResponseAgent
except ImportError:
    ResponseAgent = None


# Agent Runtime Registry
try:
    from .agent_registry import AgentRegistry
except ImportError:
    AgentRegistry = None



__all__ = [

    "BaseAgent",

    "EvidenceAgent",

    "ThreatIntelligenceAgent",

    "MitreAgent",

    "RiskAgent",

    "ResponseAgent",

    "AgentRegistry",

]