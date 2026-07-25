import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# 1. Configure the Tasks Pipeline for Python 3.13
model_path = 'hand_landmarker.task'  # Must be saved in your project folder
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2
)

# 2. Hardcoded mapping of hand connections (Replaces mp_hands.HAND_CONNECTIONS)
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),        # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),        # Index Finger
    (9, 10), (10, 11), (11, 12),           # Middle Finger
    (13, 14), (14, 15), (15, 16),          # Ring Finger
    (0, 17), (17, 18), (18, 19), (19, 20), # Pinky Finger
    (5, 9), (9, 13), (13, 17)              # Palm Base Line
]

# 3. Initialize Video Feed
cap = cv2.VideoCapture(0)

with HandLandmarker.create_from_options(options) as landmarker:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
            
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        
        # Calculate time tracker index required for video tracking mode
        timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        
        # Format the BGR canvas layout into a native MediaPipe Image container
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        result = landmarker.detect_for_video(mp_image, timestamp_ms)
        
        # Process and draw custom graphics if coordinates are caught
        if result.hand_landmarks:
            for hand_landmarks in result.hand_landmarks:
                # Convert normalized decimal points back to integer pixel screen locations
                points = []
                for lm in hand_landmarks:
                    points.append((int(lm.x * w), int(lm.y * h)))
                
                # Draw the skeletal bone structures
                for start_idx, end_idx in HAND_CONNECTIONS:
                    if start_idx < len(points) and end_idx < len(points):
                        cv2.line(frame, points[start_idx], points[end_idx], (255, 0, 0), 2)
                
                # Draw the joint dots
                for pt in points:
                    cv2.circle(frame, pt, 5, (0, 0, 255), cv2.FILLED)
                    
        cv2.imshow("Python 3.13 MediaPipe Tasks Pipeline", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
