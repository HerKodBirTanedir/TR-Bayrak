![Türk Bayrağı](resim/bayrak.png)

# Python İle Türk Bayrağı Çizimi

Python programlama dili ve matplotlib kütüphanesini kullanarak Türk bayrağı çizeceğiniz bir projedir. 
Bu proje, hem görsel programlama becerilerinizi geliştirmek hem de bayrağımızın sembolik öğelerini kodla hayata geçirmek için harika bir örnektir.

## 1.Adım: Gerekli Kurulumlar Yapmak
İlk olarak, proje klasörünü(bayrak) oluşturalım,  VSCode açalım ve venv sanal ortamını kuralım. 'sanalortam' yerine farklı bir isim de verebilirsiniz.

`py -m venv sanalortam`

`cd .\sanalortam\` 

`cd .\Scripts\`  

`.\activate.bat`   'sanal ortamı çalıştıralım' 

Sanal ortamı geçiş yapınca terminalimizin görünümü aşağıdaki gibi olmalı yani sanal ortam yazısı görünmeli. 
Not: VSCode da, powershell terminalinde sorun çıkabilir. VSCode cmd terminalini deneyebilirsiniz.   

(sanalortam) C:\Users\Desktop\bayrak>

Sonrasında matplotlib,numpy kütüphanesini kuralım. matplotlib kurulumu sırasında numpy kuracaktır. matplotlib kurulumundan sonra
'pip list' çalıştırarak kontrol ediniz numpy kurulumunu.

`pip install matplotlib`
`pip install numpy`



Sonrasında bayrak.py dosyamızı oluşturalım ve  projemiz için gerekli olan kütüphaneleri içe aktaralım.

`import matplotlib.pyplot as plt` 'Bu kütüphane, Python'da grafikler ve çizimler oluşturmak için temel bir araçtır. plt olarak takma ad kullanacağız.'

`import matplotlib.patches as patches` 'Bu kütüphane, dikdörtgenler, daireler ve çokgenler gibi temel şekilleri çizmek için gereken sınıfları içerir. Bayrağımızın farklı kısımlarını çizmek için kullanacağız.'

`import numpy as np` 'Sayısal işlemler için kullanılan bu kütüphanedir, yıldızın koordinatlarını hesaplarken trigonometrik fonksiyonlardan yararlanmamızı sağlayacaktır.'

## 2.Adım: Türk Bayrağı Oranlarını Tanımlama

```
#Bayrak oranları (Genişlik = G)'
G = 1.0
A = 0.5 * G         # Ay dış merkezinin kaçak kenar uzaklığı
B = 0.5 * G         # Ay dış dairesinin çapı
C = 0.0625 * G      # Ay iç ve dış merkezler arası
D = 0.4 * G         # Ay iç dairesinin çapı
E = (1/3) * G       # Yıldız dairesinin ay iç dairesinden uzaklığı
F = 0.25 * G        # Yıldız dairesinin çapı
L = 1.5 * G         # Bayrağın boyu (uzunluk)
M = (1/30) * G      # kaçak kenar genişliği
```

## 3.Adım: Yıldız Çizme Fonksiyonu: draw_star
```
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
```

## 4.Adım: Türk Bayrağını Çizme Fonksiyonu: draw_flag
```
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


draw_flag() # draw_flag fonksiyonunu çalıştır
```

## Video Ders için
[Türk Bayrağı Çizim Dersi](https://youtu.be/lJ0ub-MIps4)
