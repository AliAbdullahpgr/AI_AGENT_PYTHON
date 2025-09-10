import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from call_function import call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = """
    You are a helpful AI coding agent working in the 'calculator' directory.

    When a user asks a question or makes a request, create a step-by-step plan using the available functions:
    - get_files_info: List files and directories (with directory parameter)
    - get_file_content: Read the content of a file (with file_path parameter)  
    - write_file: Write to a file (with file_path and content parameters)
    - run_python_file: Run a Python file (with file_path and optional arguments parameters)

    Work systematically:
    1. First explore the relevant files/directories to understand the codebase
    2. Read specific files that are relevant to the user's question
    3. Analyze the code and provide a comprehensive answer
    4. If the user asks you to make changes, implement them and test

    When the user asks about the code project - they are referring to the working directory. So, you should typically start by looking at the project's files, and figuring out how to run the project and how to run its tests, you'll always want to test the tests and the actual project to verify that behavior is working.
    All file paths should be relative to the working directory. When you have gathered enough information to answer the user's question completely, provide a final response without calling more functions.
    """
    if len(sys.argv) < 2 :
        print("I need a prompt")
        sys.exit(1)
        return
    verbose = False
    if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
        verbose = True
    prompt = sys.argv[1];
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
    )
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
    )
    
    # Agent feedback loop - up to 20 iterations
    for i in range(20):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages,  # Pass entire conversation history
                config=config
            )
            
            if response is None or response.usage_metadata is None:
                print("response is malformed")
                return
                
            if verbose:
                print(f"Iteration {i+1}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            
            # Add model's response to conversation
            if response.candidates:
                for candidate in response.candidates:
                    if candidate is None or candidate.content is None:
                        continue
                    messages.append(candidate.content)

            # Handle function calls
            if response.function_calls:
                for function_call_part in response.function_calls:
                    result = call_function(function_call_part, verbose)
                    messages.append(result)
            else:
                # No more function calls, check for final response
                if response.text:
                    print("Final response:")
                    print(response.text)
                    break
                
        except Exception as e:
            print(f"Error during iteration {i+1}: {e}")
            break
    else:
        print("Max iterations reached without completion")


main()

# Changes