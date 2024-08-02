'''
SUMBER: https://hellosehat.com/health-tools/kebutuhan-kalori/
Menggunakan Paradigma Prosedural
Didukung: ChatGPT 🤖
'''

import os
from time import sleep
# from basal_metabolic_rate.banner import banner
# from basal_metabolic_rate.bmr_calculator import pria, wanita
# from basal_metabolic_rate.calorie_needs import aktivitas_fisik_pria, aktivitas_fisik_wanita
# from basal_metabolic_rate.physical_activity.man import female_level_1,female_level_2,female_level_3
# from basal_metabolic_rate.physical_activity.woman import female_level_1,female_level_2,female_level_3
import basal_metabolic_rate
import basal_metabolic_rate.physical_activity

os.system("cls")

def main():
  while True:
    basal_metabolic_rate.banner()

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
      hasil_bmr_pria = basal_metabolic_rate.pria(tinggi_badan=tinggi_badan, berat_badan=berat_badan, usia=usia)
      
      basal_metabolic_rate.aktivitas_fisik_pria()
      tingkat_aktivitas_fisik = int(input("Pilih tingkat intensitas aktivitas fisik Anda : "))
      
      if tingkat_aktivitas_fisik == 1:
        basal_metabolic_rate.physical_activity.male_level_1(hasil_bmr_pria=hasil_bmr_pria)
        continue
      elif tingkat_aktivitas_fisik == 2:
        basal_metabolic_rate.physical_activity.male_level_2(hasil_bmr_pria=hasil_bmr_pria)
        continue
      elif tingkat_aktivitas_fisik == 3:
        basal_metabolic_rate.physical_activity.male_level_3(hasil_bmr_pria=hasil_bmr_pria)
        continue
        
    elif jenis_kelamin == "P":
      tinggi_badan = int(input("Berapa tinggi Anda? (cm) : "))
      berat_badan = int(input("Berapa berat badan Anda? (kg) : "))
      hasil_bmr_wanita = basal_metabolic_rate.wanita(tinggi_badan=tinggi_badan, berat_badan=berat_badan, usia=usia)
      
      basal_metabolic_rate.aktivitas_fisik_wanita()
      tingkat_aktivitas_fisik = int(input("Pilih tingkat intensitas aktivitas fisik Anda : "))
      
      if tingkat_aktivitas_fisik == 1:
        basal_metabolic_rate.physical_activity.female_level_1(hasil_bmr_wanita=hasil_bmr_wanita)
        continue
      elif tingkat_aktivitas_fisik == 2:
        basal_metabolic_rate.physical_activity.female_level_2(hasil_bmr_wanita=hasil_bmr_wanita)
        continue
      elif tingkat_aktivitas_fisik == 3:
        basal_metabolic_rate.physical_activity.female_level_3(hasil_bmr_wanita=hasil_bmr_wanita)
        continue
      
    else:
      print("")
      print(f"Input yang anda Masukan Salah, Silahkan input ulang")
      sleep(7)
      os.system("cls")
      continue
      
if __name__ == "__main__":
  main()