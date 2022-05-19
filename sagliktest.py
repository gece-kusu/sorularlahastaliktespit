BitkiCaylari = ["Rezene", "Isırgan Otu Çayı", "Papatya", "Melisa Çayı", "Nane Limon"]
AgriKesiciler = ["Aferin", "Betaserc", "Parol"]

AtesDerecesi = int(input("Ateşiniz kaç derece?: "))
Oksuruk = input("Öksürüğünüz var mı? E/H: ").lower()
BasAgrisi = input("Başınız ağrıyor mu? E/H: ").lower()

if (AtesDerecesi >= 39) and (Oksuruk == "e") and (BasAgrisi == "e"):
	print("Sen hastasın. Sana herhangi bir şey önermek yanlış olur. Hemen Doktora gitmeli!")

if (AtesDerecesi >= 39) and (Oksuruk == "e") and (BasAgrisi == "h"):
    print("Hem öksürüyorsun, hem de ateşin var. Doktora gider misiniz?")

if (AtesDerecesi >= 39) and (Oksuruk == "h") and (BasAgrisi == "e"):
    print("Başın ağrıyor ve ateşin var. Doktora gider misin?")

if (AtesDerecesi >= 39) and (Oksuruk == "h") and (BasAgrisi == "h"):
	print("Sadece ateşin var. Ateşini düşürmek için duş alabilirsin.")
	Oneri1 = input("Duş sonrası çay ister misin? E/H: ").lower()
	if Oneri1 == "e":
		print(BitkiCaylari)

#-----------------
if (AtesDerecesi < 39) and (Oksuruk == "e") and (BasAgrisi == "e"):
    print("Ateşin yok ama, hastalık belirtilerin var. Lütfen doktora git..!")

if (AtesDerecesi < 39) and (Oksuruk == "h") and (BasAgrisi == "e"):
    Oneri5 = input("Ateşn yok. Öksürüğün de yok. Baş ağrın için ağrı kesici ister misin? E/H: ").lower()
    if Oneri5 == "e":
    	print(AgriKesiciler)
    if Oneri5 == "h":
        print("O zaman bitki çayı içiniz lütfen...", BitkiCaylari, "Afiyet olsun.")

if (AtesDerecesi < 39) and (Oksuruk == "e") and (BasAgrisi == "h"):
	Oneri4 = input("Herhangi bir ateş veya baş ağrısı yok. Fakat, öksürüğün var. \n Boğazın için çay önerebilirim E/H: ")
	if Oneri4 == "e":
		print(BitkiCaylari, "Afiyet olsun.")
	if Oneri4 == "h":
		Uyari = input("Bak çok güzel çaylarım var. Emin misin? E/H: ").lower()
		if Uyari == "e":
			print("Peki o zaman, görüşürüz...")
		if Uyari == "h":
			print("O zaman gelsin çaylarrr \n", BitkiCaylari)

if (AtesDerecesi < 39) and (Oksuruk =="h") and (BasAgrisi == "h"):
    Oneri7 = input("Tebrikler! Sen hasta değilsin. Dilersen sana bitki çayı önerebilirim. E/H?: ").lower()
    if Oneri7 == "e":
        print(BitkiCaylari, "\nAfiyet olsun...")
    if Oneri7 == "h":
        print("Programı kullandığın için teşekkürler...")

#-----------------
