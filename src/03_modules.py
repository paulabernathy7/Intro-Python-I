import os
import sys
import platform

"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
if len(sys.argv) > 1:
    print(sys.argv[1])
# Print out the OS platform you're using:
# YOUR CODE HERE
print(os.name)
print(platform.system())
print(platform.release())
# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("PID of the current process is:")

print(os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("CWD is:")

print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("user logged in")
print(os.getlogin())
