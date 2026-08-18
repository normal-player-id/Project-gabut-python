import time
jam = 0
menit = 0
detik = 0
print("run untuk run jam")
print("edit untuk edit jam")
def set_jam(set):
    global jam
    if set > 25 and set < 0:
        print("isi yang bener lah")
    else:
        jam = set
def set_menit(set):
    global menit
    if set > 60 and set < 0:
        print("isi yang bener lah")
    else:
        menit = set
def set_detik(set):
    global detik
    if set > 60 and set < 0:
        print("isi yang bener lah")
    else:
        detik = set
def run_jam():
    global detik
    global menit
    global jam
    while True:
        if detik >= 60:
            detik = 0
            menit += 1
        if menit >= 60:
            menit = 0
            jam += 1
        if jam >= 24:
            jam = 0
        detik += 1
        print(f"{jam} : {menit} : {detik}")
        time.sleep(1)
while True:
    seting = input()
    if seting == "run":
        run_jam()
        break
    if seting == "edit":
        print("====[EDIT]====")
        print("set jam")
        print("set menit")
        print("set detik")
        jawab = input()
        if jawab == "set jam":
            jawab = int(input("jam: "))
            set_jam(jawab)
        elif jawab == "set menit":
            jawab = int(input("menit: "))
            set_menit(jawab)
        elif jawab == "set_detik":
            jawab = int(input("menit: "))
            set_detik(jawab)
            
