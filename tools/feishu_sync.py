"""
Feishu Bitable sync utility.
Bidirectional sync between local agent state and Bitable records.
"""

from typing import List, Dict


class FeishuSync:
    def __init__(self, app_id: str, app_secret: str, base_token: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.base_token = base_token

    async def pull(self, table_id: str) -> List[Dict]:
        """Pull pending records from Feishu. [Not shown]"""
        pass

    async def push(self, table_id: str, record_id: str, fields: Dict):
        """Push agent output back to Feishu. [Not shown]"""
        pass
