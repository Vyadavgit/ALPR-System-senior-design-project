from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from accounts.decorators import unauthenticated_user
from accounts.models import *


# imports for OenCV and OCR
import cv2
import pytesseract
import matplotlib.pyplot as plt

# Create your views here.
@login_required(login_url='login')
def detectFn(request):

    ###############################################
    frameWidth = 640
    frameHeight = 480

    new_path = 'F:/UTA Summer 2021/Senior design II/venvir/Lib/site-packages/cv2/'
    nPlateCascade = cv2.CascadeClassifier(new_path + 'data/haarcascade_russian_plate_number.xml')
    minArea = 200
    color = (255,0,255)
    ###############################################
    # cap = cv2.VideoCapture("Resources/video12.mp4") # comment left for rererence 
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10,150)
    count = 0

    while True:
        success, img = cap.read()

        # press key 'd' to deactivate the camera/terminate the detection program
        if cv2.waitKey(1) & 0xFF == ord('d'):
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            messages.success(request,'License detection deactivated.')
            return redirect('dashboard')

        # img = cv2.imread('Resources/lena.png') # comment left for rererence 
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

        # press key 's' to save the detected license plate
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("static/scanned/NoPlate_"+str(count)+".jpg",imgRoi)
            cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
            cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                        2,(0,0,255),2)
            cv2.imshow("Result",img)
            cv2.waitKey(500)


            # program segment to read scanned license plates using OCR
            pytesseract.pytesseract.tesseract_cmd = 'F:/UTA Summer 2021/Senior design II/venvir/Lib/site-packages/Tesseract-OCR/tesseract.exe'
            # image_location = '../static/scanned/NoPlate_0.jpg' # comment left for rererence 
            image_location = 'static/scanned/NoPlate_'+str(count)+'.jpg'
            ocr_img = cv2.imread(image_location)

            predicted_license = pytesseract.image_to_string(ocr_img)
            # predicted_license = pytesseract.image_to_string(ocr_img, lang ='eng',
            # config ='--oem 3 --psm 6 -c tessedit_char_whitelist = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') # comment left for rererence 

            filter_predicted_license = "".join(predicted_license.split()).replace(":", "").replace("-", "")
            print('\n')
            print("OCR result: " + predicted_license)
            print("Filtered OCR result: " + filter_predicted_license)


            try:
                vehicle = Vehicle.objects.get(license_plate = filter_predicted_license)
                print("Gate opened and access allowed for vehicle " + filter_predicted_license + ".")
                print('\n')

                # TODO
                # Initial parking status:
                print("Initial parking status: " + str(vehicle.parked))
                if vehicle.parked is False:
                    vehicle.parked=True
                    vehicle.save()
                    print('The vehicle [' + filter_predicted_license + '] entered the parking garage.')
                    messages.success(request,'The vehicle [' + filter_predicted_license + '] entered the parking garage.')
                    
                else:
                    vehicle.parked=False
                    vehicle.save()
                    print('The vehicle [' + filter_predicted_license + '] exited the parking garage.')
                    messages.success(request,'The vehicle [' + filter_predicted_license + '] exited the parking garage.')

                # Final parking status:
                print("Final parking status: " + str(vehicle.parked))      
                print('\n')    

            except ObjectDoesNotExist:
                print("Access denied for vehicle " + filter_predicted_license + ". Please register your vehicle.")
                print('\n')
                messages.warning(request,'Access denied for vehicle ' + filter_predicted_license + '. Please register your vehicle.')
                

            # increment count for another image
            # since 'detect' url is triggered again at the end of 'detectFn' the increment in count doesn't make any difference(i.e updates NoPlate_0 again and again), however,
            # if any other pages is to be rendered or any other url/function is to be redirected, in that case the  same openCv window
            # can be used to detect as many number plates as possible unless the window is terminated
            count +=1

            return redirect('detect')

        # this code segment has been moved up from here for better performance/easy termination of the detection program
        # # press key 'd' to deactivate the camera/terminate the detection program (this elif condition if put here only works while the rectange has been detected
        # and is in the state of being recognized)
        # elif cv2.waitKey(1) & 0xFF == ord('d'):
        #     cv2.waitKey(1)
        #     cv2.destroyAllWindows()
        #     cv2.waitKey(1)
        #     messages.success(request,'License detection deactivated.')
        #     return redirect('dashboard')

@login_required(login_url='login')
def notificationsFn(request):
    return render(request, 'license/notifications.html')
