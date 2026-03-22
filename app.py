import streamlit as st
from src.rag_engine import RAGEngine

st.title("🎓 College Knowledge Assistant")

engine = RAGEngine()

query = st.chat_input("Ask your question...")

if query:
    st.chat_message("user").write(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, docs = engine.ask(query)

            st.write(answer)

            with st.expander("📄 Sources"):
                for d in docs:
                    st.write(d.metadata)
                    st.write(d.page_content[:200])