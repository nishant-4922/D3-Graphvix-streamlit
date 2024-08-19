import streamlit as st # type: ignore
import streamlit.components.v1 as components # type: ignore

# Main menu
menu = ["HOME", "D3 Output"]
choice = st.sidebar.selectbox("Menu", menu)

# Home Page
if choice == "HOME":
    st.title("Home")
    st.write("This page contains descriptions of different functions.")
    
    st.subheader("Function 1")
    st.write("Description of Function 1")
    if st.button("D3 Input"):
        st.session_state["navigate_to"] = "D3 Output"

# D3 Output Page
if choice == "D3 Output" or st.session_state.get("navigate_to") == "D3 Output":
    st.title("D3 Output")
    
    # Load the D3 visualization
    with open("index.html", 'r') as f:
        html_content = f.read()
    
    components.html(html_content, height=600, scrolling=True)
