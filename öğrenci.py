

class Ogrenci:
    def __init__(self, ad, soyad, numara, bolum):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.bolum = bolum

    def ekrana_bilgileri_goster(self):
        print("Öğrenci Bilgileri")
        print("Ad:", self.ad)
        print("Soyad:", self.soyad)
        print("Numara:", self.numara)
        print("Bölüm:", self.bolum)


ogrenci1 = Ogrenci("Hümeyra", "Çamkerten", 12345, "Yönetim Bilişim Sistemleri")

ogrenci1.ekrana_bilgileri_goster()
