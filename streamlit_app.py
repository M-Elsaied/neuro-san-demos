import os
import streamlit as st
from pyhocon import ConfigFactory
from neuro_san.agent_core.agent_network import AgentNetwork
from neuro_san.agent_core.agent_input import AgentInput

st.set_page_config(page_title="Embedded Neuro-SAN Agent", layout="wide")

st.title("🧠 Neuro-SAN Agent in Streamlit")

st.markdown("This demo loads and executes an agent network directly inside Streamlit.")

# Let user input a message to the agent
user_input = st.text_input("What would you like to ask the agent?", "Give me a summary of a recent AI breakthrough.")

# Path to manifest (you can change this to a custom one if needed)
manifest_path = "registries/manifest.hocon"

try:
    manifest = ConfigFactory.parse_file(manifest_path)
    network_name = list(manifest["agent_networks"].keys())[0]  # Use the first defined network
    network = AgentNetwork.from_hocon(manifest, network_name)

    if user_input:
        st.markdown("## 🧠 Agent Response")
        input_obj = AgentInput(input_type="text", input_value=user_input)
        result = network.run(input_obj)
        st.success("Agent responded:")
        st.json(result.dict())
except Exception as e:
    st.error(f"Failed to load agent network or process input: {e}")
