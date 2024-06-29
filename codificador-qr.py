import qrcode

texto_a_codificar = "Hola, me llamo marco" #texto a codificar

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=5,
)
qr.add_data(texto_a_codificar)
qr.make(fit=True)

# Crea una imagen del código QR
imagen_qr = qr.make_image(fill_color="green", back_color="white")

# Guarda la imagen en un archivo
imagen_qr.save("mi_codigo_qr.png")

print("Código QR generado y guardado como 'mi_codigo_qr.png'")