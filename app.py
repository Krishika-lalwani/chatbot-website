import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hypothesis Testing AI Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Hypothesis Testing AI Assistant")
st.write("Learn and solve hypothesis testing problems using an AI chatbot.")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📘 Learn Concepts")
    st.write("Understand Null Hypothesis, Alternative Hypothesis, p-values, significance levels and tests.")

with col2:
    st.markdown("### 📊 Solve Problems")
    st.write("Get step-by-step help solving hypothesis testing problems.")

with col3:
    st.markdown("### 🤖 AI Chatbot")
    st.write("Interact with an AI assistant trained for statistics.")

st.markdown("---")
st.subheader("💬 Chat with the Hypothesis Testing Assistant")

chatbot_html = """
<div id="chat-container"></div>

<script>
setTimeout(function() {
    const iframe = document.createElement("iframe");
    iframe.src = "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/02/20/15/20260220151633-UWG3A038.json";
    iframe.width = "100%";
    iframe.height = "700";
    iframe.style.border = "none";
    document.getElementById("chat-container").appendChild(iframe);
}, 1500); // delay loading by 1.5 seconds
</script>
"""

components.html(chatbot_html, height=720)

st.markdown("---")
st.write("© 2026 Hypothesis Testing AI Assistant")
