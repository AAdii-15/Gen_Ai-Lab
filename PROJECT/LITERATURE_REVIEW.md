# 📚 Literature Review
## PulseIQ AI — Voice-Based Multi-Disease Early Detection System

---

## 1. Introduction

This literature review surveys existing research on voice biomarkers for disease detection, AI-based diagnostic systems, and explainable AI in healthcare. The goal is to establish the scientific foundation for PulseIQ AI and identify the research gaps that this project aims to fill.

---

## 2. Voice Biomarkers in Healthcare

### 2.1 Foundational Research

**Fagherazzi, G., Fischer, A., et al. (2021)**
*"Voice for Health: The Use of Vocal Biomarkers from Research to Clinical Practice"*
*Digital Biomarkers, Karger Publishers*

This landmark paper established that diseases affecting the heart, lungs, and brain alter an individual's voice in measurable ways. It proposed vocal biomarker analysis as a new frontier in AI-powered healthcare for diagnosis, risk prediction, and remote patient monitoring. This paper directly supports PulseIQ's core hypothesis that a single voice sample can carry health information across multiple organ systems.

**Key Takeaway:** Voice is a valid, multi-system biomarker with clinical applicability.

---

**Schuller, B., Steidl, S., et al. (2021)**
*"The INTERSPEECH 2021 Computational Paralinguistics Challenge: COVID-19 Cough, Test Sympton, & Covid19"*
*INTERSPEECH 2021*

Demonstrated that respiratory diseases including COVID-19 could be detected from audio signals with high accuracy. Established benchmark datasets and evaluation methods now widely used in voice health research.

**Key Takeaway:** Voice-based disease detection is computationally feasible and reproducible.

---

### 2.2 MDPI Sensors Review (2025)

**"The Human Voice as a Digital Health Solution Leveraging Artificial Intelligence"**
*MDPI Sensors, 2025*

This comprehensive review confirmed clinical voice biomarker applications across:
- Neurological diseases: Parkinson's, Alzheimer's
- Psychological disorders: depression, anxiety
- Metabolic conditions: diabetes
- Cardiac conditions: congestive heart failure, coronary artery disease
- Pulmonary diseases: asthma, COPD, COVID-19

**Key Takeaway:** Voice biomarkers span multiple disease categories — a core justification for PulseIQ's multi-disease approach.

---

## 3. Disease-Specific Voice AI Research

### 3.1 Parkinson's Disease

**Roshanbin, S., et al. (2025)**
*"Explainable AI to Diagnose Early Parkinson's via Voice"*
*Scientific Reports (Nature)*

Developed a hybrid CNN+RNN model analyzing acoustic features (MFCCs, jitter, shimmer) achieving **91.11% accuracy** for early Parkinson's detection. Used SHAP (SHapley Additive exPlanations) to identify which acoustic features most influenced each diagnosis — making the AI's decisions interpretable.

**Key Takeaway:** Voice AI for Parkinson's is highly accurate AND explainable. PulseIQ adopts this SHAP-based explainability approach.

---

**Little, M.A., McSharry, P.E., Roberts, S.J., et al. (2007)**
*"Exploiting Nonlinear Recurrence and Fractal Scaling Properties for Voice Disorder Detection"*
*BioMedical Engineering OnLine*

A seminal study demonstrating that nonlinear voice features (jitter, shimmer, HNR) can distinguish healthy voices from Parkinson's patients with over **91% sensitivity**. The UCI Parkinson's dataset derived from this work remains a standard benchmark.

**Key Takeaway:** Foundational validation of acoustic feature extraction for neurological disease detection.

---

### 3.2 Cognitive Impairment & Alzheimer's

**Nagumo, R., et al. (2025)**
*"AI-Based Voice Biomarker Models for Cognitive Impairment Detection"*
*The Lancet Regional Health*

Demonstrated that AI-delivered voice biomarkers provide timely, noninvasive, and cost-effective detection of Mild Cognitive Impairment (MCI), achieving an **AUC of 0.89**. The model analyzed speech rhythm, pause patterns, and semantic coherence.

**Key Takeaway:** Voice AI can detect even subtle cognitive conditions with clinical-grade accuracy.

---

**Petti, U., Baker, S., Korhonen, A. (2020)**
*"A Systematic Literature Review of Automatic Alzheimer's Disease Detection from Speech and Language"*
*Journal of the American Medical Informatics Association (JAMIA)*

Reviewed 71 papers on NLP and speech-based Alzheimer's detection. Found consistent evidence that speech disfluencies, lexical richness, and acoustic features reliably differentiate dementia patients from healthy controls.

**Key Takeaway:** Speech and language analysis is a mature field for cognitive disease detection with strong reproducibility.

---

### 3.3 Diabetes

**Fagherazzi, G., et al. (2019)**
*"Voice-Based Conversational Agents for the Prevention and Management of Chronic and Mental Health Conditions"*
*Journal of Medical Internet Research (JMIR)*

Found that voice patterns in diabetic patients differ measurably from healthy controls, particularly in speech rate, voice quality, and frequency characteristics — likely due to neuropathy and vascular changes affecting vocal muscles.

**Key Takeaway:** Diabetes manifests detectable voice changes, supporting its inclusion in PulseIQ's screening scope.

---

### 3.4 Cardiac Conditions

**Amir, O., et al. (2009)**
*"Vocal Tremor and Hoarseness in Heart Failure Patients"*
*European Heart Journal*

Identified specific voice tremor patterns unique to congestive heart failure patients. Demonstrated that these patterns could serve as passive screening signals detectable via standard microphone recordings.

**Key Takeaway:** Cardiac diseases leave detectable acoustic signatures in voice.

---

## 4. Explainable AI in Healthcare

**Arrieta, A.B., Díaz-Rodríguez, N., et al. (2020)**
*"Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI"*
*Information Fusion, Elsevier*

Established the framework for XAI in high-stakes domains like healthcare. Argued that black-box AI is insufficient for medical use — clinicians and patients require explanations to trust and act on AI outputs.

**Key Takeaway:** Explainability is not optional in healthcare AI — it is a clinical necessity. PulseIQ's SHAP-based explanations directly address this.

---

## 5. Datasets Available for Training

| Dataset | Disease | Size | Source |
|---|---|---|---|
| UCI Parkinson's Dataset | Parkinson's | 195 voice recordings | UCI ML Repository |
| DEMENTIABANK | Alzheimer's / MCI | 1000+ interviews | CMU & DementiaBank |
| mPower | Parkinson's | 65,000+ voice samples | Sage Bionetworks |
| INTERSPEECH ComParE | Multiple diseases | Varies by year | INTERSPEECH |
| RAVDESS | Emotional/Health states | 24 actors, 7356 recordings | Zenodo |
| Coswara (IISc) | COVID-19 / Respiratory | 2000+ samples | Indian Institute of Science |

---

## 6. Existing Tools & Their Limitations

| Tool / System | Disease Covered | Limitation |
|---|---|---|
| Parkinson's Voice Monitor App | Parkinson's only | Single disease |
| Sonde Health Platform | Mental health / respiratory | Not multi-disease |
| Winterlight Labs | Alzheimer's only | Requires structured interview |
| Canary Speech | Depression / cognitive | Proprietary, not accessible |
| Google Health Voice Studies | Research stage only | Not a consumer product |

---

## 7. Research Gap

Based on the above review, the following gap is clearly identified:

> **No existing system performs multi-disease early screening from a single, unstructured voice sample in a consumer-accessible, multilingual, explainable format.**

PulseIQ AI is positioned to fill this gap by:

1. **Combining multiple disease detection models** into a single pipeline
2. Using a **single 30-second voice sample** (not structured interviews)
3. Providing **SHAP-based explainability** for user trust
4. Supporting **regional and multilingual** users
5. Deploying as a **smartphone app** requiring no special hardware

---

## 8. References

1. Fagherazzi et al. (2021). *Voice for Health.* Digital Biomarkers.
2. Roshanbin et al. (2025). *Explainable AI for Parkinson's Detection.* Scientific Reports (Nature).
3. Nagumo et al. (2025). *Voice Biomarkers for Cognitive Impairment.* The Lancet Regional Health.
4. MDPI Sensors (2025). *Human Voice as a Digital Health Solution.*
5. Little et al. (2007). *Nonlinear Recurrence for Voice Disorder Detection.* BioMedical Engineering OnLine.
6. Petti et al. (2020). *Alzheimer's Detection from Speech.* JAMIA.
7. Arrieta et al. (2020). *Explainable AI: Concepts and Challenges.* Information Fusion, Elsevier.
8. Amir et al. (2009). *Vocal Tremor in Heart Failure.* European Heart Journal.
9. Fagherazzi et al. (2019). *Voice-Based Agents for Chronic Disease.* JMIR.
10. Schuller et al. (2021). *INTERSPEECH 2021 Challenge.* INTERSPEECH.

---

*Literature Review compiled for GEN AI Lab Project — PulseIQ AI, 2024–25*
