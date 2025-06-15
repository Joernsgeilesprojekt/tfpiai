#!/bin/bash

echo "[+] Installing system dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip git ffmpeg libopenblas-dev libopenmpi-dev libomp-dev

echo "[+] Cloning latest version from GitHub..."
rm -rf BrainrotPi
git clone https://github.com/DEIN_USER/BrainrotPi.git
cd BrainrotPi

echo "[+] Installing Python requirements..."
pip3 install -r requirements.txt

echo "[+] Installing autostart service..."
sudo cp brainrot.service /etc/systemd/system/
sudo systemctl enable brainrot.service
sudo systemctl start brainrot.service

echo "[✓] Installation complete."
