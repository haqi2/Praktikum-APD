beratbadan = float(input("Masukkan berat badan: "))
tinggibadan = float(input("Masukkan tinggi badan: "))
tinggimeter = tinggibadan / 100
total = beratbadan / (tinggimeter * tinggimeter)

if total < 18.5 :
    print ("bmi = Underweight") 
elif total < 24.9 :
    print ("bmi = Normal")
elif total < 29.9 :
    print ("bmi = overweight")
else :
    print ("bmi = obesitas")
    
