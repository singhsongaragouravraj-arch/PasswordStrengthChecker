# PasswordStrengthChecker
Password Strength Checker & Generator

A simple Python project that will check the strength of your user-inputted password and generate a strong password.

This project was created to see how I can apply Python and learn more about strings, conditions, regex, and random password generation.
Features
 Password Strength Checker

The program checks the given password against some specific conditions and classifies it into three categories:

• Weak

• Medium

• Strong

Based on the following rules:

1. Length of the password is at least 8 characters

2. The password has at least one uppercase letter

3. The password has at least one lowercase letter

4. The password has at least one number

5. The password has at least one special character
 Strong Password Generator

The program can also generate a 12-character long password with letters, numbers, and special characters.

The "random" Python module is used for this task.

Technologies

The project is written in Python 3 and uses the following Python modules:

• string: to get letters, digits, and punctuation

• random: to generate random passwords

• re: work with regular expressions

 How It Works

"check_strength(password)"

This function checks the given password against 5 basic rules. It counts the number of met conditions and outputs the password's strength classification.

"generate_strong_password()"

The generated password will be 12 characters long and will have letters, numbers, and special characters.

 How to Run

1. Make sure you have Python 3 installed.

2. Clone or download this repository

3. Run the following command in your terminal:

python password_checker.py

Once the program starts, type in the password you want to check and follow the prompts.

 Future Improvements

Some of the possible future improvements I will add

• Add GUI

• Add password entropy

• Add more detailed feedback

• Allow the user to choose the desired length for the generated password

• More password security checks

• etc

 What I Learned

I learned how to use Python functions, "if-else" conditions, loops, strings, regex, and modules. By creating this project, I also practiced my Python coding and software developing skills in general.



