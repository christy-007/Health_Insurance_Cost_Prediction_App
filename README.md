
![Health Insurance Cost Prediction](./banner.png)

# Health Insurance Cost Prediction App

## About the Project
This project involves building a machine learning model to predict health insurance costs based on various personal and health-related features. The main goal is to provide an easy-to-use web application where users can input their details and receive an estimated insurance cost instantly. The project leverages Streamlit for the frontend and is deployed on Heroku for accessibility.

## Project Overview

### Objective
The primary objective of this project is to predict health insurance costs using a regression model trained on a publicly available dataset. This can help individuals estimate their potential insurance costs based on their personal data and lifestyle choices.

### Features
- **User Input:** Users can input their age, sex, BMI, number of children, smoking status, and region.
- **Prediction:** The app predicts the insurance cost based on the input data.
- **Model Comparison:** The application uses multiple machine learning models to compare performance and accuracy.

### Technology Stack
- **Frontend:** Streamlit for the web interface.
- **Backend:** Python for model training and prediction.
- **Deployment:** Heroku for hosting the web app.
- **Libraries:** pandas, scikit-learn, joblib, matplotlib, tkinter.

### Dataset
The dataset used for this project is obtained from Kaggle, which includes features such as age, sex, BMI, number of children, smoking status, and region. This dataset is crucial for training the machine learning model to make accurate predictions.

- [Dataset on Kaggle](https://www.kaggle.com/datasets)

## Installation
To run the application locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Health_Insurance_Cost_Prediction_App.git
    cd Health_Insurance_Cost_Prediction_App
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run health_insurance.py
    ```

You can now view the app in your browser at `http://localhost:8501`.

## Deployment
The application is deployed on Heroku. To deploy your own version:

1. **Create a `Procfile` for Heroku:**
    ```arduino
    web: streamlit run health_insurance.py
    ```

2. **Install Heroku CLI and login:**
    ```bash
    heroku login
    ```

3. **Create a new Heroku app:**
    ```bash
    heroku create your-app-name
    ```

4. **Deploy the app:**
    ```bash
    git push heroku main
    ```

5. **Open the app in your browser:**
    ```bash
    heroku open
    ```

## Model Training and Evaluation
The model is trained using various regression algorithms including Linear Regression, Support Vector Regressor (SVR), Random Forest Regressor, and Gradient Boosting Regressor. The dataset is preprocessed to convert categorical variables into numerical values.

## GUI Options

### Streamlit
The Streamlit app allows users to input their data and get predictions on insurance costs. It features sliders and select boxes for easy input and displays the prediction result along with some animations.

### Tkinter
An alternative GUI option is provided using Tkinter, a Python library for creating desktop applications. Users can input their data in the fields provided and get predictions.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or feature requests.

## License
This project is licensed under the MIT License.

## Links
- [Dataset on Kaggle](https://www.kaggle.com/datasets)
- [Live Web App](https://your-app-name.herokuapp.com)
- [Streamlit](https://streamlit.io/)
- [Heroku](https://www.heroku.com/)

