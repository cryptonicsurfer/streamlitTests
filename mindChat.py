import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "openAI-API-key"

# App title
st.title("Mind Mapping and Brainstorming Chatbot")

# Mind map nodes state management
nodes = st.session_state.get("nodes", [])
connections = st.session_state.get("connections", [])

# Create a text input for the user prompt
user_prompt = st.text_input("Enter your brainstorming prompt:")

# Submit button for sending the prompt to the chatbot
if st.button("Generate Counterpoints"):
    # Call OpenAI API with the user's prompt
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=user_prompt,
        max_tokens=100,
        n=5,
        stop=None,
        temperature=0.7,
    )

    # Display the generated counterpoints as a list with radio buttons
    counterpoints = [choice.text for choice in response.choices]
    selected_counterpoint = st.radio("Select a counterpoint:", counterpoints)

    # Add the selected counterpoint as a new node in the mind map
    if st.button("Add to Mind Map"):
        nodes.append(selected_counterpoint)
        st.session_state["nodes"] = nodes

# Display mind map nodes and connections
st.write("## Mind Map")
for i, node in enumerate(nodes):
    st.write(f"Node {i + 1}: {node}")

# Create connections between nodes
source_node = st.selectbox("Select source node:", list(range(1, len(nodes) + 1)), key="source")
target_node = st.selectbox("Select target node:", list(range(1, len(nodes) + 1)), key="target")

if st.button("Create Connection"):
    if source_node != target_node:
        connections.append((source_node, target_node))
        st.session_state["connections"] = connections

st.write("## Connections")
for connection in connections:
    st.write(f"Node {connection[0]} -> Node {connection[1]}")
