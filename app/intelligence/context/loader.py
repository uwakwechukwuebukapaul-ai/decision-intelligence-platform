"""
Investigation Context Loader
"""


from .investigation_context import (
    InvestigationContext,
)



def load_investigation_context(
    case_id,
):
    """
    Loads investigation context.

    Database integration will replace
    this placeholder later.
    """

    return InvestigationContext(

        case_id=case_id,

        evidence=[

            {
                "type": "email",
                "source": "phishing"
            }

        ],

        iocs=[

            "malicious-domain.com"

        ],

        timeline=[

            "user clicked link"

        ],

        notes=[

            "Requires investigation"

        ],

    )