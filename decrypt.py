import cv2

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def decrypt_image(image_path, password, correct_password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return
    if password != correct_password:
        print("YOU ARE NOT AUTHORIZED")
        return
    binary_message = ""
    for row in img:
        for pixel in row:
            for channel in range(3):
                binary_message += str(pixel[channel] & 1)
    message = binary_to_text(binary_message)
    if "###" in message:
        message = message[:message.index("###")]
    print("Decryption message:", message)
    

image_path = "encryptedImage.png"
pas = input("Enter passcode for Decryption: ")
decrypt_image(image_path, pas, pas)
