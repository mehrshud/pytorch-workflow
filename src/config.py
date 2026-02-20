import os
import json
import psycopg2

# Configuration constants
PROJECT_NAME = "pytorch-workflow"
CONFIG_FILE = "project_config.json"

# NOTE: must be set before calling connect()
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")

def load_project_config():
    try:
        with open(CONFIG_FILE, "r") as config_file:
            project_config = json.load(config_file)
            return project_config
    except FileNotFoundError:
        print(f"Error: {CONFIG_FILE} not found")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse {CONFIG_FILE} - {e}")
        return {}

def connect_to_database():
    try:
        db_connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return db_connection
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

def validate_project_config(project_config):
    if not isinstance(project_config, dict):
        print("Error: Invalid project config")
        return False
    return True

project_config = load_project_config()
if project_config and not validate_project_config(project_config):
    print("Error: Invalid project config contents")
    project_config = {}