import os
import subprocess
def run_python(working_directory:str,file_path:str,args=[]):
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
        final_args = ["python3", abs_file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args, 
            timeout=30, 
            capture_output=True, 
            text=True, 
            cwd=abs_working_dir)
        final_string= f"""STDOUT:{output.stdout}
                   STDERR:{output.stderr}  """

        if output.stdout=="" and output.stderr=="":
            final_string="No Code produced"
        if output.returncode !=0:
            final_string+=f"process exited with code {output.returncode}"

        return final_string
        






    except Exception as e:
        return f"Error: executing Python file: {e}"

