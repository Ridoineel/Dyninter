# Dynamic-Interpreter
Python Code interpreter at each modification


ALGO

VAR file: file
VAR content, last_content : String

START

    while (not CTR+C):  
        (* Infinity Loop )
        
        content = READ(file)
        
        If (content <> last_content) :
            (* Execute file (by content) *)
            
            Execute(content)
            
            last_content <- content
        EndIf
    EndWhile
END
