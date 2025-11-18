from langchain.tools import tool


@tool
def Search(query: str):
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        Search result
    """
    return "Sunny"
