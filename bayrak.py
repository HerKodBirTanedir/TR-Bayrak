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

def draw_flag():
    # Yeni bir figür (pencere) ve eksen (çizim alanı) oluştur
    fig, ax = plt.subplots()
    ax.set_aspect('equal') # Oranları koru
    ax.set_xlim(0, L)      # X ekseni limitleri
    ax.set_ylim(0, G)      # Y ekseni limitleri
    ax.axis('off')         # Eksenleri gizle, sadece bayrak görünsün

    # Kırmızı zemin
    ax.add_patch(patches.Rectangle((0, 0), L, G, color='#E30A17'))

    # Hilal 
    outer_center = (M + A, G/2)
    outer_r = B / 2
    inner_center = (outer_center[0] + C, G/2)
    inner_r = D / 2

    # Beyaz dış daireyi çiz
    ax.add_patch(patches.Circle(outer_center, outer_r, color='white'))

    # Kırmızı iç daireyi çizerek hilal şeklini oluştur
    ax.add_patch(patches.Circle(inner_center, inner_r, color='#E30A17'))

    # Yıldız konumu ve çizimi
    star_center = (inner_center[0] + E + F / 6, G / 2)
    star_rotation_angle = -40  # Yıldızı sola doğru -40 derece çevir
    star = draw_star(star_center[0], star_center[1], F / 2, star_rotation_angle)
    ax.add_patch(star) # Yıldızı ekrana ekle 

    # Çizimi göster
    plt.show()

# draw_flag fonksiyonunu çalıştır
draw_flag()