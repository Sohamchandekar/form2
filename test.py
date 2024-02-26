import streamlit as st

def main():
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #FFCAD4;
        }

        .sidebar .sidebar-content {
            background-color: #0C359E;
            color: white;
        }

        .Widget>label {
            color: white;
        }

        .stTextArea>div>div>textarea {
            background-color: #344955;
            color: white;
            border-color: #cccccc;
        }

        .stTextInput>div>div>input {
            background-color: #344955;
            color: white;
            border-color: #cccccc;
        }

        .stButton>button {
            background-color: #FFD23F;
            color: black;
        }

        .stFileUploader>div>div {
            background-color: #FFD23F;
            border-color: #cccccc;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("My Streamlit App")

    # Sidebar
    st.sidebar.title("Sidebar")
    st.sidebar.markdown("This is the sidebar content.")

    # Main content
    st.write("Main content goes here.")

if __name__ == "__main__":
    main()
