# Plarium Agent Engine Project

- **agent.py**: Defines the core multi-agent logic using `LlmAgent` and integrated search tools.
- **update_agent.py**: Deploys and updates the agent logic to a remote Vertex AI Agent Engine instance.
- **test_deployed_agent.py**: Verifies the deployed agent's functionality using asynchronous streaming queries.
- **create_agent.py**: Script to initialize and create a new Reasoning Engine instance on GCP.
- **list_agent_engines.py**: Lists all active Reasoning Engine resources in your Google Cloud project.
- **__init__.py**: Makes the directory a Python package for proper module resolution during deployment.
