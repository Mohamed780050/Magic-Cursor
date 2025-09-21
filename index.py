import cv2
print(cv2.__version__)


# Webcam dimensions
wCam, hCam = 1280, 720

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
while True :
    success, img = cap.read()  # Capture frame from webcam
    if not success:
        break
    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

