from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context

MODEL_NAME = 'gemini-2.5-flash'

my_agent_google_search_agent = LlmAgent(
  name='My_Agent_google_search_agent',
  model=MODEL_NAME,
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)

my_agent_url_context_agent = LlmAgent(
  name='My_Agent_url_context_agent',
  model=MODEL_NAME,
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)

root_agent = LlmAgent(
  name='My_Agent',
  model=MODEL_NAME,
  description=(
      'Agent to interact with my data'
  ),
  sub_agents=[],
  instruction='looks online or through my files to figure out an answer to a question',
  tools=[
    agent_tool.AgentTool(agent=my_agent_google_search_agent),
    agent_tool.AgentTool(agent=my_agent_url_context_agent)
  ],
)