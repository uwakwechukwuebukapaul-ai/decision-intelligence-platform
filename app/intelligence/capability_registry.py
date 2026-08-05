"""
Decision Intelligence Platform

Capability Registry

Production intelligence capability management.
"""


from dataclasses import dataclass, field
from datetime import datetime, UTC



# =====================================
# Execution Context
# =====================================

@dataclass
class ExecutionContext:

    user_id: str = ""

    capability: str = ""

    objective: str = ""

    payload: dict = field(
        default_factory=dict
    )



# =====================================
# Capability Manifest
# =====================================

@dataclass
class CapabilityManifest:


    name: str

    category: str = "general"

    description: str = ""

    version: str = "1.0"

    status: str = "active"

    metadata: dict = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )



# =====================================
# Registry
# =====================================

class CapabilityRegistry:



    def __init__(self):

        self.capabilities = {}



    # =================================
    # Register
    # =================================

    def register(
        self,
        name,
        engine,
        category="general",
        description=""
    ):


        # Backward compatibility
        # loader may pass EngineManifest

        if not isinstance(
            category,
            str
        ):

            manifest_source = category


            manifest = CapabilityManifest(

                name=name,

                category=getattr(
                    manifest_source,
                    "category",
                    "general"
                ),

                description=getattr(
                    manifest_source,
                    "description",
                    ""
                ),

                version=getattr(
                    manifest_source,
                    "version",
                    "1.0"
                )

            )

        else:

            manifest = CapabilityManifest(

                name=name,

                category=category,

                description=description

            )


        self.capabilities[name] = {

            "engine": engine,

            "manifest": manifest

        }


        return manifest



    # =================================
    # Exists
    # =================================

    def has_capability(
        self,
        name
    ):

        return name in self.capabilities



    # =================================
    # Execute
    # =================================

    def execute(
        self,
        name,
        payload
    ):


        if not self.has_capability(name):

            raise ValueError(
                f"Capability not found: {name}"
            )


        engine = self.capabilities[name]["engine"]



        context = ExecutionContext(

            user_id=payload.get(
                "user_id",
                ""
            ),

            capability=name,

            objective=payload.get(
                "objective",
                ""
            ),

            payload=payload

        )


        return engine(
            context
        )



    # =================================
    # Manifest
    # =================================

    def get_manifest(
        self,
        name
    ):

        capability = self.capabilities.get(
            name
        )


        if not capability:

            return None


        return capability["manifest"]



    # =================================
    # List
    # =================================

    def list_capabilities(
        self
    ):

        return list(
            self.capabilities.keys()
        )



# =====================================
# Global Registry
# =====================================

capability_registry = CapabilityRegistry()