
import tkinter as tk

#parent
class Konum:
    def __init__(self, sehir):
        self.sehir = sehir

    def konum_bilgisi(self):
        return f"Konum: {self.sehir}"

#child - HavaDurumu Konum'dan kalıtım alıyo
class HavaDurumu(Konum):
    def __init__(self, sehir, sicaklik, durum, nem, ruzgar):
        super().__init__(sehir)
        self.sicaklik = sicaklik
        self.durum = durum
        self.nem = nem
        self.ruzgar = ruzgar

    def bilgileri_goster(self):
        return (
            f"{self.konum_bilgisi()}\n"
            f"Sıcaklık: {self.sicaklik}°C\n"
            f"Durum: {self.durum}\n"
            f"Nem: %{self.nem}\n"
            f"Rüzgar: {self.ruzgar} km/h\n"
        )

#GUI
class HavaDurumuUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Hava Durumu Uygulaması (OOP)")

        # Nesne listesi
        self.veriler = {
            "Ankara": HavaDurumu("Ankara", 24, "Parçalı Bulutlu", 40, 15),
            "İstanbul": HavaDurumu("İstanbul", 21, "Yağmurlu", 60, 20),
            "İzmir": HavaDurumu("İzmir", 28, "Güneşli", 30, 10),
            "Antalya": HavaDurumu("Antalya", 31, "Açık", 25, 8),
            "Trabzon": HavaDurumu("Trabzon", 19, "Kapalı", 70, 12)
        }

        # Arayüz bileşenleri
        self.sehir_var = tk.StringVar(value="Ankara")
        tk.Label(root, text="Şehir Seçin:", font=("Arial", 12)).pack(pady=5)
        self.dropdown = tk.OptionMenu(root, self.sehir_var, *self.veriler.keys())
        self.dropdown.pack()

        self.goster_btn = tk.Button(root, text="Hava Durumunu Göster", command=self.goster)
        self.goster_btn.pack(pady=10)

        self.text_output = tk.Text(root, height=7, width=45, font=("Courier", 10))
        self.text_output.pack(pady=5)

        self.istatistik_btn = tk.Button(root, text="Genel İstatistikleri Göster", command=self.istatistik_goster)
        self.istatistik_btn.pack(pady=10)

    def goster(self):
        sehir = self.sehir_var.get()
        bilgi = self.veriler[sehir].bilgileri_goster()
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, bilgi)

    def istatistik_goster(self):
        sicakliklar = [v.sicaklik for v in self.veriler.values()]
        ortalama = sum(sicakliklar) / len(sicakliklar)
        en_sicak = max(self.veriler.values(), key=lambda x: x.sicaklik)
        en_serin = min(self.veriler.values(), key=lambda x: x.sicaklik)

        sonuc = (
            f"📊 Genel İstatistikler:\n"
            f"Ortalama Sıcaklık: {ortalama:.1f}°C\n"
            f"En Sıcak Şehir: {en_sicak.sehir} ({en_sicak.sicaklik}°C)\n"
            f"En Serin Şehir: {en_serin.sehir} ({en_serin.sicaklik}°C)\n"
        )
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, sonuc)

if __name__ == "__main__":
    root = tk.Tk()
    app = HavaDurumuUygulamasi(root)
    root.mainloop()
