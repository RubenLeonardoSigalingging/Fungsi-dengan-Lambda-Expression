#!/usr/bin/env python3


# Python Lambda
def Python_Lambda(VarX,Created_By="Ruben Leonardo Sigalingging"):
	return VarX
Python_Lambda=lambda VarY:VarY+9
print(Python_Lambda(8))


def Lambda(VarA,VarB,Created_By="Ruben Leonardo Sigalingging"):
	return VarA,VarB
Hasil=lambda VarA,VarB:VarA*VarB+3
print(f"Hasil Penjumlahan VarA + VarB: {Hasil(5,25)}")


Anonymous_Function=lambda Nama_Saya:Nama_Saya
Angka_Favorit=lambda Angka:Angka+5
Angka_Favorit_Saya=Angka_Favorit
print(Anonymous_Function("Ruben Leonardo Sigalingging"))
print(f"Angka Favorit Saya: {Angka_Favorit(4)}")


# Mencari Luas Segitiga, Menggunakan Anonymous Function di Python.
# Rumus Luas Segitiga: 1/2 * A * T
def Luas_Segitiga(alas_segitiga,tinggi_segitiga,Created_By="Ruben Leonardo Sigalingging"):
	return alas_segitiga,tinggi_segitiga
Hasil_Luas_Segitiga=lambda alas_segitiga,tinggi_segitiga:1/2*alas_segitiga*tinggi_segitiga
print(f"Hasil Luas Segitiga: {Hasil_Luas_Segitiga(15,10)}")