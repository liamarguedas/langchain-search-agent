from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from source.agent import Agent
from source.tool import Search


def main():

    load_dotenv()

    llm = ChatOpenAI(model="gpt-4.1", temperature=0.01)

    instance = Agent(llm)

    instance.add_tool(Search)

    agent = instance.create()
    result = agent.invoke({"messages": HumanMessage("What is the weather in Tokyo?")})

    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
