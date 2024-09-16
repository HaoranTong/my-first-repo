with open('new_file1', 'r',encoding = 'utf-8') as file:
    
    while True:
        content = file.readline()
            
        if not content:
            break  
        print(content)       
        continue_reading = input("Do you want to read the next line? (y/n): ")
        if continue_reading.lower() != 'y':
             break