# SpaceX Falcon 9 First Stage Landing Prediction

Predict whether the **Falcon 9 first stage will successfully land** using historical SpaceX launch data. This project follows a full applied ML workflow: data acquisition, cleaning, EDA, feature engineering, model training, hyperparameter tuning, and evaluation.

---

## Project Objective

Reusable Falcon 9 boosters reduce launch cost. The goal of this project is to build a classification model that predicts:

- **Target:** `Class`  
  - `1` = successful first-stage landing  
  - `0` = unsuccessful landing

This prediction can support cost estimation and operational planning.

---

## Data Sources

- **SpaceX API** (launch records, rocket/payload metadata)
- **Wikipedia** (tables containing landing outcomes and launch details)

> Note: Data is compiled for educational/portfolio use.

---

## Workflow

### 1) Data Collection
- Pulled structured launch data from the SpaceX REST API
- Scraped launch and landing outcome tables from Wikipedia
- Merged sources into a single modeling dataset

### 2) Data Cleaning & Preparation
- Handled missing values and inconsistent fields
- Selected relevant variables (e.g., payload mass, orbit, launch site)
- Converted categorical columns via one-hot encoding
- Built a clean feature matrix `X` and target label `y = Class`

### 3) Exploratory Data Analysis (EDA)
- Success rate by:
  - Launch site
  - Orbit type
  - Payload mass
  - Year / flight number
- Visualized relationships using scatter plots and bar charts

### 4) Modeling
Trained and compared multiple classifiers:
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbors (KNN)

### 5) Hyperparameter Tuning
- Used **GridSearchCV** with cross-validation to tune each model
- Selected best estimator based on validation performance

### 6) Evaluation
- Accuracy on test set
- Confusion matrix
- Classification report (precision/recall/F1 where applicable)

---

## Results

The best-performing model was selected after GridSearchCV tuning and evaluated on a held-out test set using accuracy and confusion-matrix-based diagnostics.

---

