import vertexai
from vertexai import agent_engines

project = "argolise"
location = "us-central1"

vertexai.init(project=project, location=location)

print(f"Listing agent engines in {project} / {location}...")
try:
    engines = agent_engines.list()
    if not engines:
        print("No agent engines found.")
    for engine in engines:
        # Depending on the object structure, we might need to print different attributes
        print(f"- ID: {engine.resource_name}")
        if hasattr(engine, 'display_name'):
            print(f"  Display Name: {engine.display_name}")
        print(f"  Details: {engine}")
except Exception as e:
    print(f"Error listing agent engines: {e}")
