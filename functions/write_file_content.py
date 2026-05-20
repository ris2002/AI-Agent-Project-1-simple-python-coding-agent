import os 
def write_file(working_directory,file_path,content):
    abs_working_dir=os.path.abspath(working_directory) 
    join=os.path.join(working_directory,file_path)
    abs_file_path=os.path.abspath(join)
    if not  abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    parent_dir=os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'Could not create parent dirs:{parent_dir}. Exceptionn:{e}'

    try:
        with open(abs_file_path,'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Execption writing file, filepath {file_path}, Exception :{e}'
    
