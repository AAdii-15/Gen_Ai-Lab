# Experiment 1 — Parkinson's Disease Baseline Model

## Project

PulseIQ AI — Voice-Based Multi-Disease Early Detection System

---

# Objective

The objective of this experiment is to develop a baseline machine learning model capable of detecting Parkinson's disease from voice-derived acoustic biomarkers.

This experiment validates the hypothesis that voice features can be used for early disease detection.

---

# Dataset

Dataset: **UCI Parkinson's Dataset**

Source:
https://archive.ics.uci.edu/ml/datasets/parkinsons

Properties:

| Property          | Value                |
| ----------------- | -------------------- |
| Samples           | 195 voice recordings |
| Features          | 22 acoustic features |
| Subjects          | 31                   |
| Parkinson's cases | 147                  |
| Healthy controls  | 48                   |

Key Features:

* MDVP:Fo (fundamental frequency)
* Jitter measures
* Shimmer measures
* HNR (Harmonics-to-Noise Ratio)
* RPDE
* DFA
* PPE (Pitch Period Entropy)

---

# Data Preprocessing

Steps performed:

1. Loaded dataset using Pandas
2. Verified dataset structure
3. Checked for missing values
4. Removed non-informative column (`name`)
5. Separated features and labels
6. Split dataset into training and testing sets

Train/Test Split:

* Train: 80%
* Test: 20%

Stratified sampling was used to maintain class balance.

---

# Model

Algorithm used:

Random Forest Classifier

Reason:

* Works well with tabular biomedical data
* Handles nonlinear relationships
* Provides feature importance
* Robust to small datasets

Library: **Scikit-Learn**

---

# Evaluation Metrics

The following evaluation metrics were used:

* Accuracy
* Precision
* Recall (Sensitivity)
* F1 Score
* AUROC (Area Under ROC Curve)

Medical screening systems prioritize **recall** to avoid missing diseased patients.

---

# Results

Accuracy: **92.3%**

Confusion Matrix:

| Actual / Predicted | Healthy | Parkinson's |
| ------------------ | ------- | ----------- |
| Healthy            | 8       | 2           |
| Parkinson's        | 1       | 28          |

Classification Metrics:

| Metric                  | Value |
| ----------------------- | ----- |
| Precision (Parkinson's) | 0.93  |
| Recall (Parkinson's)    | 0.97  |
| F1 Score                | 0.95  |

AUROC Score:

**0.962**

This indicates excellent diagnostic discrimination.

---

# Feature Importance

Top predictive vocal biomarkers identified by the model:

1. PPE (Pitch Period Entropy)
2. spread1
3. MDVP:Fo(Hz)
4. NHR
5. Jitter:DDP
6. MDVP:Fhi(Hz)
7. MDVP:Flo(Hz)
8. spread2
9. Shimmer:APQ5
10. MDVP:RAP

These features correspond to known Parkinson's voice abnormalities such as vocal tremor, instability, and breathiness.

---

# Explainable AI

SHAP (SHapley Additive exPlanations) was used to interpret model predictions.

SHAP provides feature-level explanations showing how each acoustic biomarker contributes to the model's prediction.

Explainability is critical for healthcare AI to ensure trust and transparency.

---

# Conclusion

This baseline experiment demonstrates that acoustic voice features can effectively detect Parkinson's disease.

Key findings:

* High recall (0.97) ensures minimal missed diagnoses
* AUROC of 0.962 indicates strong predictive power
* Feature importance aligns with known neurological biomarkers

These results validate the feasibility of using voice as a digital biomarker for early disease screening.

---

# Next Steps

Future work includes:

* Extracting acoustic features from raw audio recordings
* Training models on larger datasets such as mPower
* Developing additional disease models (MCI, diabetes, cardiac conditions)
* Integrating models into a unified multi-disease screening pipeline
* Deploying the system as a real-time voice-based health screening tool
