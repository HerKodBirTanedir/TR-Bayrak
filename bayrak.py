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