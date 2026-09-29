import streamlit as st
from agent import ask_agent

st.set_page_config(
    page_title="DevMemory",
    page_icon="🧠"
)

st.title("🧠 DevMemory")
st.subheader("An AI DevOps assistant that learns from past incidents")

st.write(
    "Describe a DevOps problem. DevMemory recalls relevant past incidents "
    "and uses them to improve its response."
)

with st.form("devmemory_form"):
    user_message = st.text_area(
        "Describe your problem",
        placeholder="Example: My Docker container cannot start because port 5000 is already in use.",
        height=150
    )

    submitted = st.form_submit_button("Ask DevMemory")

if submitted:
    if user_message.strip():

        with st.spinner("Recalling past incidents..."):
            result = ask_agent(user_message)

        st.markdown("### 🧠 Relevant Memory")

        if result["memories"]:
            for memory in result["memories"][:3]:
                st.info(memory.text)
        else:
            st.write("No relevant previous memory found.")

        st.markdown("### 🤖 DevMemory")
        st.markdown(result["answer"])

    else:
        st.warning("Please describe a problem first.")

st.divider()

st.caption("Powered by Groq + Hindsight")
