def pria(berat_badan, tinggi_badan, usia):
  """Menghitung BMR Pria"""
  bmr_pria = 66.5 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia)
  return bmr_pria

def wanita(berat_badan, tinggi_badan, usia):
  """Menghitung BMR Wanita"""
  bmr_wanita = 655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia)
  return bmr_wanita