# 🚌 AI-Based Public Transportation Demand Prediction and Route Optimization

> **Mini Project Practice Repository**

This repository contains my learning and experimentation work for my engineering mini project: **AI-Based Dynamic Public Transportation Demand Prediction and Route Optimization During Large-Scale Events.**

The goal is to explore how machine learning, data analysis, and route optimization techniques can help understand public transportation demand during large-scale events.

**Note:** This is a practice and development repository. It is not a completed or production-ready transportation management system.

## 🎯 Learning Objectives

- Understand passenger demand analysis using Python.
- Explore machine learning algorithms for passenger demand prediction.
- Analyze transportation data from different depots.
- Experiment with event-based passenger demand estimation.
- Learn route optimization and bus allocation techniques.
- Integrate machine learning models with Django REST APIs.
- Explore Flutter application development.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Pandas & NumPy | Data processing |
| Scikit-learn | Machine learning |
| Matplotlib | Data visualization |
| Joblib | Model storage |
| Django | Backend development |
| Django REST Framework | API development |
| Flutter | Mobile application development |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
Bus/
│
├── Dataset/
│   ├── Harohalli_Passenger_Details.xlsx
│   ├── Ramanagara_Depot_Passengers.xlsx
│   ├── actual_route_passengers_HRH_RMN.csv
│   ├── event_data.csv
│   ├── event_features.csv
│   ├── event_route_scenarios.csv
│   ├── event_impact_estimates.csv
│   └── route_optimization_results.csv
│
├── models/
│   ├── passenger_model.pkl
│   └── combined_passenger_model.pkl
│
├── backend/
│   ├── config/
│   └── transport/
│
├── train.py
├── predict.py
├── evaluate.py
├── cross_validate.py
├── train_combined_model.py
├── predict_combined_model.py
├── compare_models.py
├── event_impact.py
├── route_optimizer.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚌 Dataset Information

The project currently uses passenger data from two depots:

- **Harohalli (HRH)**
- **Ramanagara (RMN)**

| Depot | Actual route records | Source month |
|---|---:|---|
| Harohalli | 55 | August 2026 |
| Ramanagara | 88 | October 2026 |
| **Total** | **143** | Different months |

The repository also contains simulated event data for experimenting with event-related demand scenarios.

### ⚠️ Dataset Disclaimer

- Actual passenger records and simulated records are kept distinguishable.
- Event attendance figures are simulated examples.
- Event-related passenger estimates use illustrative assumptions.
- Synthetic data must not be represented as real-world observations.
- The current dataset is limited and does not establish reliable future or event-specific forecasting accuracy.

## 🤖 Machine Learning Experiments

The following algorithms are being explored:

- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor

### Initial Model Evaluation

A combined Random Forest model produced these results:

| Metric | Result |
|---|---:|
| MAE | 2696.32 |
| RMSE | 3389.57 |
| R² Score | 0.771 |
| 5-Fold Grouped CV MAE | 2900.36 |

These are preliminary experimental results, not verified real-world forecasting performance.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Bus
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Train the combined model

```bash
python train_combined_model.py
```

### 6. Run passenger prediction

```bash
python predict_combined_model.py
```

### 7. Run event-impact estimation

```bash
python event_impact.py
```

### 8. Run route optimization

```bash
python route_optimizer.py
```

## 🌱 Development Progress

- [x] Initial passenger dataset inspection
- [x] Combine actual route records from both depots
- [x] Passenger demand analysis
- [x] Initial machine learning model
- [x] Model evaluation and cross-validation
- [x] Compare machine learning algorithms
- [x] Simulated event dataset
- [x] Event-impact estimation
- [x] Initial route optimization simulation
- [x] Django backend project initialization
- [ ] Passenger prediction REST API
- [ ] Event analysis REST API
- [ ] Flutter application integration
- [ ] Testing and final documentation

## 📚 Learning Purpose

This repository is part of my engineering mini-project learning journey. I am using it to understand practical implementation of machine learning, data preprocessing, backend development, and optimization techniques.

The implementation may change as I learn and improve the project.

## 🤝 Contributions

Suggestions, improvements, and learning contributions are welcome.

## 📄 License

This repository is intended for educational and academic practice. Dataset redistribution and reuse should follow the permissions and terms of the original data sources.# 🚌 AI-Based Public Transportation Demand Prediction and Route Optimization

> **Mini Project Practice Repository**

This repository contains my learning and experimentation work for my engineering mini project: **AI-Based Dynamic Public Transportation Demand Prediction and Route Optimization During Large-Scale Events.**

The goal is to explore how machine learning, data analysis, and route optimization techniques can help understand public transportation demand during large-scale events.

**Note:** This is a practice and development repository. It is not a completed or production-ready transportation management system.

## 🎯 Learning Objectives

- Understand passenger demand analysis using Python.
- Explore machine learning algorithms for passenger demand prediction.
- Analyze transportation data from different depots.
- Experiment with event-based passenger demand estimation.
- Learn route optimization and bus allocation techniques.
- Integrate machine learning models with Django REST APIs.
- Explore Flutter application development.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Pandas & NumPy | Data processing |
| Scikit-learn | Machine learning |
| Matplotlib | Data visualization |
| Joblib | Model storage |
| Django | Backend development |
| Django REST Framework | API development |
| Flutter | Mobile application development |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
Bus/
│
├── Dataset/
│   ├── Harohalli_Passenger_Details.xlsx
│   ├── Ramanagara_Depot_Passengers.xlsx
│   ├── actual_route_passengers_HRH_RMN.csv
│   ├── event_data.csv
│   ├── event_features.csv
│   ├── event_route_scenarios.csv
│   ├── event_impact_estimates.csv
│   └── route_optimization_results.csv
│
├── models/
│   ├── passenger_model.pkl
│   └── combined_passenger_model.pkl
│
├── backend/
│   ├── config/
│   └── transport/
│
├── train.py
├── predict.py
├── evaluate.py
├── cross_validate.py
├── train_combined_model.py
├── predict_combined_model.py
├── compare_models.py
├── event_impact.py
├── route_optimizer.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚌 Dataset Information

The project currently uses passenger data from two depots:

- **Harohalli (HRH)**
- **Ramanagara (RMN)**

| Depot | Actual route records | Source month |
|---|---:|---|
| Harohalli | 55 | August 2026 |
| Ramanagara | 88 | October 2026 |
| **Total** | **143** | Different months |

The repository also contains simulated event data for experimenting with event-related demand scenarios.

### ⚠️ Dataset Disclaimer

- Actual passenger records and simulated records are kept distinguishable.
- Event attendance figures are simulated examples.
- Event-related passenger estimates use illustrative assumptions.
- Synthetic data must not be represented as real-world observations.
- The current dataset is limited and does not establish reliable future or event-specific forecasting accuracy.

## 🤖 Machine Learning Experiments

The following algorithms are being explored:

- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor

### Initial Model Evaluation

A combined Random Forest model produced these results:

| Metric | Result |
|---|---:|
| MAE | 2696.32 |
| RMSE | 3389.57 |
| R² Score | 0.771 |
| 5-Fold Grouped CV MAE | 2900.36 |

These are preliminary experimental results, not verified real-world forecasting performance.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/darshanmr-911/AI-based-public-transportation-demand-prediction-and-route-optimization..git

cd Bus
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Train the combined model

```bash
python train_combined_model.py
```

### 6. Run passenger prediction

```bash
python predict_combined_model.py
```

### 7. Run event-impact estimation

```bash
python event_impact.py
```

### 8. Run route optimization

```bash
python route_optimizer.py
```

## 🌱 Development Progress

- [x] Initial passenger dataset inspection
- [x] Combine actual route records from both depots
- [x] Passenger demand analysis
- [x] Initial machine learning model
- [x] Model evaluation and cross-validation
- [x] Compare machine learning algorithms
- [x] Simulated event dataset
- [x] Event-impact estimation
- [x] Initial route optimization simulation
- [x] Django backend project initialization
- [ ] Passenger prediction REST API
- [ ] Event analysis REST API
- [ ] Flutter application integration
- [ ] Testing and final documentation

## 📚 Learning Purpose

This repository is part of my engineering mini-project learning journey. I am using it to understand practical implementation of machine learning, data preprocessing, backend development, and optimization techniques.

The implementation may change as I learn and improve the project.

## 🤝 Contributions

Suggestions, improvements, and learning contributions are welcome.

## 📄 License

This repository is intended for educational and academic practice. Dataset redistribution and reuse should follow the permissions and terms of the original data sources.