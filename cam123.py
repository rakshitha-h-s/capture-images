import cv2 
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
no=0
while True:
    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite("./results2/result%04i.jpg" %no, frame)
            no+=1
            cv2.waitKey(1650)
            print("Processing image...")
            print("Image saved!")
       
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
