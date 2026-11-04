<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&center=true&vCenter=true&width=600&lines=CSE-422+%7C+Artificial+Intelligence;A*+Search+%7C+Alpha-Beta+%7C+Genetic+Algorithms;Customer+Churn+Prediction" alt="Typing SVG" />
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:3776AB,100:00C2A8&height=180&section=header&text=CSE-422%20AI&fontSize=45&fontColor=ffffff&animation=fadeIn" width="100%"/>
</div>

<div align="center">

# 📉 Customer Churn Prediction

[← Back to CSE422 repository](../README.md)

### A Comparative Study of Classification and Clustering Models

**CSE422: Artificial Intelligence — Lab Project · BRAC University**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?logo=tensorflow&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white)

</div>

---

## 📖 Overview

Customer churn prediction helps a business identify customers who are likely to leave **before** they do, so it can step in with discounts, personalised offers, or better service, which is typically far cheaper than acquiring new customers.

This project builds and compares three supervised models and one unsupervised model on a churn dataset of **1,500 customers**:

| Type | Model |
|------|-------|
| Supervised | Logistic Regression (linear baseline) |
| Supervised | K-Nearest Neighbors (instance-based) |
| Supervised | Neural Network (Keras Sequential) |
| Unsupervised | K-Means Clustering (label-free segmentation) |

> **Key finding:** All three supervised models perform close to random guessing. The available features carry very little predictive signal for churn in this dataset.

---

## 📊 Results at a Glance

Weighted-average metrics on the held-out test set (300 samples):

| Model | Accuracy | Precision | Recall | F1 | AUC |
|-------|:--------:|:---------:|:------:|:--:|:---:|
| **Logistic Regression** | **0.53** | 0.54 | 0.53 | 0.53 | 0.53 |
| KNN (k = 1) | 0.49 | 0.49 | 0.49 | 0.49 | 0.49 |
| Neural Network | 0.47 | 0.47 | 0.47 | 0.47 | 0.47 |

- All ROC curves sit very close to the random-guess diagonal.
- Correlations between every numerical feature and `Churn` are near zero (|r| < 0.04).
- K-Means showed no clear elbow, and silhouette scores stayed low (max ≈ 0.145), so there are no well-defined natural customer segments.

**Takeaway:** the dataset likely lacks the features that actually drive churn, or churn here is largely driven by random or unobserved factors.

---

## 🗂️ Dataset

- **Size:** 1,500 rows × 9 columns (including target)
- **Target:** `Churn` (1 = churned, 0 = retained)

| Feature | Type | Description / Unique Values |
|---------|------|-----------------------------|
| `Age` | Numerical | 52 unique values |
| `Income` | Numerical | 1,425 unique values |
| `Gender` | Categorical | Female, Male, Other |
| `Marital_Status` | Categorical | Married, Single, Divorced |
| `Credit_Score` | Numerical | 1,425 unique values |
| `Num_Purchases` | Numerical | 15 unique values |
| `Membership_Years` | Numerical | 14 unique values |
| `Device_Used` | Categorical | Desktop, Mobile, Tablet |
| `Churn` | Binary (target) | 0 / 1 |

The notebook reads the data from a CSV file named `3.csv`. Place it in the project root (see [Getting Started](#-getting-started)).

---

## 🔬 Methodology

### 1. Exploratory Data Analysis
- Density plots, histograms, and boxplots for numerical features
- Correlation heatmap (no strong feature-feature or feature-target correlation, so no multicollinearity concern)
- Count plots for categorical features (all well balanced)
- Found one invalid negative `Income` value and several missing values

### 2. Pre-processing
1. Dropped the row with negative income (1500 → 1499 rows); confirmed no duplicates
2. **80/20 train/test split** *before* imputation to avoid data leakage
3. Imputation, fit on the training set only:
   - `Age`, `Income`, `Credit_Score`: mean (`SimpleImputer`)
   - `Gender`: most frequent category
4. Merged `Mobile` + `Tablet` into one **Portable** category (churn rates were nearly identical)
5. One-Hot Encoding with `drop='first'`
6. `StandardScaler` (fit on train only)
7. Final shape: **1,199 training / 300 test samples, 10 features**

### 3. Models

| Model | Configuration |
|-------|---------------|
| Logistic Regression | `max_iter=10000` |
| KNN | Grid search over `k ∈ {1…20}`, 3-fold CV → best `k = 1` |
| Neural Network | Dense(16, ReLU) → Dense(8, ReLU) → Dense(1, Sigmoid); Adam, binary cross-entropy, 100 epochs, batch size 32 |
| K-Means | Elbow + Silhouette analysis for k = 2…29; k = 11 chosen as a practical trade-off |

### 4. Evaluation
Accuracy, precision, recall, F1-score, confusion matrices, and ROC-AUC curves.

---


## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook / JupyterLab (or Google Colab)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Akib-Zawad47/CSE-422-Artificial-Intelligence.git
cd /CSE-422-Artificial-Intelligence/Project

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install numpy pandas seaborn matplotlib scikit-learn tensorflow jupyter
```

### Run

```bash
jupyter notebook Customer_Churn_Prediction.ipynb
```

Make sure `3.csv` is in the same folder as the notebook, then run all cells in order.

---

## 🛠️ Tech Stack

- **Data handling:** NumPy, pandas
- **Visualization:** Matplotlib, Seaborn
- **Machine learning:** scikit-learn (Logistic Regression, KNN, K-Means, preprocessing, metrics)
- **Deep learning:** TensorFlow / Keras

---

## 🔭 Future Work

- Collect richer behavioural features such as support tickets, usage frequency, and billing history
- Re-evaluate with a dataset where churn has a measurable relationship with the features
- Explore class-imbalance handling and tree-based models once stronger signal is available

---

## 👥 Authors

| Name | Student ID |
|------|-----------|
| Akib Zawad | 24101519 |
| Muntafid Islam Nafsi | 24141057 |

Department of Computer Science and Engineering, **BRAC University**
Course: **CSE422 — Artificial Intelligence**

---

## 📄 License

This project was created for academic purposes. Add a license of your choice (e.g., MIT) if you wish to share it openly.
