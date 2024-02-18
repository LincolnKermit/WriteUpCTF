def decrypt_firmware(data, key):
    decrypted_data = bytearray()
    for byte in data:
        decrypted_data.append(byte ^ key)
    return decrypted_data

# Charger le firmware depuis le fichier
with open("firmware", "rb") as file:
    firmware_data = bytearray(file.read())

# Déchiffrer le firmware avec la clé 127 (0x7F)
decrypted_firmware = decrypt_firmware(firmware_data, 0x7F)

# Sauvegarder le firmware déchiffré
with open("firmware_decrypted.bin", "wb") as file:
    file.write(decrypted_firmware)