import os
import subprocess
import streamlit as st

st.set_page_config(page_title="Neuro-SAN Cloud Demo", layout="centered")

st.title("🧠 Neuro-SAN Cloud Runner")
st.markdown("Launch and interact with the Neuro-SAN demo from your browser.")

# Step 1: Ask for API Key
openai_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# Step 2: Set the API key to the environment if provided
if openai_key:
    os.environ["OPENAI_API_KEY"] = openai_key
    st.success("API Key saved to environment ✅")

# Step 3: Button to launch the server (run.py)
if st.button("🚀 Launch Neuro-SAN"):
    st.info("Starting Neuro-SAN... this may take a few seconds.")
    try:
        os.makedirs("logs", exist_ok=True)
        with open("logs/streamlit_output.log", "w") as log:
            subprocess.Popen(["python", "run.py", "--use-flask-web-client"], stdout=log, stderr=log)
        st.success("Neuro-SAN launched! Please wait for the web client to be available.")
        st.markdown("Go to [http://localhost:5003](http://localhost:5003) to interact with the web client.")
    except Exception as e:
        st.error(f"Failed to launch Neuro-SAN: {e}")
