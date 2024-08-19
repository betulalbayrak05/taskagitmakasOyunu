def tas_kagit_makas_betul_albayrak():
    giris = (
        """Dünyanın en ünlü oyunlarından birini oynuyoruz! Taş, kağıt ve makas! 3 tur oynayacağız ve toplam 2 turu kazanan
oyunu kazanmış olacak. Oynamak için taş, kağıt, makas girin veya oynamak istemiyorsanız 'çıkış' yazın. 
Oyun ŞİMDİ başlıyor!"""
    )
    print(giris)

    secenekler = ['taş', 'kağıt', 'makas']
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0

    i = 1
    while i <= 3:
        oyuncu_skoru = 0
        bilgisayar_skoru = 0
        j = 1
        while True:
            print(f"*** GAME{i} ROUND{j} ***")
            kullanici_secim = input("Taş, kağıt, makas ya da çıkış? :").lower()

            if kullanici_secim == 'çıkış':
                print("Oyundan çıktınız.")
                exit()
            import random
            if kullanici_secim not in secenekler:
                print("Geçersiz seçim. Tekrar deneyin.")
                continue

            seçenekler = ['taş', 'kağıt', 'makas']
            rastgele_secim = random.choice(secenekler)
            print("Bilgisayarın Seçimi: " + rastgele_secim)

            if kullanici_secim == rastgele_secim:
                print("Bu tur berabere..")
            elif kullanici_secim == 'taş' and rastgele_secim == 'makas':
                print("Kazandınız :)")
                oyuncu_skoru = oyuncu_skoru + 1
            elif kullanici_secim == 'kağıt' and rastgele_secim == 'taş':
                print("Tebrikler :)")
                oyuncu_skoru = oyuncu_skoru + 1
            elif kullanici_secim == 'makas' and rastgele_secim == 'kağıt':
                print("Şanslısın ;)")
                oyuncu_skoru = oyuncu_skoru + 1
            else:
                print("Kaybettiniz :(")
                bilgisayar_skoru = bilgisayar_skoru + 1

            print(f"OYUNCU: {oyuncu_skoru} BİLGİSAYAR: {bilgisayar_skoru}")

            j += 1
            print("********************************************")

            if oyuncu_skoru == 2:
              print("Tebrikler bu oyunu kazandınız!")
              oyuncu_galibiyetleri += 1
              break
            elif bilgisayar_skoru == 2:
              print("Kaybettiniz, bu oyunu bilgisayar kazandı.")
              bilgisayar_galibiyetleri += 1
              break
        i += 1
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"Genel Skor "
          f" Oyuncu: {oyuncu_galibiyetleri} Bilgisayar: {bilgisayar_galibiyetleri}")

tas_kagit_makas_betul_albayrak()



