def emi_simple(r , p, t ):
    return(r * p * t) / 100

def emi_compound(r, p, t, n):
    return p * (1 + (r/n)) **(n * t)


#P is the principal amount.
#r is the annual interest rate (in %).
#t is the time the money is invested for (in years).    
#n is the number of times that interest is compounded per year.

def simple(r, p , t , simpl ):
    print("rate of interest:" , r)
    print("principal amount:" , p)
    print("time the money is invested" , t)
    print("The simple interest is:" , simpl)
    total = simpl + p
    print(f"total amount: {total}"   )

def compund(r, p , t , n , a ):
    print("rate of interest:" , r)
    print("principal amount:" , p)
    print("time the money is invested" , t)
    print("times that interest:" , n)
    print("The simple interest is:" , a)
    
    print(f"total amount: {a +p}"   )


def main():

    while True:

        user = input ("do you want to calculate your emi ( yes / no)? ").lower()

        if user == "yes":
            emi = input(" compound /  simple ").lower()
            if emi == "simple":
                r = float(input("Enter the annual interest rate (in %): "))
                p = float(input("Enter the principal amount: "))
                t = float(input("Enter the time the money is invested for (in years): "))
                simpl =  emi_simple(r, p , t)
                simple(r, p , t , simpl)

            elif emi == "compound":
                r = float(input("Enter the annual interest rate (in %): "))
                p = float(input("Enter the principal amount: "))
                t = float(input("Enter the time the money is invested for (in years): "))
                n = int(input("Enter the number of times that interest is compounded per year: "))
                a = emi_compound(r, p, t, n)
                compund(r, p , t , n , a )

        elif user == "no":
            print("THANKS for emi calculator ,  good bye 🧑‍⚖️ ")
            break

        else:
            print("invalid input")

main()
