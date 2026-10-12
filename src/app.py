import utils
import streamlit as st

st.title("CHATBOT PROJECT")

prompt = st.text_input("Ask your question:")

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':'ai','content':'Hello! I am your AI assistant. How can I help you today?'}]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

prompt = st.chat_input()
model = "qwen2.5-coder:7b"
if prompt:
    st.session_state['messages'].append({'role':'user','content':prompt})
    with st.spinner('AI is typing...'):
        new_prompt = 'give me answer with example and emoji and shapes and description' + prompt
        response = utils.call_ollama_model(model, new_prompt)
        st.chat_message('ai').write(response)
        st.session_state['messages'].append({'role':'ai','content':response})
    st.chat_message('user').write(prompt)


