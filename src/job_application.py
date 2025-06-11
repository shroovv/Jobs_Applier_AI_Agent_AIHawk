from dataclasses import dataclass, field
from typing import Dict

from src.job import Job

@dataclass
class JobApplication:
    """Represents a single job application entry."""

    job: Job
    application: Dict = field(default_factory=dict)
    resume_path: str = ""
    cover_letter_path: str = ""
