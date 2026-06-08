import streamlit as st
import wikipedia
from groq import Groq
import os

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Query-Match AI", layout="wide", page_icon="🧠")

# 2. PROFESSIONAL DARK UI (CUSTOM CSS)
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stTextInput > div > div > input {
        background-color: #111; color: white; border: 1px solid #00f2ff;
        border-radius: 10px; padding: 15px; font-size: 18px;
    }
    .featured-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px; padding: 25px;
        border-left: 6px solid #00f2ff; margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 242, 255, 0.2);
    }
    .ai-tag { color: #00f2ff; font-weight: bold; letter-spacing: 1px; text-transform: uppercase; }
    .result-link { color: #8ab4f8; font-size: 20px; text-decoration: none; font-weight: 600; }
    .result-link:hover { color: #00f2ff; text-decoration: underline; }
    .name-tag { color: #ccff00; font-size: 18px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. INITIALIZING CLIENTS (API Keys)
# Note: Replace 'YOUR_GROQ_API_KEY' with your actual key
client = Groq(api_key="YOUR_GROQ_API_KEY")

if 'active' not in st.session_state:
    st.session_state.active = False

# ==================== 4. HOME PAGE ====================
if not st.session_state.active:
    st.write("\n" * 5)
    _, col, _ = st.columns([1, 3, 1])
    with col:
        st.markdown("<h1 style='text-align: center; color: white;'>🧠 QUERY-MATCH AI</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8ab4f8; font-size: 20px;'>Semantic Unification Search Engine</p>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background: rgba(255,255,255,0.03); padding: 20px; border-radius: 15px; border: 1px solid #444;'>
                <p style='color: gray; text-align: center; margin-bottom: 5px;'>DEVELOPED BY</p>
                <div class='name-tag'>SUMA SREE | JHANSI TANUJA | NAVYA SRI</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("LAUNCH AI INTERFACE 🚀", use_container_width=True):
            st.session_state.active = True
            st.rerun()

# ==================== 5. SEARCH INTERFACE ====================
else:
    # Sidebar navigation
    if st.sidebar.button("⬅ Back to Home"):
        st.session_state.active = False
        st.rerun()

    st.markdown("<h2 style='color: #00f2ff;'>Query-Match Engine</h2>", unsafe_allow_html=True)
    query = st.text_input("", placeholder="Ask anything (e.g., Explain Quantum Computing simply)...")

    if query:
        with st.spinner('Unifying Query and Generating Insight...'):
            try:
                # STEP 1: AI SEMANTIC UNIFICATION (Groq Llama-3.3)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a professional research assistant. Provide a concise, unified summary of the user's query."},
                        {"role": "user", "content": query}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                ai_response = chat_completion.choices[0].message.content

                # STEP 2: FACTUAL DATA RETRIEVAL (Wikipedia API)
                search_results = wikipedia.search(query, results=5)

                # DISPLAY AI OVERVIEW
                st.markdown(f"""
                    <div class='featured-box'>
                        <div class='ai-tag'>✨ AI Unified Overview</div>
                        <div style='color: white; font-size: 17px; margin-top: 15px; line-height: 1.6;'>
                            {ai_response}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                # DISPLAY SOURCE NODES
                st.markdown("### 📚 Related Knowledge Nodes")
                for title in search_results:
                    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
                    st.markdown(f"""
                        <div style='margin-bottom: 15px; padding-left: 10px; border-left: 2px solid #333;'>
                            <a class='result-link' href='{url}' target='_blank'>{title}</a><br>
                            <span style='color: #555; font-size: 12px;'>Source: Wikipedia API</span>
                        </div>
                    """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"System Error: {e}. Please check your API connectivity.")