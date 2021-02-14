import os, OTP_custom as otp

def MakeNum(text, spliter):

    number = ''
    for i in range(len(text)):
        number += str(ord(text[i])) + spliter
    return number
        

def MakeTxt(numString, spliter):

    string = ''
    numbers = numString.split(spliter)
    numbers = numbers[:-1]
    for i in range(len(numbers)):
        string += chr(int(numbers[i]))

    return string



spliter = '-:-'    
while True:

    Actions = ["e", "d"]


    # ----------------- action -----------------
    
    searchAction = True
    while searchAction:
        Action = input("Choose action from encrypt or decrypt (e/d): ")

        if Action in Actions:
            searchAction = False
            print("Action found!")
        else:
            print("Action not found...")


    # ---------------- selecting file ----------------
    fileSelect = True
    while fileSelect:
        fileName = input("Select file: ")

        if fileName in os.listdir():
            fileSelect = False
            print("File found!")

        else:
            print("File not found...")

    # ------------------- get key --------------------------

    gettingKey = True
    while gettingKey:
        key = input("Key: ")
        correct_key = input("Is the key \"" + key + "\"? (y/n)")
        if correct_key == "n":
            pass
        elif correct_key == "y":
            gettingKey = False
    
    # ---------------------- encrypting --------------------

    if Action == "e":
        file = open(fileName).read()
        salt = otp.salt() # generating salt
        key = otp.key512(key, salt) #generating key

        e_file = otp.encrypt(file, key)
        
        e_fileSalt = e_file + salt
        with open("EN_"+fileName, "w+", errors="ignore") as f:
            f.write(MakeNum(e_fileSalt, spliter))
            f.close()
            
     # ---------------------- decrypting --------------------

     
    elif Action == "d":
        
        e_file = MakeTxt(open(fileName).read(), spliter)
        file = e_file[0:-10]
        salt = e_file[-10:]
        
        key = otp.key512(key, salt)
        de_file = otp.decrypt(file, key)
        
        with open("DE"+fileName, "w+", errors="ignore") as f:
            f.write(de_file)
            f.close()


    else:

        print("error...")



    rep = input("run again(-), close(Enter) ")
    if rep == "-":
        pass
    else:
        break






























