# 💰 Insurance Charges Predictor  sdfsfsf
> *An intelligent Streamlit web app that predicts medical insurance costs using Machine Learning.*

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen?logo=streamlit)](https://share.streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)]()
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Model-orange?logo=scikitlearn)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

---


## 🧠 Project Overview
The **Insurance Charges Predictor** is a **machine learning web app** that estimates a person's medical insurance cost based on their **age, BMI, and smoking habits**.  

Built with:
- 🧮 **Linear Regression Model**
- 🌐 **Streamlit** for deployment
- 📊 **Kaggle’s Insurance Dataset** ([link](https://www.kaggle.com/datasets/mirichoi0218/insurance))

This project demonstrates the full ML lifecycle:
> *Data Cleaning → Model Training → Model Saving → Web Deployment*

---

## 🚀 Live Demo
Try it instantly on **Streamlit Cloud**  
👉 [🔗 Launch App](https://insurance-charges-predictor-aditya-jadhav-524.streamlit.app/)  

---

## 🧩 Features
✅ Predicts insurance cost in real time  
✅ Clean and modern UI  
✅ Interactive sliders and input fields  
✅ Powered by trained Linear Regression model  
✅ Lightweight, fast, and deployable anywhere  

---

## 📁 Project Structure
insurance-charges-predictor/
│
├── app.py                # Streamlit web app
├── insurance_model.pkl    # Saved trained ML model
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── assets/                # Optional images/backgrounds
## 🧮 How It Works

1. User provides input:
   - Age  
   - BMI (Body Mass Index)  
   - Smoking Status (Yes/No)
2. Model converts inputs into numerical features.
3. Pre-trained **Linear Regression** model predicts insurance cost (`charges`).
4. App displays the estimated amount with a clean, styled UI.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python 🐍 |
| **Frontend** | Streamlit |
| **Model** | Scikit-learn (Linear Regression) |
| **Dataset** | Kaggle - Insurance Dataset |
| **Deployment** | Streamlit Cloud / Render |

---

## 📊 Example Prediction

| Age | BMI | Smoker | Predicted Charges ($) |
|-----|-----|---------|-----------------------|
| 28  | 26.4 | No | 4,320.50 |
| 45  | 32.5 | Yes | 23,810.22 |
| 60  | 30.2 | No | 12,790.18 |

---

## 💡 Future Improvements

- Add more features (sex, region, children)  
- Include feature scaling and one-hot encoding  
- Deploy with authentication and usage analytics  
- Enhance UI with animations and tooltips  

---

## 🧑‍💻 Author

**👤 Aditya Jadhav**  
*Data Science Enthusiast | Machine Learning Developer*  
📧 [Email me](adityabjadhav.524@gmail.com)  
🌐 [LinkedIn](www.linkedin.com/in/aditya-jadhav-6775702b4)  
🐙 [GitHub](https://github.com/AdityaJadhav-ds)

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify with credit.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AdityaJadhav-ds/insurance-charges-predictor.git
cd insurance-charges-predictor

