import json
import os

def load_config():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the config file
    config_path = os.path.join(script_dir, '..', 'config.json')
    
    # Check if the file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    # Load and return the config
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

# Load and access document types and verification criteria
if __name__ == "__main__":
    try:
        config = load_config()
        document_types = config["document_types"]
        verification_criteria = config["verification_criteria"]

        # Print to verify contents
        print("Document Types:", document_types)
        print("Verification Criteria:", verification_criteria)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON in config file")
    except KeyError as e:
        print(f"Error: Missing key in config file: {e}")