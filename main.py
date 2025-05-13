import streamlit as st
from agent_runner import run_tools

st.set_page_config(page_title="Repurpose Agent")

st.title("🤖 Local Auto-Repurpose Engine (LangChain + Mistral)")

content = st.text_area("Paste your raw content here:")

if st.button("Repurpose"):
    with st.spinner("Repurposing with tools..."):
        result = run_tools(content)
        st.markdown(result)

