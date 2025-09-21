import cv2
import math
import HandTrackingModule as htm  # Assuming this is a custom module for hand tracking

# Webcam dimensions
wCam, hCam = 640, 480

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Hand tracking module
detector = htm.FindHands(detection_con=0.7)  # Assuming HandDetector class has a 'detectionCon' parameter

while True :
    success, img = cap.read()  # Capture frame from webcam
    if not success:
        break

    # Detect hands and landmarks
    img = detector.getHands(img)
    lmList = detector.getPosition(img, indexes=[4,8, 12], draw=False)  # List of hand landmarks

    if len(lmList) == 3:  # Ensure both landmarks are detected
        x1, y1 = lmList[0]  # Thumb tip
        x2, y2 = lmList[1]  # Index finger tip
        x3, y3 = lmList[2]  # Middle finger tip

        # Calculate the center point between the finger tips
        cx1, cy1 = (x1 + x2) // 2, (y1 + y2) // 2
        cx2, cy2 = (x1 + x3) // 2, (y1 + y3) // 2

        # Draw circles and line connecting the thumb and index finger
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx1, cy1), 15, (255, 0, 255), cv2.FILLED)
        # Draw circles and line connecting the thumb and middle finger
        cv2.circle(img, (x3, y3), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x3, y3), (255, 0, 255), 3)
        cv2.circle(img, (cx2, cy2), 15, (255, 0, 255), cv2.FILLED)

        # Calculate the length between the thumb and index finger
        length1 = math.hypot(x2 - x1, y2 - y1)
        # Calculate the length between the middle and index finger
        length2 = math.hypot(x3 - x1, y3 - y1)

        # Visual cue when thump and index fingers are closed
        if length1 < 50:
            cv2.circle(img, (cx1, cy1), 15, (0, 255, 0), cv2.FILLED)
        # Visual cue when thump and middle fingers are closed
        if length2 < 50:
            cv2.circle(img, (cx2, cy2), 15, (0, 255, 0), cv2.FILLED)

    # Show webcam feed
    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

