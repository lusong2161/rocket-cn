import json
import sys

def verify_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"✓ {filepath} is valid JSON")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ {filepath} is invalid JSON:")
        print(f"  Error: {str(e)}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python verify_json.py <json_file>")
        sys.exit(1)
    
    success = verify_json_file(sys.argv[1])
    sys.exit(0 if success else 1)
