
import os
from config import MAX_CHARS
def get_contents(working_directory,file_path):
    abs_working_dir=os.path.abspath(working_directory) 
    join=os.path.join(working_directory,file_path)
    abs_file_path=os.path.abspath(join)
    if not  abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    file_content_string=""
    try:
        with open(abs_file_path,'r') as f:
            file_content_string=f.read(MAX_CHARS)
            if len(file_content_string)>=MAX_CHARS:
                file_content_string+=(f'[...File "{file_path}" truncated at {MAX_CHARS} characters]')
        return file_content_string
    except Exception as e:
        return f'Execption reading file :{e}'