import streamlit as st

def show_todolist():
    st.title("Simple Todo List")

    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []

    def add_task():
        task = st.text_input("Enter a task", key="new_task")
        if st.button("Add Task") and task.strip() != "":
            st.session_state.tasks.append(task.strip())
            st.rerun()

    def remove_task(index):
        del st.session_state.tasks[index]
        st.rerun()

    add_task()

    if st.session_state.tasks:
        st.write("### Your Todo List:")

        for index, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([9, 1])

            with col1:
                st.write(f"- {task}")

            with col2:
                if st.button("Remove", key=f"remove_{index}"):
                    remove_task(index)

        # CSS Styling for Buttons
        st.markdown("""
            <style>
                .stButton button {
                    font-size: 18px;
                    font-weight: bold;
                    color: white;
                    background: #008CBA;
                    border-radius: 10px;
                    padding: 8px 20px;
                    margin: 5px;
                    border: none;
                    word-break: normal !important;
                    white-space: nowrap !important;
                }
                .stButton button:hover {
                    background-color: #2b6cb0;
                }
            </style>
        """, unsafe_allow_html=True)

    else:
        st.write("No tasks added yet!")

