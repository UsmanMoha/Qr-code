# importe les dépendances du qr code
import cv2

# créer un détecteur de lecteur de qrcode
d = cv2.QRCodeDetector()

# récupère les informations du qrcode
val, points, qrcode = d.detectAndDecode(cv2.imread('qrcode.png'))

# affiche les informations du qr code
print(val)
