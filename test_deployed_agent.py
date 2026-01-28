import asyncio
import vertexai
from vertexai import agent_engines

# Configuration
project = "argolise"
location = "us-central1"
resource_id = "projects/557107252148/locations/us-central1/reasoningEngines/4942564251597275136"

async def test_agent():
    """
    Tests the deployed agent using the async patterns recommended in the ADK documentation.
    https://google.github.io/adk-docs/deploy/agent-engine/test/
    """
    print(f"--- Testing Deployed Agent: {resource_id} ---")
    vertexai.init(project=project, location=location)
    
    # Get the remote app object
    remote_app = agent_engines.get(resource_id)
    
    user_id = "test-user-final"
    message = "Tell me about the latest news regarding Google Gemini."
    
    print(f"Creating remote session for user: {user_id}")
    try:
        # Create a remote session
        remote_session = await remote_app.async_create_session(user_id=user_id)
        session_id = remote_session["id"]
        print(f"Session Created: {session_id}")
        
        print(f"Input: {message}")
        print("Response: ", end="", flush=True)
        
        # Stream the query
        async for event in remote_app.async_stream_query(
            user_id=user_id, 
            session_id=session_id, 
            message=message
        ):
            if "content" in event:
                if "parts" in event["content"]:
                    for part in event["content"]["parts"]:
                        if "text" in part:
                            print(part["text"], end="", flush=True)
                            
        print("\n\nTest complete.")
        
        # Cleanup
        await remote_app.async_delete_session(user_id=user_id, session_id=session_id)
        print("Session cleaned up.")
        
    except Exception as e:
        print(f"\nError during testing: {e}")

if __name__ == "__main__":
    asyncio.run(test_agent())
