print("Which fiat do you want to convert to toman?")
select = input("dollar, euro, pound: ")  

print("How much to convert?")
amount = float(input(""))  

# fiats
fiat1 = 92400  # dollar
fiat2 = 99300  # euro
fiat3 = 110200  # pound


if select == "dollar":
    result = amount * fiat1
    print(f"{amount:,} dollars equals {result:,} toman.") 
elif select == "euro":
    result = amount * fiat2
    print(f"{amount:,} euros equals {result:,} toman.")
elif select == "pound":
    result = amount * fiat3
    print(f"{amount:,} pounds equals {result:,} toman.")
else:
    print("Invalid currency selected.")

