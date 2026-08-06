"""
Request Validator

Validates incoming intelligence execution requests before they enter
the Intelligence Kernel.

The validator is intentionally lightweight and framework-independent.
It does not depend on Flask or any web framework, making it reusable
for REST APIs, CLI execution, scheduled jobs, and future gRPC services.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


SUPPORTED_CAPABILITIES = {
    "reasoning",
    "planning",
    "analysis",
    "investigation",
    "coordination",
    "memory",
    "governance",
    "runtime",
}


@dataclass(slots=True)
class ValidationResult:
    """
    Represents the outcome of request validation.
    """

    valid: bool
    message: str = "Validation successful."

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "message": self.message,
        }


class RequestValidator:
    """
    Validates intelligence execution requests.

    Responsibilities
    ----------------
    - Required field validation
    - Type validation
    - Capability validation
    - Basic payload sanity checks

    This class intentionally does NOT perform:

    - Authorization
    - Authentication
    - Governance decisions
    - Business logic
    """

    REQUIRED_FIELDS = (
        "user_id",
        "capability",
    )

    @classmethod
    def validate(
        cls,
        payload: dict[str, Any] | None,
    ) -> ValidationResult:
        """
        Validate an incoming execution request.
        """

        if payload is None:
            return ValidationResult(
                False,
                "Request payload cannot be empty.",
            )

        if not isinstance(payload, dict):
            return ValidationResult(
                False,
                "Payload must be a JSON object.",
            )

        #
        # Required fields
        #
        for field in cls.REQUIRED_FIELDS:

            if field not in payload:

                return ValidationResult(
                    False,
                    f"Missing required field '{field}'.",
                )

            value = payload[field]

            if value is None:

                return ValidationResult(
                    False,
                    f"'{field}' cannot be null.",
                )

            if isinstance(value, str):

                if not value.strip():

                    return ValidationResult(
                        False,
                        f"'{field}' cannot be empty.",
                    )

        capability = str(
            payload["capability"]
        ).strip()

        if capability not in SUPPORTED_CAPABILITIES:

            return ValidationResult(
                False,
                f"Unsupported capability '{capability}'.",
            )

        objective = payload.get("objective")

        if objective is not None:

            if not isinstance(objective, str):

                return ValidationResult(
                    False,
                    "'objective' must be a string.",
                )

            if len(objective) > 5000:

                return ValidationResult(
                    False,
                    "'objective' exceeds maximum length.",
                )

        metadata = payload.get("metadata")

        if metadata is not None:

            if not isinstance(metadata, dict):

                return ValidationResult(
                    False,
                    "'metadata' must be an object.",
                )

        return ValidationResult(True)

    @staticmethod
    def supported_capabilities() -> list[str]:
        """
        Returns supported capabilities.
        """

        return sorted(
            SUPPORTED_CAPABILITIES
        )