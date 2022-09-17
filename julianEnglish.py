#This program will serve me as a writer for the progress made in the project Teach English to Julian

def main () :
    key = True
    while key :
        try : 
            fileName= "julianProgress.txt"
            fileIn = open ( fileName , "a")
            FileWriter(fileIn)
            key = False 
        finally :
            fileIn.close()

def FileWriter( file ) :
    #Coma separated values
   # week = input ("What week 
    date = input("Enter the date of this session (day, month, year): ")
    file.write ( date)
    file.write (" , ")
    sesh = input ("Completed successfuly ? (Yes or No ): ")
    file.write (sesh)
    file.write (" , ")
    comment = input ( "Add any comments : " )+ "."
    file.write ( comment + "\n" )
    

main () 
    
        
        
        
        
