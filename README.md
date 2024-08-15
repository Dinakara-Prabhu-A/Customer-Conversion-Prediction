# Customer Conversion Prediction

This repository showcases an end-to-end machine learning project developed entirely by me for the **Guvi Datathon 1.0** challenge. The project aims to predict customer conversion rates for an insurance plan using historical marketing data. It also features a Streamlit web application for real-time predictions based on user inputs.

## Project Overview

The objective of this project is to build a robust predictive model capable of determining whether a client will subscribe to an insurance plan. The model was trained and evaluated using a dataset provided during the Guvi Datathon, with a focus on optimizing the F1-Score to effectively manage class imbalance.

## Key Features

- **End-to-End Development**: This project was fully developed by me, from data preprocessing and model training to deployment in a Streamlit web application.
- **Comprehensive Data Preprocessing**: Includes handling of missing values, encoding of categorical variables, and feature scaling to ensure the dataset is ready for modeling.
- **Advanced Model Evaluation**: Utilized multiple classifiers, including RandomForest, XGBoost, and Gradient Boosting, with hyperparameter tuning via `RandomizedSearchCV` to find the best-performing model.
- **Performance Optimization**: Prioritized the F1-Score as the key evaluation metric, balancing precision and recall, which is crucial for imbalanced datasets.
- **Interactive Web Application**: A Streamlit-based app that allows users to input customer data and receive real-time predictions regarding insurance plan subscription.

## Why XGBoost?

XGBoost was selected as the final model due to its superior performance in optimizing the F1-Score. After rigorous evaluation and hyperparameter tuning, XGBoost achieved an F1-Score of **0.6014**, making it the ideal choice for accurately predicting customer conversions, particularly in scenarios involving imbalanced classes.

## Repository Contents

- **`train.csv`**: The dataset used for training the machine learning models.
- **`app.py`**: The Streamlit application script for real-time customer conversion predictions.
- **`notebook.ipynb`**: Jupyter notebook containing exploratory data analysis (EDA) and initial model development.
- **`requirements.txt`**: A file listing the Python packages necessary to run the project.
- **`xgd_model.pkl`**: The serialized XGBoost model trained on the provided dataset.

## Installation and Setup

To set up this project locally, follow these instructions:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Dinakara-Prabhu-A/Customer-Conversion-Prediction.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Customer-Conversion-Prediction
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit web application**:
    ```bash
    streamlit run app.py
    ```

## Usage Instructions

Once the Streamlit application is running, you can input customer information into the app to receive a prediction on whether the customer is likely to subscribe to the insurance plan. The app provides an intuitive and user-friendly interface, making it accessible even for non-technical users.

## Contribution Guidelines

I welcome feedback and suggestions! If you encounter any issues or have ideas for improvement, please feel free to open an issue or submit a pull request.


## Acknowledgements

- **Guvi Datathon 1.0**: For providing the dataset and the challenge that inspired this project.
- **Open-Source Tools and Libraries**: This project was built using Python, XGBoost, Scikit-learn, Streamlit, and other essential libraries.
