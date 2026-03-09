# PulseIQ AI 🎙️

### *Detect Before it's Too Late — Just By Your Voice*

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Domain](https://img.shields.io/badge/Domain-Health%20%26%20Medical-red)
![AI](https://img.shields.io/badge/AI-Generative%20%7C%20Voice%20Biomarker-blue)

---

## Overview

**PulseIQ AI** is a voice-powered, multi-disease early detection system that analyzes a user's voice to identify early risk indicators of multiple diseases — all from a single 30-second voice sample. No wearables, no blood tests, no hospital visits required.

> "Your voice carries more health information than you think."

---

## Table of Contents

- [Problem Description](#problem-description)
- [Proposed Solution](#proposed-solution)
- [System Architecture](#system-architecture)
- [Diseases Targeted](#diseases-targeted)
- [Datasets](#datasets)
- [Related Work](#related-work)
- [Experiments & Results](#experiments--results)
- [Contributions](#contributions)
- [Tech Stack](#tech-stack)
- [Project Status](#project-status)
- [References](#references)

---

## Problem Description

Every year, millions of people are diagnosed with life-threatening diseases at advanced stages — when treatment becomes costly or impossible. Conditions like Parkinson's, Type 2 Diabetes, cardiovascular disease, and Mild Cognitive Impairment (MCI) are highly treatable when caught early, yet most cases go undetected until severe symptoms appear.

**Core Problem:** No single, non-invasive, accessible, and explainable early-screening tool exists for multiple diseases simultaneously.

Key pain points:
- Parkinson's disease loses 60–80% of dopaminergic neurons **before** clinical symptoms appear
- Type 2 Diabetes affects patients for an average of **7 years before diagnosis**
- MRI, PET scans cost thousands — inaccessible to rural and semi-urban populations
- Existing AI tools are **single-disease** and lack explainability

📄 Full details: [PROBLEM_DESCRIPTION.md](./PROBLEM_DESCRIPTION.md)

---

## Proposed Solution

PulseIQ AI addresses all pain points by:

1. Accepting a **30-second voice recording** as the only input
2. Extracting **acoustic biomarkers** (jitter, shimmer, MFCCs, pitch, HNR, formants)
3. Running the features through **disease-specific AI models** in a unified pipeline
4. Generating **risk scores** for multiple diseases simultaneously
5. Providing **SHAP-based explainability** — showing *why* the model flagged a risk
6. Being accessible via **any smartphone**, with no special hardware
7. Supporting **multilingual** users

---

## System Architecture

```
[User Voice Input - 30 sec]
        ↓
[Audio Preprocessing & Noise Reduction]
        ↓
[Acoustic Feature Extraction]
  → Jitter, Shimmer, HNR
  → MFCCs (Mel-Frequency Cepstral Coefficients)
  → Pitch, Formant Frequencies
  → Speech Rate & Pause Patterns
        ↓
[Multi-Disease AI Pipeline]
  ├── Parkinson's Detection Model (CNN+RNN)
  ├── Cognitive Impairment / MCI Model
  ├── Diabetes Risk Model
  └── Cardiac Condition Model
        ↓
[SHAP Explainability Layer]
        ↓
[Risk Report with Scores + Explanations]
```

---

## Diseases Targeted

| Disease | Key Voice Biomarkers | Target Accuracy |
|---|---|---|
| Parkinson's Disease | Jitter, Shimmer, HNR, MFCCs | ~91% |
| Mild Cognitive Impairment (MCI) | Speech rhythm, pause patterns, semantic coherence | AUC ~0.89 |
| Type 2 Diabetes | Speech rate, formant frequencies, voice quality | In progress |
| Cardiovascular Disease | Voice tremor, breathiness, hoarseness | In progress |

---

## Datasets

| Dataset | Disease | Size | Source |
|---|---|---|---|
| UCI Parkinson's Dataset | Parkinson's | 195 recordings | UCI ML Repository |
| DementiaBank | Alzheimer's / MCI | 1000+ interviews | CMU & DementiaBank |
| mPower | Parkinson's | 65,000+ samples | Sage Bionetworks |
| Coswara (IISc) | COVID-19 / Respiratory | 2000+ samples | Indian Institute of Science |
| INTERSPEECH ComParE | Multiple diseases | Varies | INTERSPEECH |

📄 Full experiment details: [EXPERIMENTS.md](./EXPERIMENTS.md)

---

## Related Work

A comprehensive literature review has been conducted covering:
- Voice biomarker research (Fagherazzi et al., 2021; MDPI Sensors, 2025)
- Parkinson's voice AI (Roshanbin et al., 2025; Little et al., 2007)
- Cognitive impairment detection (Nagumo et al., 2025; Petti et al., 2020)
- Diabetes & cardiac voice research
- Explainable AI in healthcare (Arrieta et al., 2020)

📄 Full review: [LITERATURE_REVIEW.md](./LITERATURE_REVIEW.md)

**Research Gap Identified:** No existing system performs multi-disease early screening from a single, unstructured voice sample in a consumer-accessible, multilingual, explainable format.

---

## Experiments & Results

📄 See: [EXPERIMENTS.md](./EXPERIMENTS.md)

Current stage: **Dataset identification and feature extraction pipeline design.**

Planned experiments:
- Baseline feature extraction on UCI Parkinson's dataset
- Model training and evaluation (accuracy, AUC, F1)
- SHAP explainability integration
- Multi-disease pipeline integration testing

---

## Contributions

📄 See: [CONTRIBUTIONS.md](./CONTRIBUTIONS.md)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Audio Processing | Librosa, PyAudio, SciPy |
| Feature Extraction | Praat (via Parselmouth), OpenSMILE |
| ML Models | Scikit-learn, TensorFlow / PyTorch |
| Explainability | SHAP |
| Frontend (planned) | React Native / Flutter |
| Backend (planned) | FastAPI / Flask |

---

## Project Status

- [x] Problem definition and background research
- [x] Literature review completed
- [x] Datasets identified
- [ ] Feature extraction pipeline (in progress)
- [ ] Model training — Parkinson's baseline
- [ ] Model training — MCI baseline
- [ ] Multi-disease pipeline integration
- [ ] SHAP explainability layer
- [ ] Frontend / app prototype

---

## References

1. Fagherazzi et al. (2021). Voice for Health. *Digital Biomarkers.*
2. Roshanbin et al. (2025). Explainable AI for Parkinson's Detection. *Scientific Reports (Nature).*
3. Nagumo et al. (2025). Voice Biomarkers for Cognitive Impairment. *The Lancet Regional Health.*
4. MDPI Sensors (2025). Human Voice as a Digital Health Solution.
5. Little et al. (2007). Nonlinear Recurrence for Voice Disorder Detection. *BioMedical Engineering OnLine.*
6. Petti et al. (2020). Alzheimer's Detection from Speech. *JAMIA.*
7. Arrieta et al. (2020). Explainable AI: Concepts and Challenges. *Information Fusion, Elsevier.*
8. Amir et al. (2009). Vocal Tremor in Heart Failure. *European Heart Journal.*
9. Schuller et al. (2021). INTERSPEECH 2021 Challenge. *INTERSPEECH.*
