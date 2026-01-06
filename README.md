# 🏠 House Price Prediction App

This project is a machine learning–powered web application for predicting house prices based on structural and neighborhood-related features. Built using **Python**, **scikit-learn**, and **Streamlit**, it demonstrates the practical use of regression models in real estate analytics. Users can interact with a simple UI to get instant price estimates for residential properties.

---

## 📌 Key Features

- Predict house prices based on:
  - Number of bedrooms
  - Number of bathrooms
  - Living area (sq ft)
  - Condition of the house
  - Number of nearby schools
- Powered by multiple ML regression models
- Interactive web UI built with Streamlit
- Fast and user-friendly interface

---

## 🧠 Machine Learning Models Used

The following models were trained and compared:

- **Linear Regression** — baseline linear model
- **Ridge Regression** — improved generalization using L2 regularization
- **Random Forest Regressor** — ensemble model capturing complex patterns

---

## 📊 Evaluation Metrics

Model performance was measured using:

- **Mean Absolute Error (MAE)** – average magnitude of prediction errors
- **Mean Squared Error (MSE)** – squares errors to penalize larger ones
- **R² Score** – proportion of variance explained by the model

These metrics were used to select the best-performing model for deployment.

---

## 🖥️ Streamlit Web App

Users can:
- Input house details using sliders and number inputs
- Click “Predict” to see the estimated price
- Get results in real-time with a clean interface

---

## 🚀 How to Run Locally

```bash
# Clone this repository
git clone https://github.com/ghulam06mustafa/house-price-prediction.git
cd house-price-prediction

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
