# Dynamic-Interpreter
Python Code interpreter at each modification


ALGO

VAR filepath: file
VAR content, last_content : String

START

    while (not CTR+C):  
        (* Infinity Loop )
        
        content = READ(filepath)
        
        If (content <> last_content) :
            (* Execute file (by content) *)
            
            Execute(content)
            
            last_content <- content
        EndIf
    EndWhile
END
