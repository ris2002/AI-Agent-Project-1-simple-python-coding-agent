import os
import subprocess
def write_python(working_directory:str,file_path:str):
    abs_working_dir=os.path.abspath(working_directory) 
    join=os.path.join(working_directory,file_path)
    abs_file_path=os.path.abspath(join)
    if not  abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    if not file_path.endswith(".py"):
        return f'Error: File not a python file: "{file_path}"'
    try:
        output=subprocess.run(["python3",file_path],timeout=30,capture_output=True,cwd=abs_working_dir)
        return output



    except Exception as e:
        return f"Error: executing Python file: {e}"

