import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)

    abs_directory = os.path.abspath(os.path.join(abs_working_dir, directory))
    if not abs_directory.startswith(abs_working_dir):
        return f'Error: "{directory}" is not a directory'

    contents = os.listdir(abs_directory)
    filepath = ""
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        filepath += f" - {content}: file_size={size}, is_dir={is_dir}\n"

    return filepath
