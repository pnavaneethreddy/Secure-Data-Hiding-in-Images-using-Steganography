# Secure Data Hiding in Images using Steganography

## Introduction
Steganography is the practice of concealing secret information within an image in such a way that its presence is not detectable. This project demonstrates a secure approach to data hiding in images using steganographic techniques, ensuring confidentiality and integrity.

## Features
- **Image-based Steganography**: Hide secret messages within image files.
- **Encryption Support**: Secure the hidden data using encryption before embedding.
- **Lossless Extraction**: Retrieve the hidden data without degrading the quality of the image.
- **Multiple Image Format Support**: Works with PNG, BMP, and other lossless image formats.
- **User-friendly Interface**: Command-line and GUI options available.

## Technologies Used
- Python
- OpenCV
- NumPy
- Cryptography Library (for encryption)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/pnavaneethreddy/Secure-Data-Hiding-in-Images-using-Steganography.git
   cd secure-steganography
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python requirements.txt
   ```

## Usage
### Hide a Message
```sh
python encrypt.py --hide --image input.png --message "Secret Message" --output output.png
```

### Extract a Message
```sh
python decrypt.py --extract --image output.png
```

## Security Considerations
- Use **lossless** image formats like PNG to prevent data loss.
- Encrypt messages before embedding for added security.
- Avoid using publicly shared images to reduce detection risk.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to the branch and create a pull request.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact
For questions or suggestions, open an issue or contact [your-email@example.com].

