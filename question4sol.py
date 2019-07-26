user_input=input("Enter an alphabet: ")

if user_input.isalpha() and len(user_input)==1:
    vowels=['a','e','i','o','u']
    flag=True
    for l in vowels:
        if l in user_input.lower():
            flag=False
            print("The alphabet is a vowel")
    if flag:
        print("The alphabet is a consonant")
else:
    print("Enter an alphabet only")