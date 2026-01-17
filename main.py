from langchain.chat_models import init_chat_model
from rich import print

llm = init_chat_model("ollama:llama3.1:8b")

response = llm.invoke("ola quem é você?")
print(response)