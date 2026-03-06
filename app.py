import streamlit as st

st.set_page_config(
    page_title="Hypothesis Testing AI Assistant",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 Hypothesis Testing AI Assistant")
st.write("Learn and solve hypothesis testing problems with an AI chatbot.")

st.markdown("---")

# Features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📘 Learn Concepts")
    st.write("Understand Null Hypothesis, Alternative Hypothesis, p-values, and significance levels.")

with col2:
    st.markdown("### 📊 Solve Problems")
    st.write("Get step-by-step help solving hypothesis testing questions.")

with col3:
    st.markdown("### 🤖 AI Chatbot")
    st.write("Interact with an AI assistant trained for statistics.")

st.markdown("---")

st.subheader("💬 Chat with the Hypothesis Testing Assistant")
st.write("Use the chat icon at the bottom-right corner of the page.")

# Inject Botpress chatbot
st.markdown(
"""
<script src="https://cdn.botpress.cloud/webchat/v3.6/inject.js"></script>
<script src="https://files.bpcontent.cloud/2026/02/20/15/20260220151633-YX2ZU91U.js" defer></script>
""",
unsafe_allow_html=True
)

st.markdown("---")
st.write("© 2026 Hypothesis Testing AI Assistant")
