

# 💻 Laptop Price Predictor

A machine learning web application that predicts the price of a laptop based on its specifications such as brand, RAM, CPU, GPU, storage, screen features, etc.
The model is trained using ensemble learning and deployed using Streamlit.

# 📌 Project Overview

## This project:
Trains a regression model on laptop specifications
Uses feature engineering (PPI calculation, encoding categorical features)
Combines multiple models using Voting Regressor and Stacking Regressor is used as the meta model on the top of all models.
Deploys the trained pipeline as an interactive Streamlit web app
The predicted price is returned in Indian Rupees (₹).

# 🧠 Machine Learning Approach
### Models Used
Random Forest Regressor
Gradient Boosting Regressor
XGBoost Regressor

## These models are combined using:
VotingRegressor (ensemble averaging)
StackingRegressor (meta-model on the top)
Pipeline Structure
ColumnTransformer
OneHotEncoder for categorical features
Numerical features passed directly
Pipeline
Preprocessing
Ensemble regressor
The entire pipeline is saved using pickle to ensure consistent preprocessing during prediction.

# 🧮 Features Used
Feature Name	Description
Company	Laptop brand
TypeName	Laptop type (Notebook, Ultrabook, etc.)
Ram	RAM size (GB)
Weight	Laptop weight (kg)
TouchScreen	Touchscreen support (Yes/No)
Ips	IPS display (Yes/No)
ppi	Pixels Per Inch (calculated)
Cpu brand	CPU brand
HDD	HDD storage (GB)
SSD	SSD storage (GB)
Gpu_brand	GPU brand
os	Operating system

# 🧾 Tech Stack
Python
scikit-learn
XGBoost
Pandas / NumPy
Streamlit
Pickle




# 🚀 How to Run the Project Locally
## 1️⃣ Clone the Repository
git clone https://github.com/kuldeepkp911/laptop-price-predictor-ml.git
cd laptop-price-predictor

## 2️⃣ Create Virtual Environment (recommended)
python -m venv laptev
laptev\Scripts\activate   # Windows

## 3️⃣ Install Dependencies
pip install -r requirements.txt

## 4️⃣ Run the Streamlit App
streamlit run laptop.py


# 📂 Project Structure
laptop-price-predictor/
│
├── laptop.py              # Streamlit application
├── pipe.pkl            # Trained ML pipeline
├── df.pkl              # Dataset used for dropdown values
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── notebook/
    └── laptop price prediction.ipynb    # Model training notebook