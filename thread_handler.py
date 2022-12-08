import threading
#import time

class thread_handler:
    """A handler for threads and threading for Python 2 and 3."""

    def __init__(self):
        """Initialize handler with no threads."""
        self.threads = {}

    @classmethod
    def start(self, func, args=()):
        """Initializer handler with a thread."""
        newThread = func.__name__
        self.threads[newThread] = threading.Thread(target=func, args=args)
        self.threads[newThread].start()

    def add(self, func, args=()):
        """Add a new thread to the handler."""
        newThread = func.__name__

        self.checkDupe(newThread)
        
        self.threads[newThread] = threading.Thread(target=func, args=args)
        self.threads[newThread].start()

    def wait(self, func, args=()):
        """Add a new thread and block all others until it finishes executing."""
        newThread = func.__name__

        self.checkDupe(newThread)
        
        self.threads[newThread] = threading.Thread(target=func, args=args)
        self.threads[newThread].join()

    def status(self, func):
        """Check on the status of a specific thread."""
        threadStatus = self.threads[func.__name__].is_alive()
        return threadStatus

    def list(self):
        """Grab a list of all the threads currently running under thread_handler."""
        self.update()
        keys = list(self.threads.keys())
        return keys

    def display(self):
        """Display all currently active threads."""
        self.update()
        keys = self.list()
        for key in keys:
            print(key)

    def update(self):
        """Update to delete all inactive threads from the handler."""
        for thread in self.threads.copy():
            if self.threads[thread].is_alive() == False:
                del(self.threads[thread])

    def checkDupe(self, newThread):
        """Checks if a thread already exists for the function."""
        if (newThread in self.threads):
            raise DuplicateThreadError(f"A thread already exists for {newThread}.")

class DuplicateThreadError(Exception):
    """A duplicate thread error exception."""
    pass

# def test():
#     print("Testing...")
#     time.sleep(5)
#     print("Finished.")

# def test2():
#     print("Testing...")
#     time.sleep(10)
#     print("Finished.")

# if __name__ == "__main__":
#     tHandler = thread_handler() # Init empty thread handler
#     tHandler.add(test)          # Add thread to handler
#     tHandler.add(test2)         # Add second thread to handler

#     print(tHandler.status(test))   # Check the status of the first thread

#     print(tHandler.list())      # List and print each thread currently active

#     tHandler.display()          # Same as previous, but with method

#     time.sleep(6)               # Wait for them to finish

#     tHandler.add(test)          # Attempt to add copy, raise error

#     tHandler.update()           # Delete inactive threads

#     print(tHandler.list())      # List and print each currently active thread again