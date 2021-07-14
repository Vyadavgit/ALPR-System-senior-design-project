# Reference: https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/project3.py
# OCR reference: https://www.geeksforgeeks.org/license-plate-recognition-with-opencv-and-tesseract-ocr/


import cv2

# imports for OCR after detection
import pytesseract
import matplotlib.pyplot as plt


#############################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("resources/haarcascade_plate_number.xml")
minArea = 200
color = (255,0,255)
###############################################
# cap = cv2.VideoCapture("Resources/video12.mp4") 
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
count = 0

while True:
    success, img = cap.read()
    # img = cv2.imread('Resources/lena.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area >minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img,"Number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)


    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("../static/scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)


        # program segment to read scanned license plates using OCR
        pytesseract.pytesseract.tesseract_cmd = 'F:/UTA Summer 2021/Senior design II/venvir/Lib/site-packages/Tesseract-OCR/tesseract.exe'
        # image_location = '../static/scanned/NoPlate_0.jpg'
        image_location = '../static/scanned/NoPlate_'+str(count)+'.jpg'
        ocr_img = cv2.imread(image_location)

        predicted_result = pytesseract.image_to_string(ocr_img)
        # predicted_result = pytesseract.image_to_string(ocr_img, lang ='eng',
        # config ='--oem 3 --psm 6 -c tessedit_char_whitelist = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

        filter_predicted_result = "".join(predicted_result.split()).replace(":", "").replace("-", "")
        print('\n')
        print("OCR result: " + predicted_result)
        print("Filtered OCR result: " + filter_predicted_result)


        # increment count for another image
        count +=1