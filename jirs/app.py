import streamlit as st
from DynamicPrompt.Utils.common import PromptOperations


st.title("Auto Prompt 🔗")

with st.form("user input"):


    story_id = st.text_input("Story id", max_chars=20)

    button = st.form_submit_button("Generate Prompt")

    if button:
        response = PromptOperations(story_id=story_id).generate_prompt()

        st.text_area(label="Prompt", value=response)
# story_id = 'TMS-84'
# response = PromptOperations(story_id=story_id).generate_prompt()