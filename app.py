# road-safety
# Navigate to your project folder
cd /path/to/your/project

# Initialize git repo (if not done already)
git init

# Add all files (including app.py)
git add .

# Commit files
git commit -m "Initial commit with Streamlit app"

# Add remote repo (replace <username> and <repo>)
git remote add origin https://github.com/<username>/<repo>.git

# Push to GitHub
git branch -M main
git push -u origin main
import streamlit as st

st.title("AI Traffic Accident Prediction")

st.sidebar.header("Input Features")

age = st.sidebar.number_input("Age of Driver", min_value=16, max_value=100, value=30)
vehicle_type = st.sidebar.selectbox("Vehicle Type", ["Car", "Motorcycle", "Truck", "Van", "Bicycle", "Other"])
weather = st.sidebar.selectbox("Weather Condition", ["Clear", "Rainy", "Foggy", "Snowy", "Other"])
road_surface = st.sidebar.selectbox("Road Surface", ["Dry", "Wet", "Icy", "Other"])
journey_purpose = st.sidebar.selectbox("Journey Purpose", ["Work", "Leisure", "Other"])

if st.button("Predict Accident Risk"):
    # Dummy logic — replace with your actual model prediction
    risk_prob = 0.12
    if risk_prob < 0.3:
        risk = "Low"
        color = "green"
    elif risk_prob < 0.7:
        risk = "Medium"
        color = "orange"
    else:
        risk = "High"
        color = "red"

    st.markdown(f"### Predicted Accident Risk: <span style='color:{color}'>{risk}</span>", unsafe_allow_html=True)
    st.write(f"Probability: {risk_prob:.2f}")

