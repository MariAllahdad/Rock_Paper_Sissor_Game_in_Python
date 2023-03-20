import cv2
import random as rnd
from cvzone.HandTrackingModule import HandDetector
U_list = ['Rock','','Sessor','','','Paper']
C_list = ['Rock','Paper','Sissor']
U_select = ''
C_select = ''
U_score = 0
C_score = 0
result = '-'
cap= cv2.VideoCapture(0)
detect = HandDetector(detectionCon=0.5)
old_select = '-'
while(True):
    suc,img = cap.read()
    hands , img  = detect.findHands(img)
    if(hands):
        hand1 = hands[0]
        fingure1 = detect.fingersUp(hand1)
       # print(fingure1)
        score = 0
        for i in fingure1:
            score += i

        U_select = U_list[score]
        if old_select != U_select:
            C_select = rnd.choice(C_list)
            old_select = U_select
            if(U_select == C_select):
                result = 'Draw'
            elif( U_select == 'Paper' and C_select == 'Sissor'):
                result = 'Computer Win'
                C_score += 1
            elif (U_select == 'Paper' and C_select == 'Rock'):
                result = 'User Win'
                U_score +=1

            # elif (U_select == 'Paper' and C_select == 'Paper'):
            #     result = 'Draw'

            elif (U_select == 'Rock' and C_select == 'Paper'):
                result = 'Computer Win'
                C_score += 1
            elif (U_select == 'Rock' and C_select == 'Sissor'):
                result = 'User Win'
                U_score += 1

            elif (U_select == 'Sissor' and C_select == 'Rock'):
                result = 'Computer Win'
                C_score += 1
            elif (U_select == 'Sissor' and C_select == 'Paper'):
                result = 'User Win'
                U_score += 1

        cv2.putText(img,f'User: {U_select} Score: {U_score}' ,(10,30),cv2.FONT_HERSHEY_DUPLEX,1,(0,250,0),2)
        cv2.putText(img, f'Computer: {C_select} Score: {C_score}', (10, 80), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 250), 2)
        cv2.putText(img, f'Result: {result}', (10, 120), cv2.FONT_HERSHEY_DUPLEX, 1, (100, 50, 200), 2)
    cv2.imshow('Image1',img)
    if(cv2.waitKey(1) == 27):
        break

cap.release()
cv2.destroyAllWindows()
