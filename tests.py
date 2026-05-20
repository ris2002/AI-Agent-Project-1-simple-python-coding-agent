from functions.get_files_info import get_files_from_wd
from functions.get_file_contents import get_contents
from functions.write_file_content import write_file
from functions.run_python import write_python
def main():
    working_dir="calculator"
    print(write_python(working_dir,"main.py",["3 + 5"]))
    
main()

