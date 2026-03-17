# Experiment 2 — Audio Feature Extraction from Raw Voice

## Project

PulseIQ AI — Voice-Based Multi-Disease Early Detection System

---

# Objective

The objective of this experiment is to build a pipeline that extracts acoustic and clinical voice biomarkers directly from raw voice recordings.

Unlike Experiment 1, which used pre-extracted dataset features, this stage processes **raw audio signals** to generate features suitable for machine learning models.

---

# Input

Input data consists of voice recordings in `.wav` format.

Example:

test_voice.wav

Voice samples are stored in:

data/audio_samples/

---

# Feature Extraction Pipeline

The feature extraction system combines:

* Librosa (signal processing)
* Parselmouth (Praat-based clinical voice analysis)

Pipeline:

Voice Recording (.wav)
↓
Signal Processing
↓
Feature Extraction
↓
Feature Vector

---

# Extracted Features

## 1. Acoustic Features (Librosa)

* Pitch → fundamental frequency of voice
* Spectral Centroid → brightness of sound
* Zero Crossing Rate (ZCR) → signal variation

## 2. Clinical Voice Biomarkers (Parselmouth / Praat)

* Jitter → frequency instability of vocal folds
* Shimmer → amplitude instability
* HNR (Harmonic-to-Noise Ratio) → breathiness of voice

These are critical biomarkers used in **Parkinson’s voice research**.

---

## 3. MFCC Features

* MFCC_1 to MFCC_13
* Represent the spectral envelope of speech
* Widely used in speech recognition and audio ML

---

# Output

The extracted features form a structured feature vector:

pitch
spectral_centroid
zcr
jitter
shimmer
hnr
mfcc_1 ... mfcc_13

These are converted into a Pandas DataFrame.

---

# Implementation

The feature extraction module is implemented in:

src/feature_extraction/audio_features.py

Libraries used:

* Librosa
* NumPy
* Parselmouth

---

# Example Output

Example feature values extracted from a test recording:

pitch: 808.33
spectral_centroid: 2750.94
zcr: 0.0588
jitter: 0.0232
shimmer: 0.1281
hnr: 11.34

---

# Significance

This experiment enables the system to process **real voice recordings instead of pre-computed dataset features**.

This is a critical step toward building a real-time voice-based health screening system.

---

# Next Step

The next stage connects the feature extraction pipeline with machine learning models to perform disease prediction from voice input.
