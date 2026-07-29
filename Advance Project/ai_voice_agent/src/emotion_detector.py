import librosa
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

# Load pre-trained model (train separately on emotion dataset)
model = joblib.load("data/emotion_model.pkl")
scaler = joblib.load("data/emotion_scaler.pkl")

def detect_emotion(audio_file: str) -> str:
    y, sr = librosa.load(audio_file)
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    features = scaler.transform([mfccs])
    prediction = model.predict(features)[0]
    return prediction
