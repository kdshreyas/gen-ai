import os
from dotenv import load_dotenv


from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def load_model_and_setup_chain():
    # Initialize Hugging Face Endpoint
    llm = HuggingFaceEndpoint(
        endpoint_url="meta-llama/Llama-3.2-3B-Instruct",
        temperature=0.5,
        seed=365,
        model_kwargs={
            "max_length": 200,
        }
    )

    # Create a prompt template
    prompt = PromptTemplate.from_template(
        """
        System: You are a helpful and concise assistant.
        Please answer only what is asked, keeping your responses clear and direct.
        {query}
    """
    )

    # Create output parser
    output_parser = StrOutputParser()

    # Create the chain
    model_chain = prompt | llm | output_parser
    return model_chain


chain = load_model_and_setup_chain()
INPUT = str(input("Input: "))
response = chain.invoke({"query": INPUT})
print(response)
