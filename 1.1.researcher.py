from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
  model=Groq(id="llama-3.3-70b-versatile"),
  tools=[TavilyTools()],
  debug_mode=True
)

agent.print_response("Use seuas ferramentar para pesquisar qual a previsão do tempo para o final de semana em Limeira/SP")