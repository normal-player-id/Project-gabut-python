#!/data/data/com.termux/files/usr/bin/python
import random
import time
ikan_rendahan = ([
    "batu",
    "besi",
    "kayu",
    "durian laut"
])
ikan_biasa = ([
    "cupang",
    "bintang laut",
    "ikan badut nabung pty",
    "kepiting"
])
ikan_langka = ([
    "lumba lumba",
    "paus",
    "Orca!",
    "megaladon"
])
ikan_misterius = ([
    "IJN yamato",
    "belgorod",
    "B2A spirit",
    "USS misouri"
])
rod_db = ({
    1: {
        "nama" : "rod pemula",
        "lure" : 0,
        "luck" : 0,
        "speed" : 0,
        "max kg" : 50,
        "harga" : 0
    },
    2: {
        "nama" : "rod besi",
        "lure" : 0,
        "luck" : 50,
        "speed" : -10,
        "max kg" : 100000,
        "harga" : 10000
    },
    3: {
        "nama" : "speed rod",
        "lure" : 10,
        "luck" : 0,
        "speed" : 20,
        "max kg" : 1000,
        "harga" : 500
    }
    
})
input_ = ([
    "w",
    "a",
    "s",
    "d"
])
uang: int = 1000
tas = ([])
tas_rod = ([])
progres = 0
#rod stat
bonus_lure: int = 0
lure: float = 10.0
min_lure: float = 0.0
luck: int = 0
max_kg: int = 0
speed = 0
def sell(nama, berat):
    global uang

    for ikan in tas:
        if ikan["nama"] == nama and ikan["berat"] == berat:
            tas.remove(ikan)
            harga = ikan["berat"] * 10
            uang += harga
            print(f"ikan terjual dengan harga: {harga}")
            return
        print("ikan does exit")
def pilih_rod(nama):
    global bonus_lure, luck, max_kg, speed
    for rod in tas_rod:
        if rod["nama"] == nama:
            bonus_lure = rod["lure"]
            luck = rod["luck"]
            max_kg = rod["max kg"]
            speed = rod["speed"]
            print("rod telah di pakai")
            return
        print("rod does exit")
        
def shop():
    global uang
    print("semua rod yang aku jual dengan harga murah")
    print("dengan diskon yang sangat tinggi")
    print("diskon 0.0000000000001% sangat worit kan")
    print("semua rod")
    print(rod_db)
    print(f"uang mu : {uang}")
    jawab = input("pilih nama nya untuk beli ")
    id_beli = None
    for id_rod, rod in rod_db.items():
        if rod["nama"] == jawab:
            if uang >= rod["harga"]:
                uang -= rod["harga"]
                tas_rod.append(rod)
                id_beli = id_rod
                print(f"rod terjual dengan harga{rod["harga"]}")
            else:
                print("anda miskin")
    if id_beli is not None:
        del rod_db[id_beli]

print("mancinggg!!!!!")
print("enter buat lanjut")
while True:
    while True:
        print("pilih rod")
        print(tas_rod)
        print("pilih rod 1")
        print("beli rod = 5")
        jawab_ = int(input("??? "))
        if jawab_ == 1:
            jawab = input("nama ")
            pilih_rod(jawab)
            if max_kg > 0:
                break
            else:
                print("tolong pakai rod mu")
        elif jawab_ == 5:
            shop()
    jawab = input("lempar??? y/n  ")
    if jawab == "y":
        print("tunggu ikan")
    elif jawab == "n":
        break

    
    tunggu_ikan_lapar = lure - bonus_lure
    if tunggu_ikan_lapar < 0:
        tunggu_ikan_lapar = 0
    time.sleep(tunggu_ikan_lapar)
    kemungkinan = random.randint(1,100)
    if kemungkinan <= 5 and max_kg >=1000000:
        print("dapet military loot box")
        while True:
            speed_progres = 5 + speed
            print("enter dan wasd untuk tarik")
            gerak = random.choice(input_)
            print(f"gerak: {gerak}")
            player_input = input()
            if player_input == gerak:
                progres += speed_progres
                print(f"progres {progres}%")
            else:
                progres += -30 + speed
                print(f"progres {progres}%")
            if progres >= 100:
                dapet = random.choice(ikan_misterius)
                berat = random.randint(10000, 1000000)
                tas.append({
                    "nama": dapet,
                    "berat" : berat
                     })
                print(dapet)
                print("========")
                print("•[[[|>⟩•")
                print("========")
                print(f"berat ikan: {berat}kg")
                progres = 0
                break
            elif progres < 0:
                print("ikan lolos")
                progres = 0
                break
    elif kemungkinan <= 50 and max_kg >= 10000:
        print("dapet ikan langka")
        while True:
            speed_progres = 10 + speed
            print("enter dan wasd buat tarik")
            gerak = random.choice(input_)
            print(f"gerak: {gerak}")
            player_input = input()
            if player_input == gerak:
                progres += speed_progres
                print(f"progres {progres}%")
            else:
                progres += -5
                print(f"progres {progres}%")
            if progres >= 100:
                dapet = random.choice(ikan_langka)
                berat = random.randint(1000, 10000)
                tas.append({
                    "nama" : dapet,
                    "berat" : berat
                })
                print(dapet)
                print("========")
                print("><(((('>")
                print("========")
                print(f"berat ikan: {berat}kg")
                progres = 0
                break
            elif progres < 0:
                print("ikan lolos")
                progres = 0
                break
    elif kemungkinan <= 60 and max_kg >= 1000:
        print("dapet ikan biasa")
        while True:
            speed_progres = 30 + speed
            print("enter dan wasd buat tarik")
            gerak = random.choice(input_)
            print(f"gerak: {gerak}")
            player_input = input()
            if player_input == gerak:
                progres += speed_progres
                print(f"progres {progres}%")
            else:
                progres += -1
                print(f"progres {progres}%")
            if progres >= 100:
                dapet = random.choice(ikan_biasa)
                berat = random.randint(20, 1000)
                tas.append({
                    "nama" : dapet,
                    "berat" : berat
                })
                print(dapet)
                print("========")
                print("  ⟩><)>")
                print("========")
                print(f"berat ikan: {berat}kg")
                progres = 0
                break
            elif progres < 0:
                print("ikan lolos")
                print("noob amat")
                progres = 0
                break
    else:
        print("ikan pemula")
        while True:
            speed_progres = 50 + speed
            print("enter dan wasd buat tarik")
            gerak = random.choice(input_)
            print(f"gerak: {gerak}")
            player_input = input()
            if player_input == gerak:
                progres += speed_progres
                print(f"progres {progres}%")
            else:
                progres += -1
                print(f"progres {progres}%")
            if progres >= 100:
                dapet = random.choice(ikan_rendahan)
                berat = random.randint(1,50)
                tas.append({
                    "nama" : dapet,
                    "berat" : berat
                })
                print(dapet)
                print("========")
                print("  ><>")
                print("========")
                print(f"berat ikan: {berat}kg")
                progres = 0
                break
            elif progres < 0:
                print("ikan lolos")
                print("bot")
                progres = 0
                break
    print("0: stop")
    print("1: lanjut")
    print("2: inventory")
    jawab = int(input("mancing lagi?? "))
    if jawab == 0:
        break
    elif jawab == 1:
        print("mancing lagi")
    elif jawab == 2:
        while True:
            print("tas mu")
            print(tas)
            print(f"uang mu: {uang}")
            print("jual ikan?")
            print("jual ikan = 1")
            print("gak jual = 0")
            jawab = int(input("1 atau 0? "))
            if jawab == 1:
                nama = str(input("nama ikan: "))
                berat = int(input("berat ikan: "))
                sell(nama, berat)
            elif jawab == 0:
                print("ok")
                break
            else:
                print("bisa baca gak sih lo")
    else:
        print("input tidak ada")
