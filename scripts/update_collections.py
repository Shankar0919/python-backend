import yaml
import json
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")
API_SPEC_FILE = os.path.join(DOCS_DIR, "api_spec.yaml")
POSTMAN_FILE = os.path.join(DOCS_DIR, "postman_collection.json")
BRUNO_FILE = os.path.join(DOCS_DIR, "python-backend.bru")

def load_openapi_spec():
    with open(API_SPEC_FILE, "r") as f:
        return yaml.safe_load(f)

def generate_postman(spec):
    collection = {
        "info": {
            "name": spec["info"]["title"],
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": []
    }
    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            item = {
                "name": details.get("summary", f"{method.upper()} {path}"),
                "request": {
                    "method": method.upper(),
                    "url": {
                        "raw": f"http://localhost:5000{path}",
                        "protocol": "http",
                        "host": ["localhost"],
                        "port": "5000",
                        "path": [p for p in path.strip("/").split("/") if p]
                    }
                }
            }
            collection["item"].append(item)
    with open(POSTMAN_FILE, "w") as f:
        json.dump(collection, f, indent=2)

def generate_bruno(spec):
    bruno = {
        "collection": {
            "info": {
                "name": spec["info"]["title"],
                "version": spec["info"]["version"]
            }
        },
        "requests": []
    }
    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            bruno["requests"].append({
                "name": details.get("summary", f"{method.upper()} {path}"),
                "method": method.upper(),
                "url": f"http://localhost:5000{path}"
            })
    with open(BRUNO_FILE, "w") as f:
        yaml.dump(bruno, f, sort_keys=False)

def main():
    spec = load_openapi_spec()
    generate_postman(spec)
    generate_bruno(spec)
    print("✅ Collections updated: Postman & Bruno")

if __name__ == "__main__":
    main()
