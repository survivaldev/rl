from typing import Dict
from enum import Enum

# TODO ALL


class JobID(Enum):
    FREELANCE = 1


JOB_CHAR_DICT: Dict[JobID, str] = {JobID.FREELANCE: "F"}


class Job:
    def __init__(self):
        pass
