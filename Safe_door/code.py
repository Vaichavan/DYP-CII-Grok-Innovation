model = None
categories = None


import cv2
import numpy as np
np.set_printoptions(suppress=True) # prevent numpy exponential
from tensorflow.keras.models import load_model
model = load_model("../model.h5")

categories = ['Cat', 'Dog', 'Elephant', 'Human', 'Peacock', 'Pig']

cap = cv2.VideoCapture(0)
while True:

  ret, frame = cap.read()

  image = cv2.resize(frame, (224, 224))
  image = np.expand_dims(image, axis=0)
  image = image / 255.0

  prediction = model.predict(image)[0]
  class_idx = np.argmax(prediction)
  class_label = categories[class_idx]
  confidence = prediction[class_idx] * 100

  cv2.putText(frame, f"{class_label} {confidence:.2f}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

  cv2.imshow("Live Camera", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
  		break

cap.release()
cv2.destroyAllWindows()
