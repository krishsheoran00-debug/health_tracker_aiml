# Function to calculate BMI (Body Mass Index)
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Function to provide health category based on BMI logic
def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Healthy Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main Program Loop
def main():
    print("--- Personal Health Analytics Tool ---")
    user_data = []

    while True:
        print("\nOptions: [1] Add Entry [2] View History [3] Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter name: ")
            weight = float(input("Enter weight in kg: "))
            height = float(input("Enter height in cm: "))
            
            bmi_value = calculate_bmi(weight, height)
            category = get_category(bmi_value)
            
            # Storing data in a dictionary (Basic Data Structure)
            entry = {
                "name": name,
                "bmi": bmi_value,
                "status": category
            }
            user_data.append(entry)
            
            print(f"\nResult for {name}:")
            print(f"BMI: {bmi_value} | Category: {category}")

        elif choice == '2':
            print("\n--- Saved Health Records ---")
            if not user_data:
                print("No records found.")
            for record in user_data:
                print(f"Name: {record['name']} | BMI: {record['bmi']} | Status: {record['status']}")

        elif choice == '3':
            print("Exiting. Stay healthy!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()