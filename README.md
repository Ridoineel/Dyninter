# Dynamic-Interpreter
Python Code interpreter at each file's modification (save)

**Use -f or --file option to specify the input file**:
    ex: ./dyninter.py -f test.py


ALGO

VAR filepath: file
    content, last_content : String

START

    last_content <-- ""
    
    while (not CTR+C):  
        (* Infinity Loop *)
        
        content <-- READ(filepath)
        
        If (content <> last_content) :
            (* Execute file (by content) *)
            Execute(content)
            
            last_content <-- content
        EndIf
    EndWhile
    
END

**Author**: RidoineEl <ridoineelofficiel@gmail.com/>
