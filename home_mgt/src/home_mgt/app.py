import streamlit as st
from crew import HomeMgt
import os
from dotenv import load_dotenv
from crewai import Task

load_dotenv()

st.title("🏠 Home Management AI")

# Initialize session state for storing conversation history and task list
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "home_tasks" not in st.session_state:
    st.session_state.home_tasks = ""
if "crew" not in st.session_state:
    st.session_state.crew = HomeMgt().crew()
    st.session_state.list_manager = HomeMgt().list_manager()

# --- Layout with two columns ---
col1, col2 = st.columns([2, 1])  # Adjust the ratio as needed

# --- Chat Window (col1) ---
with col1:
    st.subheader("Chat with AI Assistant")
    # Display conversation history
    if st.session_state.conversation_history:
        for item in st.session_state.conversation_history:
            st.write(item)

    # User input box
    user_input = st.text_input("Enter a task:", key="user_input")

    if st.button("Send"):
        if user_input.strip():
            st.session_state.conversation_history.append(f"**You:** {user_input}")

            # Create a Task that takes the user input.
            task_input = Task(
                description=f"Continue updating a structured to-do list based on user input: {user_input}. "
                "The list should include sections for weekly, monthly, and seasonal tasks.",
                expected_output="A markdown-formatted list of home tasks, "
                "with sections for weekly, monthly, and seasonal tasks.",
                agent=st.session_state.list_manager,
            )
            # Run CrewAI with current input and update home_tasks
            try:
                result = st.session_state.crew.kickoff(inputs={"user_input": user_input}, tasks=[task_input])
                st.session_state.home_tasks = result
                st.session_state.conversation_history.append(f"**AI:** {result}")

            except Exception as e:
                st.error(f"An error occurred: {e}")

            # Clear input field after processing
            st.session_state.user_input = ""


# --- Task List Window (col2) ---
with col2:
    st.subheader("Current Task List")
    if st.session_state.home_tasks:
        st.markdown(st.session_state.home_tasks)
    else:
        st.write("No tasks yet. Start a conversation to add tasks.")
