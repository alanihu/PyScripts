import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  print(os.getcwd())
  with open ('script.py') as file:
    pass
  os.chdir("..")
  print(os.getcwd())
  # Return the list of files in the new directory
  return os.listdir("PythonPrograms")

print(new_directory("PythonPrograms", "script.py"))
