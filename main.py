import cv2
from PIL import Image
from util import get_limits

colors = {
    'yellow': [0, 255, 255],
    'green': [0, 255, 0],
    'red': [0, 0, 255]
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, bgr_color in colors.items():
        lowerLimits, upperLimits = get_limits(color_name)

        # If there are multiple limits (like for red), we process each one
        for lowerLimit, upperLimit in zip(lowerLimits, upperLimits):
            mask = cv2.inRange(hsv_image, lowerLimit, upperLimit)
            
            mask_ = Image.fromarray(mask)
            bbox = mask_.getbbox()

            if bbox is not None:
                x1, y1, x2, y2 = bbox
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr_color, 2)
                cv2.putText(frame, color_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr_color, 2)

    cv2.imshow('frame', frame)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
