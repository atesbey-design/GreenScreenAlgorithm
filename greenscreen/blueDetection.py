import numpy as np
import cv2

def nothing(x):#boş bir fonksiyon tanımlıyoruz nedenenini bilmiyorum
    pass
image=cv2.imread("hayat.jpg")
img=np.zeros((512,512,3),np.uint8)# sıfır tanımlı bir matris oluşturdum amaç siyah ekran döndermek
cv2.namedWindow("trackbar")#alanın gözükmesi için bir isim vardim
cv2.createTrackbar("R","trackbar",0,255,nothing)#RED(R) trackbara ekledim ve değer aralığını 0 255 aralığında tanımladım,gerekli olduğun için nothing fonksiyonunu buraya ekledim
cv2.createTrackbar("G","trackbar",0,255,nothing)#GREEN(G) trackbara ekledim  ve değer aralığını 0 255 aralığında tanımladım
cv2.createTrackbar("B","trackbar",0,255,nothing)#BLUE(B) trackbara ekledim ve değer aralığını 0 255 aralığında tanımladım
switch="1 ON \n 2 OFF" #bir anahtar bilgisi girdim
cv2.createTrackbar(switch,"trackbar",0,1,nothing)#bu   anahtar değişkeninin aralığını 1 0 olarak ayarlayıp tekrardan işleme soktum

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))
    width = int(cap.get(3))
    height = int(cap.get(4))
    r = cv2.getTrackbarPos("R", "trackbar")
    g = cv2.getTrackbarPos("G", "trackbar")
    b = cv2.getTrackbarPos("B", "trackbar")
    s = cv2.getTrackbarPos(switch, "trackbar")
    if s == 1:
        print(r,g,b)
    if s == 0:
        img[:] = (b, g, r)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0, 0, 0])
    upper_blue = np.array([r, g, b])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    f=result-frame
    green_screen=np.where(f==0,image,f)
    cv2.imshow("Frame",frame)
    cv2.imshow("GreenScreen",green_screen)

    cv2.imshow('mask', mask)
    cv2.imshow("trackbar",img)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()