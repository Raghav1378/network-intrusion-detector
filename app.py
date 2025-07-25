import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('network_logs_decision_tree_model.joblib')
scaler = joblib.load('scaler_payload.joblib')

# Category mappings (update these if your encodings are different!)
port_categories = [21, 22, 25, 53, 80, 135, 443, 4444]  # Example: sorted unique ports from your data
request_types = ["DNS", "FTP", "HTTP", "HTTPS", "SMTP", "SSH", "Telnet"]
protocols = ["ICMP", "TCP", "UDP"]
user_agents = [
    "Mozilla/5.0", "curl/7.68.0", "Wget/1.20.3", "python-requests/2.25.1", "nmap/7.80", "Nikto/2.1.6"
]
statuses = ["Success", "Failure"]

# Label mapping (from your notebook)
label_mapping = {0: "BotAttack", 1: "Normal", 2: "PortScan"}

st.title("Network Threat Detection")

st.write("Enter the network log features:")

# Port (as category code)
port_selected = st.selectbox("Port", options=range(len(port_categories)), format_func=lambda x: str(port_categories[x]))
# Request_Type
request_type_selected = st.selectbox("Request Type", options=range(len(request_types)), format_func=lambda x: request_types[x])
# Protocol
protocol_selected = st.selectbox("Protocol", options=range(len(protocols)), format_func=lambda x: protocols[x])
# User_Agent
user_agent_selected = st.selectbox("User Agent", options=range(len(user_agents)), format_func=lambda x: user_agents[x])
# Status
status_selected = st.selectbox("Status", options=range(len(statuses)), format_func=lambda x: statuses[x])
# Payload_Size (raw, will be scaled)
payload_size = st.number_input("Payload Size", min_value=0, value=1000)

# Scale payload size
scaled_payload = scaler.transform(np.array([[payload_size]]))[0][0]

# Prepare input for model
input_features = np.array([[
    port_selected,
    request_type_selected,
    protocol_selected,
    user_agent_selected,
    status_selected,
    scaled_payload
]])

if st.button("Predict"):
    prediction = model.predict(input_features)[0]
    st.success(f"Prediction: {label_mapping.get(prediction, prediction)}")

st.markdown("---")
st.write("**Note:** If you add new categories or change encodings, update the lists above.")