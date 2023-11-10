# Thread-Handler
 A class for handling Python threads using the threading module.

The class name is thread_handler. To instantiate an object of this class, use
"thread_handler_name = thread_handler". The handler cannot have multiple threads
with the same function/name.

Testing is included in the file, but commented out. Additional tests are welcome.

## Methods

### thread_handler.start(function name, args)
    Initializes a thread handler with a new thread with function 'function name'
    and arguments 'args', which defaults to empty.

### thread_handler.add(function name, args)
    Creates a new thread managed by the handler with function 'function name' 
    and arguments 'args', which defaults to empty.

### thread_handler.wait(function name, args)
    Creates a new thread managed by the handler with function 'function name'
    and arguments 'args', which defaults to empty, and blocks other threads
    until it is finished executing.

### thread_handler.status(function name)
    Checks on the function 'function name' and returns True if it is still
    running.

### thread_handler.list()
    Creates a Python list object with the names of all currently alive and
    running threads. Automatically runs 'update()' to check active threads.

### thread_handler.display()
    Displays a list of all currently alive and running threads in the console.
    Automatically runs update().

### thread_handler.update()
    Checks active threads in the handler and deletes all terminated/inactive
    threads.

### thread_handler.checkDupe()
    Internal error checker to make sure there do not exist multiple threads
    of the same name.
