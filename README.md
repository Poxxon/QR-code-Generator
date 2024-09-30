# QR Code Generator

This Python script generates a QR code for a given URL using the `qrcode` library. The QR code is saved as an image file in the current directory.

## Features
- Generates a QR code for a specified URL.
- Allows customization of the output filename.
- Saves the QR code image in PNG format.

## Upcoming features (TBD):
- Allowing user to input a URL through CLI or GUI rather than modifying parts of the code
- Allowing to download through browser to your downloads directory rather than the source code directory

## Prerequisites

To use this script, you must have Python installed on your machine. Additionally, the script requires the `qrcode` library, which can be installed using pip.

### Installing the required library

```bash
pip install qrcode[pil]
```

### How to use
- Clone or download the script.
- Ensure you have the required library installed (see Prerequisites).
- Modify the url variable in the script to the URL you want to generate a QR code for. By default, the script points to Pouya's GitHub account.
- Optionally, change the filename parameter to save the QR code image with a different name.
- Run the script:
  python main.py

#### To customize your own URL change this:
```python
url = "https://github.com/Poxxon"
