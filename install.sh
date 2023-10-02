#!/usr/bin/env bash

echo "Verify your PATH exist added `$HOME/.local/bin/`"

sudo chmod +x ./src/convert_img_to_pdf.py
cp ./src/convert_img_to_pdf.py $HOME/.local/bin/convert_img_to_pdf

echo "copy to $HOME/.local/bin/convert_img_to_pdf"
