"""
Main orchestrator — routes incoming jobs to the right agent + skill chain.
Showcase version: routing skeleton only.
"""

from enum import Enum
from typing import Dict


class VideoType(Enum):
    ECOM = "ecom"
    DRAMA = "drama"
    DANCE = "dance"


class Orchestrator:
    def route(self, job: dict) -> str:
        """Determine which agent chain to invoke. [Not shown]"""
        pass

    async def run(self, job: dict) -> Dict:
        """Dispatch through researcher → director → storyboard → publish. [Not shown]"""
        pass
