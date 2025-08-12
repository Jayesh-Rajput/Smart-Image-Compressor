# Smart Image Compressor (Python + GUI)

A Python application to batch compress images using Pillow, featuring a Tkinter GUI with side-by-side preview for quality comparison.

---

## Features

- **Batch Compression:** Compress all images in a selected folder.
- **Custom Dimensions:** Resize images to a specified maximum width and height, maintaining aspect ratio.
- **Quality Control:** Adjust JPEG compression quality to balance file size and visual fidelity.
- **Format Selection:** Convert images to JPEG, PNG, or WebP, or retain their original format.
- **Side-by-Side Preview:** Compare the original and compressed versions of a sample image before running batch compression.
- **User-Friendly GUI:** Select folders and settings easily with the Tkinter graphical interface.

---

## Installation

1. **Clone the repository** (or download the project files):

    ```bash
    git clone <your-repo-url>
    cd Image-Compression
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. **Run the GUI application:**

    ```bash
    python gui.py
    ```

2. **How to use:**
    - Select the source folder containing images to compress.
    - Select the destination folder for saving compressed images.
    - Set maximum width, height, compression quality, and format.
    - Choose a sample image and click **Update Preview** to view original vs compressed images side-by-side.
    - If satisfied, click **Compress Images** to batch process all images in the source folder.

---

## Supported Formats

- Input: JPEG, PNG, WEBP
- Output: JPEG, PNG, WEBP

---

## Example

1. Original folder: `input_images/`
2. Destination folder: `compressed_images/`
3. Set width = 800, height = 800, quality = 90, format = JPEG
4. Preview with a sample image.
5. Run batch compression.

---

## License

MIT

---

## Contributing

Feel free to fork the repository and submit pull requests for improvements or new features!

---

## Credits

- [Pillow](https://python-pillow.org/) for image processing.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for GUI.
