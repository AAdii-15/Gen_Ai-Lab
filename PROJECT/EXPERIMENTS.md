# Experiments & Dataset Documentation — PulseIQ AI

## Project: PulseIQ AI — Voice-Based Multi-Disease Early Detection System

---

## Overview

This document details the dataset configurations, planned experiments, and any results obtained during the development of PulseIQ AI. The project is currently in the **dataset identification and feature extraction design phase**.

---

## 1. Datasets

### 1.1 UCI Parkinson's Dataset
| Property | Details |
|---|---|
| **Disease** | Parkinson's Disease |
| **Size** | 195 voice recordings from 31 subjects (23 with Parkinson's, 8 healthy) |
| **Features** | 22 acoustic features including MDVP:Fo, Jitter(%), Shimmer, HNR, RPDE, DFA |
| **Source** | UCI Machine Learning Repository |
| **URL** | https://archive.ics.uci.edu/ml/datasets/parkinsons |
| **Format** | CSV |
| **Label** | `status` — 1 = Parkinson's, 0 = Healthy |
| **Usage Plan** | Primary dataset for Parkinson's baseline model training and evaluation |

**Key Features Description:**

| Feature | Description |
|---|---|
| MDVP:Fo (Hz) | Average vocal fundamental frequency |
| MDVP:Jitter(%) | Variation in fundamental frequency (cycle-to-cycle) |
| MDVP:Shimmer | Variation in amplitude (cycle-to-cycle) |
| HNR | Harmonics-to-Noise Ratio |
| RPDE | Recurrence Period Density Entropy |
| DFA | Detrended Fluctuation Analysis |
| PPE | Pitch Period Entropy |

---

### 1.2 DementiaBank (Pitt Corpus)
| Property | Details |
|---|---|
| **Disease** | Alzheimer's Disease / Mild Cognitive Impairment (MCI) |
| **Size** | 1000+ interview recordings |
| **Source** | Carnegie Mellon University & DementiaBank Consortium |
| **URL** | https://dementia.talkbank.org/ |
| **Format** | Audio + transcripts (CHAT format) |
| **Label** | Diagnosis label: Control / MCI / Dementia |
| **Access** | Requires registration and data use agreement |
| **Usage Plan** | MCI and Alzheimer's detection model training |

---

### 1.3 mPower (Parkinson's mHealth Study)
| Property | Details |
|---|---|
| **Disease** | Parkinson's Disease |
| **Size** | 65,000+ voice samples from 9,500+ participants |
| **Source** | Sage Bionetworks |
| **URL** | https://www.synapse.org/#!Synapse:syn4993293 |
| **Format** | Audio (m4a/wav) + metadata |
| **Label** | Self-reported Parkinson's diagnosis |
| **Access** | Requires Synapse account and IRB agreement |
| **Usage Plan** | Large-scale Parkinson's model validation and generalization |

---

### 1.4 Coswara Dataset (IISc)
| Property | Details |
|---|---|
| **Disease** | COVID-19 / Respiratory conditions |
| **Size** | 2000+ samples |
| **Source** | Indian Institute of Science, Bangalore |
| **URL** | https://github.com/iiscleap/Coswara-Data |
| **Format** | Audio (wav) + metadata |
| **Label** | COVID-19 positive/negative + symptom data |
| **Usage Plan** | Respiratory condition baseline; also useful for Indian accent generalization |

---

### 1.5 INTERSPEECH ComParE Challenge Datasets
| Property | Details |
|---|---|
| **Disease** | Multiple (varies by year — COVID-19, Alzheimer's, depression, etc.) |
| **Source** | INTERSPEECH Computational Paralinguistics Challenge |
| **URL** | http://www.compare.openaudio.eu/ |
| **Format** | Audio + labels |
| **Usage Plan** | Supplementary datasets for model validation across disease categories |

---

## 2. Planned Experiments

### Experiment 1 — Parkinson's Baseline (UCI Dataset)
| Property | Details |
|---|---|
| **Objective** | Train a baseline classifier for Parkinson's detection |
| **Dataset** | UCI Parkinson's Dataset (195 samples) |
| **Features** | All 22 acoustic features from CSV |
| **Models** | Random Forest, SVM, XGBoost |
| **Evaluation Metrics** | Accuracy, Precision, Recall, F1-Score, AUC-ROC |
| **Explainability** | SHAP feature importance plots |
| **Status** | 🔲 Planned |

---

### Experiment 2 — Feature Extraction from Raw Audio
| Property | Details |
|---|---|
| **Objective** | Build a Python pipeline to extract acoustic features from raw .wav files |
| **Libraries** | Librosa, Parselmouth (Praat), OpenSMILE |
| **Features to Extract** | Jitter, Shimmer, HNR, MFCCs (13–40 coefficients), Pitch, Formants F1–F3, Speech rate, Pause duration |
| **Input** | Raw 30-second voice recording (.wav) |
| **Output** | Feature vector (CSV / JSON) |
| **Status** | 🔲 Planned |

---

### Experiment 3 — MCI / Cognitive Impairment Model
| Property | Details |
|---|---|
| **Objective** | Detect Mild Cognitive Impairment from voice and speech patterns |
| **Dataset** | DementiaBank Pitt Corpus |
| **Features** | Speech rhythm, pause frequency/duration, semantic coherence (NLP), acoustic features |
| **Models** | LSTM / Transformer-based model for sequential speech data |
| **Evaluation Metrics** | AUC-ROC (target: ≥0.85), Accuracy, F1 |
| **Status** | 🔲 Planned |

---

### Experiment 4 — Multi-Disease Pipeline Integration
| Property | Details |
|---|---|
| **Objective** | Combine all disease models into a single inference pipeline |
| **Input** | One 30-second voice recording |
| **Output** | Risk scores for all 4 diseases + SHAP explanations |
| **Approach** | Modular pipeline: shared feature extractor → disease-specific classifiers |
| **Status** | 🔲 Planned |

---

## 3. Evaluation Framework

All models will be evaluated using:

| Metric | Description |
|---|---|
| **Accuracy** | Overall correct predictions / total predictions |
| **Precision** | True Positives / (True Positives + False Positives) |
| **Recall (Sensitivity)** | True Positives / (True Positives + False Negatives) |
| **F1-Score** | Harmonic mean of Precision and Recall |
| **AUC-ROC** | Area Under the ROC Curve — key metric for medical screening |
| **SHAP Values** | Feature-level contribution to each prediction |

> In medical screening, **Recall (Sensitivity)** is prioritized over Precision — it is worse to miss a sick person than to flag a healthy one.

---

## 4. Current Status Summary

| Experiment | Status |
|---|---|
| Dataset identification | ✅ Complete |
| Literature-backed feature selection | ✅ Complete |
| Feature extraction pipeline | 🔲 Planned |
| Parkinson's baseline model | 🔲 Planned |
| MCI model | 🔲 Planned |
| Diabetes model | 🔲 Planned |
| Cardiac model | 🔲 Planned |
| Multi-disease integration | 🔲 Planned |
| SHAP explainability | 🔲 Planned |

---

*Last updated: March 2026*
