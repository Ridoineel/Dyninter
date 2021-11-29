# Dyninter: Dynamic python program interpreter and watcher.

\# Python program monitor <br/>
\# Python program watcher

Python Code interpreter at each file's modification.

>**Use -f or --file option to specify the input file**: <br/>
    ex: 
    ``` 
        ./dyninter.py -f test.py
    ```

_____________

### ALGO

```

VAR file_path: file
    last_modification_time, tmp_modification_time : Float

START
    
    file_path <-- python program file (file path)
    last_modification_time <-- file modification time 
    
    while (not CTR+C):  
        (* Infinity Loop *)

        tmp_modification_time <-- file modification time 
        
        If (last_modification_time <> tmp_modification_time) :
            (* Execute file *)
            Execute(file_path)
            
            last_modification_time <-- tmp_modification_time
        EndIf
    EndWhile
    
END
```
