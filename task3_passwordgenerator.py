import random,string

n=int(input("Length: "))
chars=string.ascii_letters+string.digits
pwd=''.join(random.choice(chars) for i in range(n))

print("Password:",pwd)
