KRISH CHOUDHARY  
25BAI10143
VITYARTHI PROJECT

Python Console Calculator Script:

A lightweight, console-based Python script that performs basic arithmetic operations on floating-point numbers.

DESCRIPTION:

The Personal Health Analytics Tool is a Python-based console application designed to help users monitor and understand their health status using the Body Mass Index (BMI). The system allows users to input their basic details such as name, weight, and height, and then calculates their BMI using a standard mathematical formula.

Based on the calculated BMI value, the application classifies the user into one of the health categories: Underweight, Healthy Weight, Overweight, or Obese. In addition to classification, the system provides simple health recommendations to guide users toward maintaining or improving their fitness.

The project is implemented using a modular programming approach with functions, loops, and conditional statements. It demonstrates fundamental concepts of programming as well as basic Artificial Intelligence principles through rule-based decision-making

FEATURES:
1. BMI Calculation:-
Calculates Body Mass Index (BMI) accurately using user-provided height and weight.
2. Health Classification:-
Categorizes users into Underweight, Healthy Weight, Overweight, or Obese based on BMI values.
3. Personalized Recommendations:-
Provides basic health advice according to the user’s BMI category.
4. User Data Storage:-
Stores multiple user records during program execution using lists and dictionaries.
5. View History:-
Allows users to view previously entered health records.
6. Statistical Analysis:-
Displays the number of users in each BMI category for basic data insights.
7. Menu-Driven Interface:-
Provides a simple and interactive console-based menu for easy navigation.
8. Input Validation:-
Handles invalid or incorrect inputs to prevent errors and ensure smooth execution.

Prerequisites:

Python 3.x installed on your system.

How to Use:

Save the Python code into a file named health tracker.py (or any preferred name).

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script using the following command:

bash python health tracker.py

Follow the on-screen prompts to select an operation and enter your name,weight,height.

EXAMPLE INTERACTIONS:

=== Personal Health Analytics Tool ===

Menu:
1. Add Entry
2. View History
3. View Statistics
4. Exit

Enter your choice: 1

Enter name: Raj
Enter weight (kg): 70
Enter height (cm): 175

Rahul's Result:
BMI: 22.86
Category: Healthy Weight
Advice: Maintain your current lifestyle.


Menu:
1. Add Entry
2. View History
3. View Statistics
4. Exit

Enter your choice: 1

Enter name: Aman
Enter weight (kg): 90
Enter height (cm): 170

Aman's Result:
BMI: 31.14
Category: Obese
Advice: Consult a doctor and follow a fitness plan.


Menu:
1. Add Entry
2. View History
3. View Statistics
4. Exit

Enter your choice: 2

--- Saved Records ---
Name: Raj | BMI: 22.86 | Status: Healthy Weight
Name: Aman | BMI: 31.14 | Status: Obese


Menu:
1. Add Entry
2. View History
3. View Statistics
4. Exit

Enter your choice: 3

--- Health Statistics ---
Underweight: 0
Healthy Weight: 1
Overweight: 0
Obese: 1


Menu:
1. Add Entry
2. View History
3. View Statistics
4. Exit

Enter your choice: 4

Exiting... Stay healthy!


Important note on existing:


The application provides an Exit option in the menu to allow users to safely terminate the program. When the user selects this option, the system stops execution gracefully after displaying a closing message.

Since the program uses in-memory data storage, all user records are temporary and will be lost once the program is exited. This ensures simplicity but also highlights the limitation of not having permanent data storage.

Proper exit handling ensures:

Smooth termination of the program

Prevention of runtime errors

Clear communication to the user with a final message
