import string
import random

def generating_password(length_of_password):
    # Defining the char to be used in the generated_password
    char = string.ascii_letters + string.punctuation + string.digits

    # Generating generated_password
    generated_password = ''.join(random.choice(char) for i in range(length_of_password))
    return generated_password


# Input from the user for the desired generated_password length_of_password
length_of_password = int(input("Enter the desired length_of_password for the generated_password: "))
    
# Generate the generated_password by passing value to function
generated_password = generating_password(length_of_password)
    
# Display the generated_password
print(f"Generated generated_password: {generated_password}")


