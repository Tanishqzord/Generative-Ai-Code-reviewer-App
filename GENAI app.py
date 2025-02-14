import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import streamlit as st  # type: ignore
import google.generativeai as genai  # type: ignore

# Configure your API key.
genai.configure(api_key="AIzaSyCKvEtJKsO8PtgUBL2wUr4piGCAJgSB5DI")

sys_prompt = (
    "You are a code review assistant. Please analyze the following Python code for potential bugs, "
    "errors, and areas of improvement. Provide detailed feedback and suggest fixes where appropriate.\n\n"
    "Please provide your analysis and any improved code snippets:"
)

# Pick up a model.
model = genai.GenerativeModel(
    model_name="models/gemini-2.0-flash-exp",
    system_instruction=sys_prompt
)

# Build the Streamlit UI.
st.title("GenAI App - AI Code Reviewer")
st.write(
    """
    Welcome to the AI Code Reviewer powered by Google Generative AI!  
    Enter your Python code in the text area below and click **Review Code** to receive detailed feedback.
    """
)

# Create a text area for Python code input.
user_prompt = st.text_area("Enter your Python code here:", height=300)

# When the button is clicked, call the model's generate_content method.
if st.button("Review Code"):
    if not user_prompt.strip():
        st.error("Please enter some Python code to review.")
    else:
        with st.spinner("Reviewing your code..."):
            response = model.generate_content(user_prompt)
            review_result = response.text  
        st.subheader("Review Results")
        st.text_area("Feedback and Improved Code", value=review_result, height=400)
