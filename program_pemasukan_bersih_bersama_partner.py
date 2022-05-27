def validasi_persen_hasil(hasil):
	if(hasil > 100):
		print("Jumlah persen yang di input melebihi 100%")
		exit()
	elif(hasil < 0):
		print("Jumlah persen yang di input kurang dari 0%")
		exit()

def validasi_total_persen_hasil(hasil_anda, hasil_partner):
	total_hasil = hasil_anda + hasil_partner
	if(total_hasil != 100):
		print("Total persen bersama partner anda tidak 100%")
		exit()

print("PROGRAM MENDAPATKAN PEMASUKAN BERSIH BERSAMA PARTNER KERJA")
print()

try:
	anda = int(input("Masukan jumlah % hasil anda "))
	validasi_persen_hasil(anda)

	partner = int(input("Masukan jumlah % hasil partner anda "))
	validasi_persen_hasil(partner)

	validasi_total_persen_hasil(anda, partner)

	pemasukan = int(input("Masukan pemasukan bersih dari bisnis bersama partner anda "))
	hasil_anda = pemasukan * (anda / 100)
	hasil_partner_anda = pemasukan * (partner / 100)
	print('Hasil pemasukan bersih anda: {:.3f}'.format(hasil_anda).rstrip("0"))
	print('Hasil pemasukan bersih partner anda: {:.3f}'.format(hasil_partner_anda).rstrip("0"))
except ValueError:
	print("Yang anda inputkan bukan angka!")
