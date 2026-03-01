import os

DOSYA_ADI = "gorevler.txt"

def gorevleri_oku():
    gorevler = []
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            for satir in dosya:
                gorev = satir.strip()
                if gorev:
                    gorevler.append(gorev)
    except FileNotFoundError:
        print("Görev dosyası bulunamadı veya okunamadı. Yeni bir liste oluşturuldu.")
    return gorevler

def gorevleri_kaydet(gorevler):
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            for gorev in gorevler:
                dosya.write(gorev + "\n")
    except Exception as e:
        print(f"Hata: {e}")


def gorevleri_listele(gorevler):
    if not gorevler:
        print("\nHenüz görev eklenmemiş.\n")
    else:
        print("\n--- GÖREV LİSTESİ ---")
        for i, gorev in enumerate(gorevler, 1):
            print(f"{i}. {gorev}")
        print()

def yeni_gorev_ekle(gorevler):
    yeni_gorev = input("Yeni görevi girin: ").strip()
    if not yeni_gorev:
        print("Hata: Boş görev eklenemez.")
    else:
        gorevler.append(yeni_gorev)
        gorevleri_kaydet(gorevler)
        print("Görev başarıyla eklendi.\n")

def gorev_duzenle(gorevler):
    gorevleri_listele(gorevler)
    if not gorevler:
        return
    try:
        numara = int(input("Düzenlenecek görev numarasını girin: "))
        if 1 <= numara <= len(gorevler):
            yeni_metin = input("Yeni görev metnini girin: ").strip()
            if yeni_metin:
                gorevler[numara - 1] = yeni_metin
                gorevleri_kaydet(gorevler)
                print("Görev güncellendi.\n")
            else:
                print("Boş görev girilemez.")
        else:
            print("Geçersiz görev numarası.\n")
    except ValueError:
        print("Lütfen sayı giriniz.")

def gorev_sil(gorevler):
    gorevleri_listele(gorevler)
    if not gorevler:
        return
    try:
        numara = int(input("Silinecek görev numarasını girin: "))
        if 1 <= numara <= len(gorevler):
            silinen = gorevler.pop(numara - 1)
            gorevleri_kaydet(gorevler)
            print(f"'{silinen}' silindi.\n")
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen sayı giriniz.")



def ana_menu():
    gorevler = gorevleri_oku()
    print("To-Do List Uygulamasına Hoş Geldiniz!\n")

    while True:
        print("--- TO-DO LIST UYGULAMASI ---")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görev Düzenle")
        print("4. Görev Sil")
        print("5. Çıkış")
        secim = input("Seçiminiz (1-5): ").strip()

        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            yeni_gorev_ekle(gorevler)
        elif secim == "3":
            gorev_duzenle(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
        elif secim == "5":
            print("Programdan çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-5 arasında bir sayı girin.\n")