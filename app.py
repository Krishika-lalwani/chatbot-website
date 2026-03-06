import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Hypothesis Testing AI Assistant",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Hypothesis Testing AI Assistant")
st.write("Learn and solve hypothesis testing problems using an AI chatbot.")

st.markdown("---")

# Features section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📘 Learn Concepts")
    st.write("Understand Null Hypothesis, Alternative Hypothesis, p-values,significance levels and some tests.")

with col2:
    st.markdown("### 📊 Solve Problems")
    st.write("Get step-by-step help solving hypothesis testing problems.")

with col3:
    st.markdown("### 🤖 AI Chatbot")
    st.write("Interact with an AI assistant trained for statistics.")

st.markdown("---")

st.subheader("💬 Chat with the Hypothesis Testing Assistant")

# Embed chatbot using iframe
chatbot_url = "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/02/20/15/20260220151633-UWG3A038.json"

components.iframe(chatbot_url, height=650)
st.markdown("---")
st.markdown("---")
st.write("© 2026 Hypothesis Testing AI Assistant")


st.switch_page("app.py")
