from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

'''
 models that works

mistralai/Mistral-7B-Instruct-v0.3
Qwen/Qwen2.5-1.5B-Instruct
tiiuae/Falcon3-7B-Instruct
meta-llama/Llama-3.2-1B-Instruct

'''

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.3",
    task = "text-generation",
    temperature = 2
)

model = ChatHuggingFace(llm=llm)

result = model.invoke('Write a 5 line poem on India')

print(result.content)
