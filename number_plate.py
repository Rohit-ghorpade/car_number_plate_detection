import cv2 


haar_cascade  = "model\car.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

min_area = 500
count = 0
 
#  loading the Haar Cascade
plate_casade = cv2.CascadeClassifier(haar_cascade
                                     )
while True:
    success , img = cap.read()
    
    if not success:
        print("Failed to capture video.")
        break
        
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    plates = plate_casade.detectMultiScale(img_gray, 1.1, 4)
    
    for (x, y, w, h) in plates:
        
        area = w*h
        
        if area>min_area:
            
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0) ,2)
            cv2.putText(img, "Number Plate", (x, y - 5, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2))
            
            img_roi = img[y: y+h, x: x+w]
            
            cv2.imshow("ROI", img_roi)
    
    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f"plates/scanned_img_{count}.jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (200, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1

cap.release()
cv2.destroyAllWindows()