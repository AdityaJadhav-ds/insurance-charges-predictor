import streamlit as st
import pickle
import numpy as np
from PIL import Image

# ------------------------------
# 🌟 Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Insurance Charges Predictor",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------------------------
# 🎨 Custom Styling
# ------------------------------
st.markdown("""
    <style>
        body {
            background-color: #f4f6f9;
            color: #222;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            text-align: center;
            color: #1e3a8a;
            font-size: 2.5em;
            font-weight: bold;
        }
        .sub-title {
            text-align: center;
            font-size: 1.2em;
            color: #374151;
        }
        .prediction {
            font-size: 1.5em;
            font-weight: bold;
            color: #047857;
        }
        .footer {
            text-align: center;
            margin-top: 3rem;
            font-size: 0.9em;
            color: #6b7280;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# 🧠 Load Model
# ------------------------------
model = pickle.load(open('insurance_model.pkl', 'rb'))

# ------------------------------
# 🖼️ Title and Header
# ------------------------------
st.markdown("<p class='main-title'>💰 Insurance Charges Prediction</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Estimate your medical insurance cost based on personal attributes</p>", unsafe_allow_html=True)
st.write("")

# ------------------------------
# 🧾 User Inputs
# ------------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Select Age", 18, 100, 30)
    bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)

with col2:
    smoker = st.radio("Are you a Smoker?", ("No", "Yes"))
    smoker_yes = 1 if smoker == "Yes" else 0

# ------------------------------
# 🔮 Prediction Logic
# ------------------------------
if st.button("💵 Predict Charges", use_container_width=True):
    input_data = np.array([[age, bmi, smoker_yes]])
    prediction = model.predict(input_data)[0]
    
    st.markdown(f"<p class='prediction'>Estimated Insurance Charges: <br> 💵 ${prediction:,.2f}</p>", unsafe_allow_html=True)

# ------------------------------
# 🧭 Sidebar Info
# ------------------------------
st.sidebar.header("📊 About the Model")
st.sidebar.info(
    "This model predicts medical insurance costs based on **Age**, **BMI**, and **Smoking Status**. "
    "It was trained using the Kaggle Insurance dataset by *Aditya Jadhav* using Linear Regression."
)

st.sidebar.header("⚙️ Features Used")
st.sidebar.write("- Age\n- BMI\n- Smoker (Yes/No)")

st.sidebar.header("🧠 Model Type")
st.sidebar.write("Linear Regression")

# ------------------------------
# 📜 Footer
# ------------------------------
st.markdown("<p class='footer'>Developed by <b>Aditya Jadhav</b> | Powered by Streamlit ⚡</p>", unsafe_allow_html=True)
