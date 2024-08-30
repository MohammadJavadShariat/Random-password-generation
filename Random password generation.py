print("Hello my friend! \n I am an automatic password generator program.")
while(True): #To repeat the question
    Input = input("If you want a password to be generated for you, enter 'yes' and otherwise enter 'no'😊:\n")
    
    def password(Input) : #Function to generate password
        """
        This function is used to generate a random password.        
        The input parameters of the function must be the word 'yes' or 'no'.
        """
        #If a wrong word or number is entered.
        if Input != "yes" and Input != "no" :
            while(True): #To repeat the question if entered incorrectly
                print("\nThe given value is invalid. Please enter only yes or no.😱 \n")
                Input2 = input("If you want a password to be generated for you, enter 'yes' and otherwise enter 'no'😊:\n")
                if Input2 == "yes" :
                    Input = Input2
                    break
                elif Input2 == "no" :
                    Input = Input2
                    break
        if Input == "no" : 
            return ""
        if Input == "yes" :
            import random as rand
            password = "" #Variable to store the password
            S_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            C_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            Signs = ["@","#","."]
            #The bottom part for putting numbers, letters and symbols in the code            
            for i in range(2) :
                rand_C_letter = rand.choice(C_letters)
                password += rand_C_letter
            for i in range(2) :
                rand_S_letter = rand.choice(S_letters)
                password += rand_S_letter
            for i in range(1) :
                rand_Signs = rand.choice(Signs)
                password += rand_Signs
            for i in range(4) :
                rand_num = rand.randint(0 , 9)
                password += str(rand_num)
            return password
        
    password1 = password(Input)
    
    if password1 != "" :
        name = input("Enter your name in English:")
        #The following two variables to check if the name is English        
        Persian_letters = {'ی', 'ه', 'و', 'ن', 'م', 'ل', 'گ', 'ک', 'ق', 'ف', 'غ', 'ع', 'ظ', 'ط', 'ض', 'ص', 'ش', 'س', 'ژ', 'ز', 'ر', 'ذ', 'د', 'خ', 'ح', 'چ', 'ج', 'ث', 'ت', 'پ', 'ب' ,'آ', 'ا'}
        num_letter = 0
    
    if password1 == "" :
        print("any comfort Bye!")
        break
    
    else:
        #To generate a special password        
        name2 = password1[0:5] + name + '.' +password1[5:11]
        #To check if the name is English        
        for j in Persian_letters :
            if j in name :
                num_letter += 1
        if num_letter > 0 :
            print(f"Dear {name}, please enter the name in English.")
        else:
            print(f"\n{password1}: Normal password \n{name2}: Your special password")
            