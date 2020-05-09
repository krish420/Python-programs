def panagram(phrase):
    
    word='abcdefghijklmnopqrstuvwxyz'
    for letter in word:
        if word not in phrase:
            print("It is not a panagram")
            break
        else:
            print("It is a panagram")
            break
        

ph=raw_input("Enter a string: ")
panagram(ph)
