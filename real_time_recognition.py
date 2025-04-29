import cv2
import mediapipe as mp
import numpy as np
import pickle
import os
import time

def main():  # 🔹 Wrap everything inside main()

    MODEL_PATH = r"C:\Users\khush\Sem 6\HandSpeak\ASL hand recognition\src\asl_model.pkl"
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    DATASET_PATH = r"C:\Users\khush\Sem 6\HandSpeak\ASL hand recognition\dataset\asl_alphabet_train\asl_alphabet_train"
    labels = sorted(os.listdir(DATASET_PATH))

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, 
                          max_num_hands=1,
                          min_detection_confidence=0.7,
                          min_tracking_confidence=0.5)
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    last_prediction_time = 0
    prediction_interval = 2
    current_prediction = ""
    text_content = ""
    last_action_time = 0

    print("🎥 Starting real-time ASL recognition. Press 'q' to exit.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("❌ ERROR: Failed to capture image")
            break

        frame = cv2.flip(frame, 1)
        height, width = frame.shape[:2]

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append(lm.x)
                    landmarks.append(lm.y)

                current_time = time.time()
                if current_time - last_prediction_time >= prediction_interval:
                    landmarks = np.array(landmarks).reshape(1, -1)
                    prediction = model.predict(landmarks)
                    current_prediction = prediction[0]
                    last_prediction_time = current_time
                    
                    if current_time - last_action_time > 0.5:
                        if current_prediction.lower() == "space":
                            text_content += " "
                            last_action_time = current_time
                        elif current_prediction.lower() in ["del", "delete"]:
                            text_content = text_content[:-1]
                            last_action_time = current_time
                        elif len(current_prediction) == 1 and current_prediction.isalpha():
                            text_content += current_prediction.lower()
                            last_action_time = current_time

        cv2.putText(frame, f"Prediction: {current_prediction}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        if result.multi_hand_landmarks:
            time_remaining = max(0, prediction_interval - (current_time - last_prediction_time))
            cv2.putText(frame, f"Next in: {time_remaining:.1f}s", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

        text_box_height = 80
        cv2.rectangle(frame, (0, height - text_box_height), (width, height), (50, 50, 50), -1)
        cv2.putText(frame, f"Text: {text_content}", (20, height - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        cv2.putText(frame, "Press 'c' to clear text", (width - 250, height - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv2.imshow("ASL Hand Recognition", frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('c'):
            text_content = ""

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()  # 🔹 Run main only if this file is executed directly
