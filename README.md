# AI_Medical-Chatbot – Intelligent Disease Prediction & Health Assistant

### Overview

AI Medical Chatbot is an AI-powered virtual assistant designed to provide basic medical information based on user symptoms. It leverages LangChain and Falcon-7B-Instruct from Hugging Face API to generate accurate and context-aware medical responses. The chatbot can be integrated into various platforms, such as web applications using Flask or Streamlit, making it a scalable and user-friendly solution.

### Flowchart of the Chatbot Process

The chatbot begins by taking user input, where a user enters their symptoms or asks about a medical condition. This input is then processed by LangChain, which structures it into a well-defined prompt. The structured prompt is sent to Falcon-7B-Instruct, an advanced AI model hosted on Hugging Face, to generate a medically relevant response. Finally, the chatbot presents the response to the user in a conversational format, making it easy to understand.

### Technologies Used:

Python – Backend logic & chatbot integration

LangChain – Managing LLM interactions

Falcon-7B-Instruct – AI model for medical response generation

Hugging Face API – Model hosting & inference

Streamlit – Web app deployment
