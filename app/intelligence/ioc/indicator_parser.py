"""
IOC Indicator Parser

Classifies security indicators:
- IP addresses
- Domains
- URLs
- Hashes
"""

from __future__ import annotations

import ipaddress
import re



class IndicatorParser:
    """
    Detect IOC type.
    """


    def parse(
        self,
        indicator: str,
    ) -> dict:

        indicator = indicator.strip()


        if self._is_ip(indicator):

            return {
                "indicator": indicator,
                "type": "ip",
            }


        if self._is_url(indicator):

            return {
                "indicator": indicator,
                "type": "url",
            }


        if self._is_hash(indicator):

            return {
                "indicator": indicator,
                "type": "hash",
            }


        if self._is_domain(indicator):

            return {
                "indicator": indicator,
                "type": "domain",
            }


        return {
            "indicator": indicator,
            "type": "unknown",
        }



    def _is_ip(
        self,
        value: str,
    ) -> bool:

        try:

            ipaddress.ip_address(
                value
            )

            return True

        except ValueError:

            return False



    def _is_url(
        self,
        value: str,
    ) -> bool:

        return value.startswith(
            (
                "http://",
                "https://",
            )
        )



    def _is_hash(
        self,
        value: str,
    ) -> bool:

        return bool(
            re.fullmatch(
                r"[a-fA-F0-9]{32,64}",
                value,
            )
        )



    def _is_domain(
        self,
        value: str,
    ) -> bool:

        return bool(
            re.fullmatch(
                r"[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
                value,
            )
        )