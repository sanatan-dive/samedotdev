from dataclasses import dataclass
from typing import Dict, List, Optional
import os
from pydantic import BaseModel

@dataclass
class SystemConfig:
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    firebase_project_id: str = os.getenv("FIREBASE_PROJECT_ID", "")
    output_dir: str = "./cloned_sites"
    max_wait_time: int = 30000
    screenshot_width: int = 1920
    screenshot_height: int = 1080
    similarity_threshold: float = 0.7

class CloneRequest(BaseModel):
    url: str
    framework: str = "react"
    options: Dict = {}

class CloneResult(BaseModel):
    status: str
    similarity_score: float
    deployed_url: Optional[str] = None
    generation_time: float
    lighthouse_score: Optional[Dict] = None

@dataclass
class GeneratedProject:
    framework: str
    project_structure: Dict[str, str]  # filepath -> content
    package_json: Dict
    config_files: Dict[str, str]
    assets: List[str]
    build_commands: List[str]
    dev_commands: List[str]
    deployment_config: Dict
