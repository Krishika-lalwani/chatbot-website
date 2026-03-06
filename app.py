import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hypothesis Testing AI Assistant",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
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

# Title
st.markdown('<div class="main-title">📊 Hypothesis Testing AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask statistical questions and learn hypothesis testing instantly</div>', unsafe_allow_html=True)

# Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📘 Learn Concepts</h3>
    Understand Null Hypothesis, Alternative Hypothesis, p-values and significance levels.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>📊 Solve Problems</h3>
    Get step-by-step help solving hypothesis testing questions.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🤖 AI Chatbot</h3>
    Ask the AI assistant any statistics question.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.write("💬 Use the chat icon at the **bottom-right corner** to talk with the assistant.")

# Inject chatbot script globally
components.html(
"""
<script src="https://cdn.botpress.cloud/webchat/v3.6/inject.js"></script>
<script src="https://files.bpcontent.cloud/2026/02/20/15/20260220151633-YX2ZU91U.js"></script>
""",
height=0
)

st.markdown('<div class="footer">© 2026 Hypothesis Testing AI Assistant</div>', unsafe_allow_html=True)
