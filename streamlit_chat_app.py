import streamlit as st
import time
import random
import uuid

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())[:8]

st.title("Streamlit Chat App")

# Display chat messages
chat_container = st.container()

# Input for new messages
user_input = st.text_input("Type a message:")

if user_input:
    # Add user message to chat
    st.session_state.messages.append(("You", user_input))
    
    # Simulate receiving a message from another user
    other_user_id = f"User {random.randint(1000, 9999)}"
    response = f"This is a simulated response from {other_user_id}"
    st.session_state.messages.append((other_user_id, response))
    
    # Clear the input box
    st.experimental_rerun()

# Display all messages
with chat_container:
    for sender, message in st.session_state.messages:
        if sender == "You":
            st.text_area(sender, message, height=50, key=f"{time.time()}{sender}")
        else:
            st.text_area(sender, message, height=50, key=f"{time.time()}{sender}")

# Display user ID
st.sidebar.write(f"Your User ID: {st.session_state.user_id}")