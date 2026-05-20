from functions.get_files_info import get_files_from_wd
from functions.get_file_contents import get_contents
from functions.write_file_content import write_file
def main():
    working_dir="calculator"
    print(write_file(working_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
main()

