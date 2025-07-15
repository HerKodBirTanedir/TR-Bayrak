import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Bayrak oranları (Genişlik = G)
G = 1.0
A = 0.5 * G         # Ay dış merkezinin kaçak kenar uzaklığı
B = 0.5 * G         # Ay dış dairesinin çapı
C = 0.0625 * G      # Ay iç ve dış merkezler arası
D = 0.4 * G         # Ay iç dairesinin çapı
E = (1/3) * G       # Yıldız dairesinin ay iç dairesinden uzaklığı
F = 0.25 * G        # Yıldız dairesinin çapı
L = 1.5 * G         # Bayrağın boyu (uzunluk)
M = (1/30) * G      # kaçak kenar genişliği

def draw_star(center_x, center_y, radius, rotation_angle=0):
    coords = []
    for i in range(10):
        # Her bir köşe ve iç nokta için açı hesapla
        angle = np.deg2rad(90 + i * 36 + rotation_angle) 

        # Dış ve iç noktalar için farklı yarıçaplar
        r = radius if i % 2 == 0 else radius * np.sin(np.deg2rad(18)) / np.sin(np.deg2rad(126))

        # Koordinatları hesapla
        coords.append((center_x + r * np.cos(angle), center_y + r * np.sin(angle)))

    # Hesaplanan koordinatlarla bir yıldız oluştur
    return patches.Polygon(coords, closed=True, color='white')