#!/bin/bash

# Instalasi dependensi
pip install -r requirements.txt

# Salin file .env.example menjadi .env jika belum ada
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "File .env telah dibuat. Mohon isi dengan nilai yang sesuai."
else
    echo "File .env sudah ada."
fi

echo "Setup selesai. Silakan jalankan main.py untuk memulai bot."
