from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai


#Load environment variables
load_dotenv()

api_key = "AIzaSyDrKeDRSpZ5g1ZUa4wTSN5MJ77a3uvjrOA"
genai.configure(api_key = api_key)

model = genai.GenerativeModel('gemini-1.5-flash')


#Function to translate text

def translate_text(text, source_language, target_language):
    model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = (f"Translate the following text from {source_language} to {target_language}: {text}")
    response = model.generate_content([prompt])
    return response.text 

#Initialize Streamlit app
st.set_page_config(page_title = "AI - Powered Language Translator", page_icon = "🌐")
st.header("🌐 AI-Powered Language Translator")

#User input for text, source language, and target language
text = st.text_area("📝 Enter text to translate:")
source_language = st.selectbox("🌍 Select source language:", ["English", "Spanish", "French", "German", "Chinese"])
target_language = st.selectbox("🌏 Select target language:", ["English", "Spanish", "French", "German", "Chinese"])

#Translate text button
if st.button("🔄️ Translate"):
    if text and source_language and target_language:
        try:
            translated_text = translate_text(text, source_language, target_language)
            st.header("🗣️ Translated Text:")
            st.write(translated_text)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
    
    else:
        st.warning("⚠️ Please fill in all fields.")



