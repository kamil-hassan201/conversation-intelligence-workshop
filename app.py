import streamlit as st
from engine import get_response


# set the title of the document
st.title("Chat with Your Document")

# step 1: declare array of messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": get_response("What is the document about?")
    })

# step 2: display the messages stored in array
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# step 3: Take user input:
prompt = st.chat_input("Type your question")

if prompt:
    # display the prompt in the chat container
    with st.chat_message("user"):
        st.markdown(prompt)

    # store the prompt in the array
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # get response from document
    response_stream = get_response(prompt)

    # display the response to the chat container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response_text = ""
        for response in response_stream.response_gen:
            response_text += response
            message_placeholder.markdown(response_text + "| ") # Streaming effect

        message_placeholder.markdown(response_text)


    # store the response in the array
    st.session_state.messages.append({
        "role": "assistant",
        "content": response_text
    })