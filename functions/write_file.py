import os
from google.genai import types
def write_file(working_directory, file_path,content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Could not create parent dirs: {parent_dir} = {e}"
    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
            return (
                f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            )
    except Exception as e:
        return f"Failed to write to file: {file_path}, {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=" Overwrites to a an existing file if it doesn't exist (and creates required parent dirs safely) contrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to, relative to the working directory.",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file as a string"
            )
        },
    ),
)