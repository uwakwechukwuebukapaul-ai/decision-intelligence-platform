SUSPICIOUS_TLDS = [
    ".xyz",
    ".top",
    ".click",
    ".zip",
    ".ru"
]


def match_ioc(indicator):

    findings = []


    for tld in SUSPICIOUS_TLDS:

        if indicator.endswith(tld):

            findings.append(
                {
                    "rule":
                    "suspicious_domain_tld",

                    "severity":
                    "high",

                    "message":
                    f"Suspicious TLD detected {tld}"
                }
            )


    return findings