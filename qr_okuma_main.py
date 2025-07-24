import cv2
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0) #Kamerayı başlatır.

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) #CLAHE objesini oluşturur.

while True:
    ret, frame = cap.read()
    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # İmgeyi griye çevirir.
    
    gray = clahe.apply(gray) #Kontrastı artırır.
    
   
    _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Sırasıyla thresh-gray-color dener.
    barcodes = decode(th)
    if not barcodes:
        barcodes = decode(gray)
    if not barcodes:
        barcodes = decode(frame)

    # Bulduysan işaretle ve göster işlemini gerçekleştirir.
    for barcode in barcodes:
        data = barcode.data.decode('utf-8')
        print("QR Metni:", data)

        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, data, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("QR Scanner (Enhanced)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
