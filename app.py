import os
import openai
from dotenv import load_dotenv
import streamlit as st
from datetime import datetime

# Load environment variables
load_dotenv()

# Set up OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
openai.api_key = api_key

# Constants
MODELS = ["gpt-3.5-turbo", "gpt-4"]
CONTENT_TYPES = ["Blog post", "Social media post", "Product description", "Email", "News article"]
TONES = ["Professional", "Casual", "Humorous", "Formal", "Persuasive", "Informative"]

def validate_input(prompt, content_type, tone, length, temperature):
    if not prompt:
        raise ValueError("Please enter a content topic.")
    if content_type not in CONTENT_TYPES:
        raise ValueError("Invalid content type selected.")
    if tone not in TONES:
        raise ValueError("Invalid tone selected.")
    if not 50 <= length <= 1000:
        raise ValueError("Word count must be between 50 and 1000.")
    if not 0.1 <= temperature <= 1.0:
        raise ValueError("Temperature must be between 0.1 and 1.0.")

def generate_content(prompt, content_type, tone, length, model, temperature):
    validate_input(prompt, content_type, tone, length, temperature)
    
    full_prompt = f"Generate a {content_type} with a {tone} tone. The content should be approximately {length} words long. The topic is: {prompt}"
    
    try:
        response = openai.Completion.create(
            model=model,
            prompt=full_prompt,
            max_tokens=length * 2,  # Approximate token count
            temperature=temperature,
        )
        return response.choices[0].text.strip()
    except openai.OpenAIError as e:
        raise RuntimeError(f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Streamlit UI
st.title("Enhanced AI-Powered Content Generator")

prompt = st.text_input("Enter your content topic:")
content_type = st.selectbox("Select content type:", CONTENT_TYPES)
tone = st.selectbox("Select tone:", TONES)
length = st.slider("Approximate word count:", 50, 1000, 200)
model = st.selectbox("Select AI model:", MODELS)
temperature = st.slider("Temperature (creativity):", 0.1, 1.0, 0.7, 0.1)

if st.button("Generate Content"):
    try:
        with st.spinner("Generating content..."):
            generated_content = generate_content(prompt, content_type, tone, length, model, temperature)
        st.subheader("Generated Content:")
        st.write(generated_content)
    except ValueError as e:
        st.error(str(e))
    except RuntimeError as e:
        st.error(str(e))
