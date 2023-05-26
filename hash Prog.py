import hashlib

choice_val = "y"

while choice_val == "y" or choice_val =="Y":
    data = input("Enter some data : ")
    print("Select any one hashing algorithm from the following".center(80,"*"))
    print("\t1. MD5 \n\t2. SHA - 256\n\t3. SHA - 384\n\t4. SHA - 512\n\t5. SHA1")
    algo = input("Enter the number or the name of the algoirhtm: ")
    flag=True
    if algo == "1" or algo == "MD5":
        hash_value = hashlib.md5(data.encode()).hexdigest()
    elif algo =="2" or algo=="SHA - 256":
        hash_value =hashlib.sha256(data.encode()).hexdigest()
    elif algo =="3" or algo == "SHA - 384":
        hash_value = hashlib.sha384(data.encode()).hexdigest()
    elif algo =="4" or algo == "SHA - 512":
        hash_value = hashlib.sha512(data.encode()).hexdigest()
    elif algo =="5" or algo == "SHA1":
        hash_value = hashlib.sha1(data.encode()).hexdigest()
    else:
        print("Please enter a valid option.")
        flag= False
    if flag:
        print("The hash value of the enter data is : ",hash_value)
    choice_val = input("Do you want to continue (y/Y/n/N):")
    print("".center(80,"*"))
        
        
