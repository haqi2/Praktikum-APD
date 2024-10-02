username = "Haqi"
password = 81
upayalogin = 0
maksimallogin = 3

while upayalogin < maksimallogin:
    usn = input("Masukkan username: ")
    pw = input("Masukkan password: ")
    
    if username == usn and int(pw) == password:
        print("Login berhasil")
        beratbadan = float(input("Masukkan berat badan (kg): "))
        tinggibadan = float(input("Masukkan tinggi badan (cm): "))
        tinggimeter = tinggibadan / 100
        bmi = beratbadan / (tinggimeter * tinggimeter)
        
        if bmi < 18.5:
            print("BMI = Underweight")
        elif bmi < 24.9:
            print("BMI = Normal")
        elif bmi < 29.9:
            print("BMI = Overweight")
        else:
            print("BMI = Obesitas")
        break
    else:
        upayalogin += 1
        print(f"Login gagal! Anda telah mencoba {upayalogin}/{maksimallogin} kali.")
    
    if upayalogin == maksimallogin:
        print("Anda telah gagal login 3 kali, program berhenti.")

