import cv2

# Importamos librerías
import smtplib
import mimetypes

# Importamos los módulos necesarios
from email.mime.multipart import MIMEMultipart

# Correo de acceso al servidor
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


## ------------------------------------------------------------------------------ ##
def enviarCorreo():
    # Creamos objeto Multipart, quien será el recipiente que enviaremos
    msg = MIMEMultipart()
    print("Correo Enviado - :)")
    msg['From']="correo-que-recibe"
    msg['To']="correo-que-envia"
    msg['Subject']="MOVIMIENTO DETECTADO"
    msg.attach(MIMEText("-- NUEVA ALERTA --"))

    # Adjuntamos Imagen
    file = open("c.jpg", "rb")
    attach_image = MIMEImage(file.read())
    attach_image.add_header('Content-Disposition', 'attachment; filename = "Alarma"')
    msg.attach(attach_image)

    # Autenticamos
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()  
    mailServer.ehlo()
    #https://www.google.com/settings/security/lesssecureapps   enlace para activar envío de correos desde mi cuenta
    mailServer.login("correo-que-envia","contraseña")

    # Enviamos
    mailServer.sendmail("correo-que-envia", "correo-que-recibe", msg.as_string())

    # Cerramos conexión
    mailServer.close()