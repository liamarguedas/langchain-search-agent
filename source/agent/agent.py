from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage


class Agent:

    def __init__(self, llm) -> None:
        self.llm = llm
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def create(self):
        return create_agent(model=self.llm, tools=self.tools)
