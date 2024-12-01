import random
import string


print("Welcome to the password Genarator!")

pw_len = int(input("Enter the total numbers of characters in the password : "))
lett_len = int(input("Enter the numbers of latters in the password : "))
num_len = int(input("Enter the numbers of numbers in the password : "))
sym_len = int(input("Enter the numbers of symbols in the password : "))

lett = random.choices(string.ascii_letters, k=lett_len)
pun = random.choices(string.punctuation, k=sym_len)
num = random.choices(string.digits, k=num_len)

char = lett + pun + num
random.shuffle(char)

password = ""

for x in char : 
    password += f"{x}"

if pw_len == 0 or (lett_len + num_len + sym_len) == 0 : 
    print("Are you ahbel")

elif  pw_len <  lett_len + num_len + sym_len : 
    print("Invalid input. The sum of letters, numbers and symbols does't match the password length. Plz try again")

else : 
    print(f"Generated Password : {password}")

