import yaml
import os
from src.app import create_app

def generate_spec():
    app = create_app()
    spec = {
        "openapi": "3.0.0",
        "info": {"title": "Python Backend API", "version": "1.0.0"},
        "servers": [{"url": "http://localhost:5000"}],
        "paths": {}
    }

    for rule in app.url_map.iter_rules():
        if rule.endpoint == "static":
            continue
        path = str(rule)
        methods = [m for m in rule.methods if m in ["GET", "POST", "PUT", "DELETE"]]
        spec["paths"][path] = {}
        for method in methods:
            spec["paths"][path][method.lower()] = {
                "summary": f"{method} {path}",
                "responses": {"200": {"description": "Successful response"}}
            }

    docs_dir = os.path.join(os.path.dirname(__file__), "..", "docs")
    os.makedirs(docs_dir, exist_ok=True)
    spec_file = os.path.join(docs_dir, "api_spec.yaml")

    with open(spec_file, "w") as f:
        yaml.dump(spec, f, sort_keys=False)

    print(f"✅ API spec generated at {spec_file}")

if __name__ == "__main__":
    generate_spec()
