from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.3",
    task = "text-generation",
    temperature = 2
)

model = ChatHuggingFace(llm=llm)
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful AI Assistant'),
])

