"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
 in addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)



#file handling

# Read the contents of the file
file = open("filename.txt", "r") 
print(file.read()) 
file.close()  


# Write to the file
file = open("filename.txt", "w") 
file.write("Thank you for reading.") 
file.close()

def write_to_file(file_name, data, mode="w"):
    
   # Writes data to a file
    #:parameter file_name: Name of the file to write to
    #:parameter data: Data to write to the file
    #:parameter mode: Mode to open the file in
    #:return:
    

"""
# exception handling

try:
    file = open("filename.txt", "r")
    print(file.read())

except FileNotFoundError:
        print("File not found")

finally:
        file.close()
