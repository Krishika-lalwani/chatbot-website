import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="My Chatbot")

st.title("My HyTest Chatbot 🤖")

st.write("If you have anything to ask about Hypothesis testing, Chat with my chatbot below.")

botpress = """
<iframe 
src="https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/02/20/15/20260220151633-UWG3A038.json"
width="100%"
height="600">
</iframe>
"""

components.html(botpress, height=600)
