def bmi_category(bmi):

    #BMI category based on BMI value

    if bmi < 15:
        return "Very severely underweight 🧑‍⚖️"
    elif bmi < 16:
        return "Severely underweight 🤕"
    elif bmi < 18.5:
        return "Underweight 😐"
    elif bmi < 25:
        return "Normal weight 👍"
    elif bmi < 30:
        return "Overweight 🤯"
    elif bmi < 35:
        return "Moderately obese 🤪"
    elif bmi < 40:
        return "Severely obese 😨"
    else:
        return "Very severely obese 😱"
         



def bmi_calculator():

    #This program will calculate the Body Mass Index (BMI) for users 

    name = input("Enter your Name: ")
    height = float(input("Please Share your weight (in kg): "))
    weight = float(input("Please Share your height (in meters): "))

    # BMI Calculation

    bmi = (weight / (height ** 2))


    print('\n' , name ,' your BMI is: ' , round(bmi, 2) ,'\n')

    # Category determination

    category = bmi_category(bmi)


    print("Category: ", category ,"\n")
 

def main():

    #Main function to run the BMI calculator.

    while True:

        
        calculate = input("Do you want to calculate your BMI? (yes/no): ").lower()
        
        if calculate == 'yes':
            bmi_calculator()

        elif calculate == 'no':
            print("Thank you for using BMI calculator!")
            break

        else:
            print("choose yes or no")
            continue


# Run function with yes
main()

