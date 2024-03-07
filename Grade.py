nilai = int(input("Masukkan nilai Anda: "))

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 60:
    grade = "C"
else:
    grade = "D"
    
print("Grade nilai Anda: " + grade)
