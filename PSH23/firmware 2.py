def find_url_indicator(decrypted_data):
    indicator = b'Q'
    for i in range(len(decrypted_data) - len(indicator) + 1):
        if decrypted_data[i:i+len(indicator)] == indicator:
            return i + len(indicator)
    return -1

# Charger le firmware déchiffré depuis le fichier
with open("firmware_decrypted.bin", "rb") as file:
    decrypted_firmware = file.read()

# Rechercher l'indicateur de l'URL dans le firmware déchiffré
index = find_url_indicator(decrypted_firmware)

if index != -1:
    print("Indicateur de l'URL trouvé à la position :", index)
    # Extraire l'URL à partir de l'indicateur trouvé
    url_bytes = decrypted_firmware[index:index+100]
    
    # Filtrer les caractères imprimables
    printable_chars = [chr(char) if 32 <= char < 127 else '?' for char in url_bytes]
    printable_url = ''.join(printable_chars)
    
    print("URL extrait brut :", printable_url)
    
    # Générer le hash MD5 de l'URL pour le format FLAG
    import hashlib
    md5_hash = hashlib.md5(url_bytes).hexdigest()
    print("MD5 de l'URL :", md5_hash)
    
    # Format FLAG avec l'URL brut et le MD5
    flag = f"FLAG{{{md5_hash}({printable_url})}}"
    print("Format FLAG complet :", flag)
else:
    print("Indicateur de l'URL non trouvé dans le firmware.")