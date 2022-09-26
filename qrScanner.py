# For creating the QR code scanner you need to import cv2 & browser library.
import cv2
import webbrowser


# for capturing the QR code
cam = cv2.VideoCapture(0)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# Tis loop will read your webcam screen
while True:
    _, img = cam.read()

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    
    # check if there is a QRCode in the image
    if data:
        a=data
        break
    
    # This will produce the output
    cv2.imshow("QR_Code_Scanner", img)
    
    # if the 'q' key is pressed, stop the loop(video streaming).
    if cv2.waitKey(1) == ord("q"):
        break

# You've to create the variable for call the Object
b=webbrowser.open(str(a))

# otherwise, release the camera
cam.release()

# close all windows
cv2.destroyAllWindows()
