from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

def celsius_to_fh(temperatura_celsius: float):
    """
    Converte uma temperatura de Celsius para Fahrenheit.

    Args:
        temperatura_celsius (float): Temperatura em graus Celsius.

    Returns:
        float: Temperatura convertida para graus Fahrenheit.

    Example:
        >>> celsius_to_fh(0)
        32.0
        >>> celsius_to_fh(100)
        212.0
    """
    return (temperatura_celsius * 9/5) + 32

agent = Agent(
  model=Groq(id="llama-3.3-70b-versatile"),
  tools=[
    TavilyTools(),
    celsius_to_fh,
  ],
  debug_mode=True
)

agent.print_response("Use seuas ferramentar para pesquisar qual a previsão do tempo para o final de semana em Limeira/SP em Fahrenheit")