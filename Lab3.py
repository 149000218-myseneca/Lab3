
def helloWorld():
    print('Hello World')
    
helloWorld()


def write_name_to_file():
    file_path = "ppanchal20/home/ops345/lab3/file.txt"
    name = "Your Name"
    
    try:
        with open(file_path, 'w') as file:
            file.write(name)
        
        print("File created successfully.")
    except Exception as e:
        print("An error occurred:", str(e))
