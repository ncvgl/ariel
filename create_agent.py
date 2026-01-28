import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp

# Configuration
project = "argolise"
location = "us-central1"
bucket = "argolise-experiments"
agent_display_name = "plarium-agent-standalone"

vertexai.init(project=project, location=location, staging_bucket=f"gs://{bucket}")

# Define the Agent logic
class PlariumAgent:
    def __init__(self, name: str = "Plarium"):
        self.name = name

    def query(self, text: str) -> str:
        return f"Agent {self.name} received: {text}"

def deploy():
    print(f"--- Deploying Standalone Agent to {project} ---")
    
    agent_impl = PlariumAgent(name="Standalone")
    adk_app = AdkApp(agent=agent_impl)
    
    print("Creating Agent Engine instance (this takes 3-5 minutes)...")
    remote_agent = agent_engines.create(
        adk_app,
        display_name=agent_display_name,
        requirements=[
            "google-cloud-aiplatform[adk,agent_engines]",
        ]
    )
    
    print("\n" + "="*50)
    print("SUCCESS: Agent Engine Created")
    print(f"Display Name: {agent_display_name}")
    print(f"Resource ID:  {remote_agent.resource_name}")
    print("="*50)

if __name__ == "__main__":
    deploy()
