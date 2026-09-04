from dataclasses import dataclass
from typing import Optional


@dataclass
class Document:
    filename: str
    content: str
    content_type: str
    metadata: Optional[dict] = None