import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Hypothesis Testing AI Assistant",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>

.main-title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#1f77b4;
}

.subtitle {
    text-align:center;
    font-size:20px;
    margin-bottom:40px;
}

.card {
    padding:25px;
    border-radius:12px;
    background-color:#f8f9fa;
    box-shadow:0 4px 15px rgba(0,0,0,0.1);
}

.footer {
    text-align:center;
    margin-top:40px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="main-title">📊 Hypothesis Testing AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask statistical questions and learn hypothesis testing instantly</div>', unsafe_allow_html=True)

# Feature cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📘 Learn Concepts</h3>
    <p>Understand Null Hypothesis, Alternative Hypothesis, p-values and significance levels.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>📊 Solve Problems</h3>
    <p>Get step-by-step solutions for hypothesis testing questions.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🤖 AI Chatbot</h3>
    <p>Chat with an AI assistant trained to help with statistics.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("💬 Chat with the Hypothesis Testing Assistant")

# Embed Botpress chatbot
chatbot_html = """
<script src="https://cdn.botpress.cloud/webchat/v3.6/inject.js"></script>
<script src="https://files.bpcontent.cloud/2026/02/20/15/20260220151633-YX2ZU91U.js" defer></script>
"""

components.html(chatbot_html, height=600)

# Footer
st.markdown('<div class="footer">© 2026 Hypothesis Testing AI Assistant</div>', unsafe_allow_html=True)
