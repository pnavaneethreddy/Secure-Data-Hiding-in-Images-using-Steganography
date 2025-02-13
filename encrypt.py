import cv2
import os

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encrypt_image(image_path, message, password, output_path="encryptedImage.png"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return
    message += "###"
    binary_message = text_to_binary(message)
    data_index = 0
    total_bits = len(binary_message)
    for row in img:
        for pixel in row:
            for channel in range(3):
                if data_index < total_bits:
                    pixel[channel] = (pixel[channel] & 0xFE) | int(binary_message[data_index])
                    data_index += 1
                else:
                    break
    cv2.imwrite(output_path, img)
    print("Encryption complete. Saved as", output_path)
    return password


image_path = "mydog.png"
message = input("Enter secret message: ")
password = input("Enter a passcode: ")
correct_password = encrypt_image(image_path, message, password)