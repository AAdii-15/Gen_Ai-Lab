import librosa
import numpy as np

def extract_features(audio_path):

    y, sr = librosa.load(audio_path, sr=None)

    # MFCC features
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc, axis=1)

    # Pitch
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch = np.mean(pitches[pitches > 0]) if np.any(pitches > 0) else 0

    # Spectral centroid
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))

    # Zero crossing rate
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    features = {
        "pitch": pitch,
        "spectral_centroid": spectral_centroid,
        "zcr": zcr
    }

    for i, mf in enumerate(mfcc_mean):
        features[f"mfcc_{i+1}"] = mf

    return features