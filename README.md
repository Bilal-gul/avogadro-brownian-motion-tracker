# 🔬 Otonom Brownian Motion Analiz Motoru & Avogadro Hesabı

Bu proje, mikroskobik ortamdaki polen tanelerinin kaotik hareketlerini (Brownian Motion) yapay görme algoritmalarıyla otonom olarak takip etmek ve Einstein-Stokes difüzyon teorisi üzerinden **Avogadro Sabitini** hesaplamak amacıyla geliştirilmiştir.

## 🚀 Öne Çıkan Mühendislik Çözümleri

* **Yapışık Nesne Segmentasyonu:** Polenlerin temas anında birbirine karışmasını engellemek amacıyla `cv2.distanceTransform` tabanlı çekirdek izolasyonu uygulanmıştır.
* **Dinamik Hafıza ve Takip:** `cv2.moments` ile anlık ağırlık merkezleri hesaplanmış ve Öklid mesafesi üzerinden dinamik ID eşleştirmesi yapılmıştır.
* **Fiziksel Kalibrasyon:** Piksel dünyası ile makroskopik fizik dünyası (`PIXEL_TO_METER`) kalibre edilerek ham veri saf fiziksel veriye dönüştürülmüştür.

## 📊 Zafer Raporu (Başarı Metrikleri)

8.999 adet anlık hareket verisi işlenerek elde edilen sonuçlar:

| Parametre | Değer / Sonuç |
| :--- | :--- |
| **Hesaplanan Avogadro Sabiti** | **6.0083e+23** |
| **Teorik Gerçek Değer** | **6.022e+23** |
| **Teorik Değerden Sapma Oranı** | **%0.23** |

## 🛠️ Kullanılan Teknolojiler
* Python 3
* OpenCV (Yapay Görme)
* NumPy (Vektörel Matematik)

## 📌 Teşekkür / Atıf (Acknowledgment)
Bu projede test verisi olarak kullanılan mikroskobik polen videosu, eğitim ve araştırma amacıyla YouTube üzerindeki orijinal kaynağından referans alınmıştır. Akademik dürüstlük gereği kaynak gösterilerek depoya dahil edilmiştir.
