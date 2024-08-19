import streamlit as st
import streamlit.components.v1 as components
import graphviz

# Initialize session state for navigation
if "navigate_to" not in st.session_state:
    st.session_state.navigate_to = "HOME"

# Define the menu
menu = ["HOME", "D3 Output"]

# Main menu
choice = st.sidebar.selectbox("Menu", menu, index=menu.index(st.session_state.navigate_to))

# Home Page
if choice == "HOME":
    st.title("Home")
    st.write("This page contains descriptions of different functions.")
    
    st.subheader("Function 1")
    st.write("Description of Function 1")
    
    if st.button("Go to D3 Output"):
        st.session_state.navigate_to = "D3 Output"
    
    # Graphviz Flowchart
    st.subheader("Graphviz Flowchart")

    # Create a Graphviz source object
    dot = graphviz.Digraph()

    # Add nodes and edges to the graph
    dot.node('A', 'flare')
    
    dot.node('B', 'analytics')
    dot.node('C', 'cluster')
    dot.node('D', 'graph')
    dot.node('E', 'optimization')
    
    dot.node('F', 'AgglomerativeCluster')
    dot.node('G', 'CommunityStructure')
    dot.node('H', 'HierarchicalCluster')
    dot.node('I', 'MergeEdge')
    
    dot.node('J', 'BetweennessCentrality')
    dot.node('K', 'LinkDistance')
    dot.node('L', 'MaxFlowMinCut')
    dot.node('M', 'ShortestPaths')
    dot.node('N', 'SpanningTree')
    
    dot.node('O', 'AspectRatioBanker')
    
    # Add edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('B', 'D')
    dot.edge('B', 'E')
    
    dot.edge('C', 'F')
    dot.edge('C', 'G')
    dot.edge('C', 'H')
    dot.edge('C', 'I')
    
    dot.edge('D', 'J')
    dot.edge('D', 'K')
    dot.edge('D', 'L')
    dot.edge('D', 'M')
    dot.edge('D', 'N')
    
    dot.edge('E', 'O')
    
    # Render the graph in Streamlit
    st.graphviz_chart(dot)

# D3 Output Page
if choice == "D3 Output":
    st.title("D3 Output")
    
    # Load the D3 visualization
    with open("index.html", 'r') as f:
        html_content = f.read()
    
    components.html(html_content, height=600, scrolling=True)
