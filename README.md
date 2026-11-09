# 🚌 AI-Based Public Transportation Demand Prediction and Route Optimization

> **Engineering Mini Project – Practice Repository**

This repository contains my learning and experimentation work for my engineering mini project:

**AI-Based Dynamic Public Transportation Demand Prediction and Route Optimization During Large-Scale Events.**

The main purpose of this repository is to practise Python programming, Machine Learning, data analysis, and route optimization techniques using public transportation datasets.

**Note:** This is an experimental practice repository, not a completed or production-ready transportation system.

## 🔗 GitHub Repository

[View Repository](https://github.com/darshanmr-911/AI-based-public-transportation-demand-prediction-and-route-optimization.)

### Clone Repository

```bash
git clone https://github.com/darshanmr-911/AI-based-public-transportation-demand-prediction-and-route-optimization..git

cd AI-based-public-transportation-demand-prediction-and-route-optimization.
```

## 🎯 Learning Objectives

- Practise Python programming and data preprocessing.
- Understand passenger demand analysis.
- Explore Machine Learning algorithms.
- Experiment with passenger demand prediction.
- Analyse transportation data from different depots.
- Explore event-based passenger demand estimation.
- Practise route optimization and bus allocation.
- Learn model evaluation and cross-validation.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Matplotlib | Data visualization |
| Joblib | Model serialization |
| Git | Version control |
| GitHub | Repository management |

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

The project uses passenger data from two depots:

| Depot | Actual route records | Source month |
|---|---:|---|
| Harohalli (HRH) | 55 | August 2026 |
| Ramanagara (RMN) | 88 | October 2026 |
| **Total** | **143** | Different months |

The repository also contains simulated event data for experimenting with event-related demand scenarios.

### Dataset Disclaimer

- Actual and simulated records are distinguished.
- Event attendance figures are simulated examples.
- Event-related estimates use illustrative assumptions.
- Synthetic data is not real-world ground truth.
- The current dataset does not establish reliable future or event-specific forecasting accuracy.

## 🤖 Machine Learning Experiments

The following algorithms are explored:

- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor

### Initial Model Evaluation

| Metric | Result |
|---|---:|
| MAE | 2696.32 |
| RMSE | 3389.57 |
| R² Score | 0.771 |
| 5-Fold Grouped CV MAE | 2900.36 |

These are preliminary experimental results, not verified real-world forecasting performance.

## ⚙️ Features and Experiments

- Passenger data inspection and preprocessing.
- Combining actual route records from two depots.
- Depot-wise passenger demand analysis.
- Machine Learning model training.
- Passenger demand prediction.
- Model evaluation and cross-validation.
- Comparison of different ML algorithms.
- Simulated event-demand estimation.
- Route prioritization and bus allocation experiments.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/darshanmr-911/AI-based-public-transportation-demand-prediction-and-route-optimization..git

cd AI-based-public-transportation-demand-prediction-and-route-optimization.
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

### 6. Predict passenger demand

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

- [x] Dataset inspection
- [x] Combine actual route records
- [x] Passenger demand analysis
- [x] Initial Machine Learning model
- [x] Model evaluation
- [x] Cross-validation
- [x] Compare ML algorithms
- [x] Simulated event dataset
- [x] Event-impact estimation
- [x] Initial route optimization simulation
- [ ] Improve prediction performance
- [ ] Improve route optimization
- [ ] Experiment with additional ML algorithms
- [ ] Final analysis and documentation

## 📚 Learning Purpose

This repository is part of my engineering mini-project learning journey.

I am using it to gain practical experience in Python, Machine Learning, data preprocessing, model evaluation, and optimization techniques.

The implementation may change as I continue learning and experimenting.

## 🤝 Contributions

Suggestions, improvements, and learning contributions are welcome.

## 📄 License

This repository is intended for educational and academic practice. Dataset reuse and redistribution should follow the permissions and terms of the original data sources.

---

**Project Type:** Engineering Mini Project Practice

**Focus:** Python | Machine Learning | Data Analysis | Route Optimization