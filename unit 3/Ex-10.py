from Temperature import f_to_c, c_to_f, c_to_k
try:
    while True:
        print("Choose an option:")
        print("1.fahrenheit to celcius.")
        print("2.celcius to fahrenheit.")   
        print("3.celcius to kelvin.")
        o=int(input("Enter choice:"))
        if o==1:
            fahrenheit=float(input("Enter fahrenheit"))
            c=f_to_c.fahrenheit_to_celcius(fahrenheit)
        elif o==2:
            celcius=float(input("Enter celcius"))
            f=c_to_f.celcius_to_faherenheit(celcius)
        elif o==3:
            celcius=float(input("Enter celcius"))
            k=c_to_k.celcius_to_kelvin(celcius)
        else:
            print("Invalid Choice.")
            break
        print("________Wanna continue________")
        p=(input("Enter Y/y for continue and N/n for not:"))
        if p.lower =='n':
            break
       
except:
    print("Error!!!")