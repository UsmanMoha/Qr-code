# on importe le module qrcode
import qrcode
# on importe le module error_correction ERROR_CORRECT_M
from qrcode.constants import ERROR_CORRECT_M
# la variable qr contient l'objet qr code en lui donnant ses propres caractéristiques
qr = qrcode.QRCode(
    # version correspondant entre 1 et 40 qui va être la taille du qrcode plus au moins complexe visuellement
    version = 5,
    # environ 15% ou moins des erreurs peuvent être corrigées
    error_correction = ERROR_CORRECT_M,
    # taille de la bordure
    box_size = 5,
    # taille de la boite
    border = 7
)
# permet d'ajouter les informations dans le qrcode
qr.add_data('https://www.synopsisgroup.com/en/')
# détecte la taille du QR code et le créer
qr.make(fit=True)
# permet la personnalisation des couleurs du qr code
img = qr.make_image(fill_color="blue", back_color="white")
# permet la sauvegarde et la création du qrcode
img.save('synopsis.png')
