import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

st.title('Simple Chatbot')

with st.sidebar:
    st.title('Login Hugchat')
    hf_email = st.text_input('Enter E-mail:')
    hf_pass = st.text_input('Enter Password:', type='password')
    if not (hf_email and hf_pass):
        st.warning('Pease enter your account')
    else:
        st.success('Processed to entering your prompt message!')

# store LLM generated responses
if 'messages' not in st.session_state.keys():
    st.session_state.messages = [
        {'role': 'assistant', 'content': 'How may I help you?'}
    ]


# display chat message
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

# Function to generate response


def generate_response(prompt_input, email, password):
    # Login
    sign = Login(email, password)
    cookies = sign.login()

    # create chatbot
    chatbox = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbox.chat(prompt_input)


# User-provided prompt
if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.write(prompt)

# generate a new response if last message is not from assistant
if st.session_state.messages[-1]['role'] != 'assistant':
    with st.chat_message('assistant'):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, hf_email, hf_pass)
            st.write(response)

    message = {'role': 'assistant', 'content': response}
    st.session_state.messages.append(message)
