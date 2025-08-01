import random
n=random.randint(1,100)
a=-1
guess=0
while(a!=n):
    guess +=1
    a=int(input("guess the number:"))
    if(a>n):
        print("guess the lower number")
    elif(a<n):
        print("guess the higher number")
    else:
         print("🎉 Congratulations! You guessed it right!")

print(f"you have guessed the number in {guess} attempts")