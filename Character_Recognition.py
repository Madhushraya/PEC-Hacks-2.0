import cv2
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import time
from skimage import io

ocr = PaddleOCR(use_angle_cls=True, lang='en')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Press 'c' to capture a frame for OCR processing, 'q' to quit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        cv2.imshow("Webcam Feed", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            print("Capturing frame for OCR processing...")
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            results = ocr.ocr(np.array(pil_image), cls=True)
            if results and len(results[0]) > 0:
                recognized_texts = [res[1][0] for res in results[0]]
                print("\nRecognized Texts:")
                for text in recognized_texts:
                    print(text)
            else:
                print("\nNo text recognized in the captured frame.")

        elif key == ord('q'):  
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("\nInterrupted by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("Webcam feed closed.")
