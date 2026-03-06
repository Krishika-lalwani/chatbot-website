import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hypothesis Testing AI Assistant",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 Hypothesis Testing AI Assistant")
st.write("Ask statistical questions and learn hypothesis testing with AI.")

# Feature section
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📘 **Learn Concepts** \nUnderstand null hypothesis, alternative hypothesis and p-values.")

with col2:
    st.info("📊 **Solve Problems** \nGet step-by-step help for hypothesis testing questions.")

with col3:
    st.info("🤖 **AI Chatbot** \nChat with the statistics assistant.")

st.markdown("---")
st.subheader("💬 Chat with the Assistant")

# Chatbot embed
components.html(
"""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.botpress.cloud/webchat/v3.6/inject.js"></script>
<script src="https://files.bpcontent.cloud/2026/02/20/15/20260220151633-YX2ZU91U.js"></script>
</head>
<body>
</body>
</html>
""",
height=600,
)

st.markdown("© 2026 Hypothesis Testing Assistant")
