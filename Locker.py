import os, OTP_custom as otp

# remember to use UTF-32

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
        with open("EN_"+fileName, "w+", errors="ignore", encoding="utf-16") as f:
            f.write(e_fileSalt)
            f.close()
            
     # ---------------------- decrypting --------------------

     
    elif Action == "d":
        
        e_file = open(fileName, encoding = "utf-16").read()
        file = e_file[0:-10]
        salt = e_file[-10:]
        
        key = otp.key512(key, salt)
        de_file = otp.decrypt(file, key)
        
        with open("DE"+fileName, "w+", errors="ignore", encoding="utf-16") as f:
            f.write(de_file)
            f.close()


    else:

        print("error...")



    rep = input("run again(-), close(Enter) ")
    if rep == "-":
        pass
    else:
        break






























