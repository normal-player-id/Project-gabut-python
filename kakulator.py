angka_pertama = 0
angka_kedua = 0

while True:
    angka_pertama = int(input("angka pertama:" ))
    penjumlahan = str(input("penjumlahan?" ))
    angka_kedua = int(input("angka ke dua:" ))
    if penjumlahan == "+":
        print("jawqban:%d" % (angka_pertama + angka_kedua))
    elif penjumlahan == "-":
        print("jawaban:%d" % (angka_pertama - angka_kedua))
    elif penjumlahan == "×":
        print("jawaban:%d" % (angka_pertama * angka_kedua))
    elif penjumlahan == "÷":
        print("jawaban:%d" % (angka_pertama / angka_kedua))
    else:
        print("ber otak senku")
    print("0 untuk stop")
    print("1 untuk lanjut")
    lanjut = int(input("??:" ))
    if lanjut == 0:
        break
    else:
        print("ok")
