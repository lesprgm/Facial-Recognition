import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Error: Camera is not working")
        break

    cv2.imshow("Test Window", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cam.release()
cv2.destroyAllWindows()
