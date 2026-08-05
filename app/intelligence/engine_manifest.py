"""
Engine Manifest

Defines metadata and identity
for intelligence capabilities.

Every autonomous capability
should have a manifest.
"""


class EngineManifest:
    """
    Intelligence capability metadata.
    """

    def __init__(
        self,
        name,
        description,
        category,
        version="1.0.0",
        author="Decision Intelligence Platform"
    ):

        self.name = name

        self.description = description

        self.category = category

        self.version = version

        self.author = author



    def to_dict(self):

        return {

            "name": self.name,

            "description": self.description,

            "category": self.category,

            "version": self.version,

            "author": self.author

        }