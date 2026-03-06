import streamlit as st
from memory_agent import MemoryAgent

# initialize agent
agent = MemoryAgent()

st.set_page_config(page_title="AI Memory Agent", page_icon="🧠")

st.title("🧠 Persistent Memory AI Agent")
st.write("This AI system remembers information using embeddings and a vector database (ChromaDB).")

st.divider()

# remember section
st.subheader("📌 Store Memory")

memory_text = st.text_input("Enter something you want the AI to remember")

if st.button("Save Memory"):

    if memory_text:
        agent.remember(memory_text)
        st.success("Memory stored successfully!")
    else:
        st.warning("Please enter something.")

st.divider()

# recall section
st.subheader("🔎 Recall Memory")

query = st.text_input("Ask something to recall stored memory")

if st.button("Search Memory"):

    if query:

        results = agent.recall(query)

        st.write("### Relevant Memories")

        if results:
            for r in results:
                st.write(f"- {r}")
        else:
            st.info("No memories found.")

    else:
        st.warning("Enter a query.")