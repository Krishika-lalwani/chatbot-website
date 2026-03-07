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
    st.write("Understand Null Hypothesis, Alternative Hypothesis, p-values, significance levels and tests.")

with col2:
    st.markdown("### 📊 Solve Problems")
    st.write("Get step-by-step help solving hypothesis testing problems.")

with col3:
    st.markdown("### 🤖 AI Chatbot")
    st.write("Interact with an AI assistant trained for statistics.")

st.markdown("---")

st.subheader("💬 Ask Questions Using the Chatbot")

# Inject Botpress widget into the parent page
botpress_widget = """
<div id="botpress-chat"></div>

<script src="https://cdn.botpress.cloud/webchat/v3.6/inject.js"></script>
<script>
window.addEventListener("load", function () {
  const script = document.createElement("script");
  script.src = "https://files.bpcontent.cloud/2026/02/20/15/20260220151633-YX2ZU91U.js";
  script.defer = true;
  document.body.appendChild(script);
});
</script>
"""

components.html(botpress_widget, height=50)

st.markdown("---")
st.write("© 2026 Hypothesis Testing AI Assistant")
