import qrcode

# Dados para o QR Code
data = "Hello, world!"

# Criação do objeto QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adiciona os dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Cria a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem do QR Code em um arquivo
img.save("qrcode.png")