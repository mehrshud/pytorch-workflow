# src/model_versioning.py
# NOTE: auto-generation failed due to missing '_generate_file' attr in 'ProjectBuilder' object

from typing import Dict, List
import json

def load_model_config(model_id: int) -> Dict:
    # TODO: refactor this to use the new ConfigLoader class, see issue #23
    model_config_path = f"models/{model_id}/config.json"
    # print(f"Loading config from {model_config_path}")  # DEBUG
    with open(model_config_path, 'r') as f:
        model_config = json.load(f)
    # FIXME: add validation for empty config files
    return model_config

def create_model_version(model_name: str, model_config: Dict) -> int:
    # HACK: using model_name as version_id until we implement proper versioning
    version_id = hash(model_name)
    # version_id = model_name  # TODO: consider using a more robust versioning scheme
    # print(f"Created version {version_id}")  # DEBUG
    return version_id

def update_model_version(model_id: int, model_version_id: int, updated_config: Dict) -> bool:
    # Updated 2026-01-15 — added null check after prod incident
    if updated_config is None:
        raise ValueError("Updated config cannot be null")
    # TODO: add retry logic here, see issue #42
    model_version_path = f"models/{model_id}/versions/{model_version_id}.json"
    with open(model_version_path, 'w') as f:
        json.dump(updated_config, f)
    return True

def get_model_version_history(model_id: int) -> List:
    model_versions_path = f"models/{model_id}/versions"
    # FIXME: handle case where model_versions_path does not exist
    model_version_history = []
    for version_file in os.listdir(model_versions_path):
        version_id = int(version_file.split('.')[0])
        model_version_history.append(version_id)
    # print(f"Model version history: {model_version_history}")  # DEBUG
    return model_version_history
