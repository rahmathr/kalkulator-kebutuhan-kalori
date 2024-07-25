'''
References: https://hellosehat.com/health-tools/kebutuhan-kalori/
Didukung: ChatGPT✨

Menggunakan Paradigma Procedural✨
'''

import os
from time import sleep

os.system("cls")

def pria(berat_badan, tinggi_badan, usia):
  bmr_pria = 66.5 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia)
  return bmr_pria

def wanita(berat_badan, tinggi_badan, usia):
  bmr_wanita = 655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia)
  return bmr_wanita

def main():
  while True:
    print("="*28)
    print("KALKULATOR KKEBUTUHAN KALORI")
    print("="*28)
    usia = int(input("Usia anda : "))
    jenis_kelamin = str(input("Apa jenis kelamin Anda? (L/P) : "))
    
    
    if jenis_kelamin == "l" or jenis_kelamin == "p":
      print("")
      print("Tolong Gunakan Huruf Besar 🔠, Ulangi kembali!")
      sleep(2)
      os.system("cls")
      continue
    
    
    elif jenis_kelamin == "L":
      tinggi_badan = int(input("Berapa tinggi Anda? (cm) : "))
      berat_badan = int(input("Berapa berat badan Anda? (kg) : "))
      hasil_bmr_pria = pria(tinggi_badan=tinggi_badan, berat_badan=berat_badan, usia=usia)
      
      print("")
      print("=============================")
      print("KEBUTUHAN KALORI DALAM SEHARI")
      print("=============================")
      print("1. Hampir tidak pernah berolahraga")
      print("2. Jarang berolahraga")
      print("3. Sering berolahraga atau beraktivitas fisik berat")
      print("")
      tingkat_aktivitas_fisik = int(input("Pilih tingkat intensitas aktivitas fisik Anda : "))
      
      if tingkat_aktivitas_fisik == 1:
        hasil_tingkat_aktivitas_fisik = hasil_bmr_pria * 1.2
        print("")
        print(f"Berarti BMR-nya sebesar {hasil_bmr_pria:.0f} kkal, sedangkan kebutuhan kalorinya sebesar {hasil_tingkat_aktivitas_fisik:.0f} kkal")
        sleep(7)
        os.system("cls")
        continue
      
      elif tingkat_aktivitas_fisik == 2:
        hasil_tingkat_aktivitas_fisik = hasil_bmr_pria * 1.3
        print("")
        print(f"Berarti BMR-nya sebesar {hasil_bmr_pria:.0f} kkal, sedangkan kebutuhan kalorinya sebesar {hasil_tingkat_aktivitas_fisik:.0f} kkal")
        sleep(7)
        os.system("cls")
        continue
      
      elif tingkat_aktivitas_fisik == 3:
        hasil_tingkat_aktivitas_fisik = hasil_bmr_pria * 1.4
        print("")
        print(f"Berarti BMR-nya sebesar {hasil_bmr_pria:.0f} kkal, sedangkan kebutuhan kalorinya sebesar {hasil_tingkat_aktivitas_fisik:.0f} kkal")
        sleep(7)
        os.system("cls")
        continue
        
    elif jenis_kelamin == "P":
      tinggi_badan = int(input("Berapa tinggi Anda? (cm) : "))
      berat_badan = int(input("Berapa berat badan Anda? (kg) : "))
      hasil_bmr_wanita = wanita(tinggi_badan=tinggi_badan, berat_badan=berat_badan, usia=usia)
      print("")
      print("=============================")
      print("KEBUTUHAN KALORI DALAM SEHARI")
      print("=============================")
      print("1. Hampir tidak pernah berolahraga")
      print("2. Jarang berolahraga")
      print("3. Sering berolahraga atau beraktivitas fisik berat")
      print("")
      tingkat_aktivitas_fisik = int(input("Pilih tingkat intensitas aktivitas fisik Anda : "))
      
      if tingkat_aktivitas_fisik == 1:
        hasil_tingkat_aktivitas_fisik = hasil_bmr_wanita * 1.2
        print("")
        print(f"Berarti BMR-nya sebesar {hasil_bmr_wanita:.0f} kkal, sedangkan kebutuhan kalorinya sebesar {hasil_tingkat_aktivitas_fisik:.0f} kkal")
        sleep(7)
        os.system("cls")
        continue
      
      elif tingkat_aktivitas_fisik == 2:
        hasil_tingkat_aktivitas_fisik = hasil_bmr_wanita * 1.3
        print("")
        print(f"Berarti BMR-nya sebesar {hasil_bmr_wanita:.0f} kkal, sedangkan kebutuhan kalorinya sebesar {hasil_tingkat_aktivitas_fisik:.0f} kkal")
        sleep(7)
        os.system("cls")
        continue
      
      elif tingkat_aktivitas_fisik == 3:
        hasil_tingkat_aktivitas_fisik = hasil_bmr_wanita * 1.4
        print("")
        print(f"Berarti BMR-nya sebesar {hasil_bmr_wanita:.0f} kkal, sedangkan kebutuhan kalorinya sebesar {hasil_tingkat_aktivitas_fisik:.0f} kkal")
        sleep(7)
        os.system("cls")
        continue
      
      print("")
      print(f"BMR anda sebesar {hasil_bmr_wanita:.0f} kkal")
      sleep(7)
      os.system("cls")
      continue
      
    else:
      print("")
      print("Input salah, silahkan masukkan input yang valid.")
      sleep(2)
      os.system("cls")
      continue
    
if __name__ == "__main__":
  main()