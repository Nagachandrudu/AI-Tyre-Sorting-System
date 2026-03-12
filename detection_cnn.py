import cv2
import numpy as np
import serial
import time
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

MODEL = "tyre_model.keras"
IMG_SIZE = (224,224)
PORT = "COM7"
BAUD = 9600
CONF_THRESH = 0.75

model = load_model(MODEL)

cap = cv2.VideoCapture(1)

last_sent = None   # ⭐ KEY FIX

while True:
    ret, frame = cap.read()
    if not ret:
        break
      
    idx = np.argmax(preds)
    label = classes[idx]
    conf = preds[idx]

    if conf > CONF_THRESH:
            if label == "EMPTY":
                arduino.write(b'0')
                print("Sent EMPTY → Conveyor STOP")
            elif label == "STRAIGHT":
                arduino.write(b'1')
                print("Sent STRAIGHT")
            elif label == "ZIGZAG":
                arduino.write(b'2')
                print("Sent ZIGZAG")

            last_sent = label

    cv2.putText(frame, f"{label} {conf:.2f}",
                (10,40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0,255,255), 2)

    cv2.imshow("Tyre Sorting", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
