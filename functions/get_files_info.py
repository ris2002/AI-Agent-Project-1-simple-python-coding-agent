import os
def get_files_from_wd(working_directory,directory=None):
    #we need to keep a gaurdrail so the llm edits the code only in the selected directory 
    abs_working_dir=os.path.abspath(working_directory) #gets absolute path from relative path
    print(directory)
    print(working_directory)
    if directory is None:
        directory=working_directory #root of given directory
        abs_directory=os.path.abspath(working_directory)
    else:
        join=os.path.join(working_directory,directory)
        abs_directory=os.path.abspath(join)
    if not abs_directory.startswith(abs_working_dir):
        return f'ERROR :"{directory}"is notin the working directory' # we arenot raiseing the error because we want LLM to read it if we raise errro the tool will stop working and the concept of agennt collapeses 
    contents=os.listdir(abs_directory)
    final_response=""
    for content in contents:
        content_path=os.path.join(abs_directory,content)
        is_dir=os.path.isdir(content_path)
        size=os.path.getsize(content_path)
        final_response+=f"- {content}:file_size={size} bytes,isdir:{is_dir}\n"
    return final_response
