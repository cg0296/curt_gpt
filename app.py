import os

import streamlit as st
from openai import OpenAI


st.set_page_config(page_title="Curt GPT", page_icon=":speech_balloon:")
st.title("Curt Gpt")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY is not set in the environment.")
    st.stop()

client = OpenAI()

if "last_output" not in st.session_state:
    st.session_state.last_output = ""

st.subheader("Output")
if st.session_state.last_output:
    st.write(st.session_state.last_output)
else:
    st.write("")

with st.form("prompt_form", clear_on_submit=False):
    model = st.selectbox(
        "Model",
        [
            "gpt-5.1",
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "o3",
            "o4-mini",
            "gpt-4o",
            "gpt-4o-realtime-preview",
        ],
        index=0,
    )
    input_message = st.text_input("How can I help today?", value="")
    submitted = st.form_submit_button("Submit")

if submitted:
    prompt = input_message.strip()
    if prompt:
        try:
            with st.spinner("Thinking..."):
                resp = client.responses.create(
                    model=model,
                    input=prompt,
                )
            st.session_state.last_output = resp.output_text
        except Exception as exc:
            st.error(f"Request failed: {exc}")
