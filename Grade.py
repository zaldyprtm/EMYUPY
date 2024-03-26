def get_grade(s1: int, s2: int, s3: int) -> str:
    # Menghitung rata-rata dari tiga skor
    average_score = (s1 + s2 + s3) / 3
    
    # Menentukan huruf nilai berdasarkan skor rata-rata
    if 90 <= average_score <= 100:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'

# Contoh penggunaan
score1 = 85
score2 = 92
score3 = 78

# Mendapatkan huruf nilai dari rata-rata skor
grade = get_grade(score1, score2, score3)
print(f"Nilai huruf: {grade}")  # Output: B
