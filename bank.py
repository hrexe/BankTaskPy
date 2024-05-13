class Hesab:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = int(balans)  
        print("Yeni hesab yaradıldı. Hesab nömrəsi:", self.hesab_nomresi, "Balans:", self.balans)

    def balansi_artir(self, mebleg):
        self.balans += int(mebleg)  
        print("Balans artırıldı. Yeni balans:", self.balans)

    def pul_cixar(self, mebleg):
        mebleg = int(mebleg)
        if mebleg <= self.balans:
            self.balans -= mebleg
            print("Pul çıxarıldı. Yeni balans:", self.balans)
        else:
            print("Balansınızda kifayət qədər pul yoxdur.")

    def balansi_goster(self):
        print("Hesab nömrəsi:", self.hesab_nomresi)
        print("Balans:", self.balans)


class Kredit(Hesab):
    def __init__(self, hesab_nomresi, balans, kredit_mebli):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meblegi = int(kredit_mebli)  

    def kredit_ver(self):
        self.balans += self.kredit_meblegi
        print("Kredit hesabınıza əlavə olundu. Yeni balans:", self.balans)

    def kredit_odenişi(self):
        ayliq_odenis = self.kredit_meblegi / 12
        self.balans -= int(ayliq_odenis) 
        print("Kredit ödənişi yerinə yetirildi. Yeni balans:", self.balans)


hesab = Hesab(123456, 1000)
hesab.balansi_artir(500) 
hesab.pul_cixar(200)
hesab.balansi_goster()

kredit_hesabi = Kredit(7891011, 2000, 10000)
kredit_hesabi.kredit_ver()
kredit_hesabi.kredit_odenişi()
kredit_hesabi.balansi_goster()
