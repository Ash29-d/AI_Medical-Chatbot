from langchain_core.prompts import PromptTemplate , ChatPromptTemplate 
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
import os 
import streamlit as st

load_dotenv()

api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm =HuggingFaceEndpoint(
    repo_id = "tiiuae/falcon-7b-instruct",
    task = "Question-answering",
    temperature = 0.59
    # huggingfacehub_api_token = api_key,
    # max_new_tokens = 256
)

model = ChatHuggingFace(llm =llm)

#Define the Prompt
templates = PromptTemplate(
    template = """You are an AI assistant acting as a Professional {types} of the Doctor , 
    Give the  suggestions in concise and solutions about the {problem} and cure .
    If you dont know the answer then its better to say 'I Dont know' rather than making a wrong answer ,
    If the conditions is severe then its better to appoint doctor""",
    input_variables = ["types","problem"]

)


# Streamlit UI


# Input fields
types = st.sidebar.selectbox("Select Doctor Type", ["Dermatologist", "General Physician", "Pediatrician", "Cosmetologist"])


st.title(f"AI {types} Hospitality")
st.write("Get professional advice from AI")
problem = st.text_input("Enter your skin problem")


if st.button("Get Advice"):
    if problem:
        prompt = templates.invoke({"types": types, "problem": problem})
        response = llm.invoke(prompt)
        st.subheader("AI's Advice:")
        st.write(response)
    else:
        st.warning("Please enter a skin problem to get advice.")


# types = "Dermatologist"
# problem = "Acne"

# prompt = templates.invoke({
#     "types" : types,
#     "problem" : problem
# })


# result = model.invoke(prompt)
# print(result)