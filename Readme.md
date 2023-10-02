# Convert images to PDF

## How to use

```commandline
Script to convert images to pdf

HOW TO USE:

    convert_img_to_pdf image.png
    convert_img_to_pdf .
    convert_img_to_pdf /home/user/Pictures 
```

## Dependence

- Pillow

## Install

To install in `$HOME/.local/bin` with name convert_img_to_pdf
```commandline
wget -c https://raw.githubusercontent.com/jalmx/img-to-pdf/master/src/convert_img_to_pdf.py -O $HOME/.local/bin/convert_img_to_pdf

sudo chmod +x $HOME/.local/bin/convert_img_to_pdf
```

### Install dependence

First step create a venv and then install dependence

```commandline
pip install Pillow
```

Or

```commandline
pip install -r requirements.txt
```
