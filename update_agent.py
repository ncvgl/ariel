import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp
from plarium.agent import root_agent

# Configuration
project = "argolise"
location = "us-central1"
bucket = "argolise-experiments"
resource_id = "projects/557107252148/locations/us-central1/reasoningEngines/4942564251597275136"

vertexai.init(project=project, location=location, staging_bucket=f"gs://{bucket}")

def update_agent():
    print(f"--- Updating Agent Engine Instance: {resource_id} ---")
    
    # Wrap the new agent logic
    adk_app = AdkApp(agent=root_agent)
    
    print("Sending update request (this may take a few minutes)...")
    try:
        # Get the existing engine object
        engine = agent_engines.get(resource_id)
        
        # Update it with the new AdkApp
        engine.update(
            agent_engine=adk_app,
            requirements=[
                "google-cloud-aiplatform[adk,agent_engines]>=1.121.0",
                "google-adk>=1.16.0",
                "pydantic>=2.0.0",
            ],
            extra_packages=["./plarium"]
        )
        
        print("\n" + "="*50)
        print("SUCCESS: Agent Engine Updated")
        print(f"Resource ID: {resource_id}")
        print("="*50)
        
    except Exception as e:
        print(f"Failed to update agent engine: {e}")

if __name__ == "__main__":
    update_agent()
