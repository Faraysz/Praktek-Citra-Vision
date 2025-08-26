import cv2
import numpy as np

# Ganti 'image.jpg' dengan nama file gambar yang ingin dideteksi
gambar_path = 'image.jpg'
img = cv2.imread(gambar_path)
if img is None:
    print(f'Gambar tidak ditemukan: {gambar_path}')
    exit()

# Deteksi tepi dengan Canny
tepi = cv2.Canny(img, 100, 200)

# Tampilkan hasil
title = 'Hasil Deteksi Tepi'
cv2.imshow(title, tepi)
cv2.waitKey(0)
cv2.destroyAllWindows()
