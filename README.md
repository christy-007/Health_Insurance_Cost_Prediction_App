
![Health Insurance Cost Prediction](./banner.png)

This repository contains a web application for predicting health insurance costs using machine learning. The application is built with Streamlit and deployed on Heroku. The dataset used for training and testing the model is sourced from Kaggle.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [GUI Options](#gui-options)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

## Introduction

The Health Insurance Cost Prediction App uses a machine learning model to estimate the insurance cost based on various health-related features. The app provides an easy-to-use interface for users to input their data and receive cost predictions instantly.

## Dataset

The dataset used in this project is sourced from Kaggle and contains various features such as age, sex, BMI, children, smoker, and region.

- [Dataset on Kaggle](https://www.kaggle.com/datasets)

## Installation

To run this application locally, follow these steps:

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

## Usage

To run the Streamlit app locally, use the following command:

```bash
streamlit run health_insurance.py
