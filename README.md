# AI Agent with Function Calling

A Python-based AI agent that uses Google's Gemini API with function calling capabilities to interact with files and execute Python code. The agent can explore codebases, read files, write code, and run Python scripts autonomously.

## Features

- **Function Calling**: Structured interaction with the environment through defined functions
- **File System Operations**: List directories, read file contents, and write files
- **Code Execution**: Run Python files with optional arguments
- **Conversation Memory**: Maintains context across multiple interactions
- **Safety Constraints**: All operations are constrained to a specified working directory

## Available Functions

1. **`get_files_info`** - List files and directories with size information
2. **`get_file_content`** - Read the contents of any file
3. **`write_file`** - Create or update files with new content
4. **`run_python_file`** - Execute Python scripts with optional command-line arguments

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AliAbdullahpgr/AI_AGENT_PYTHON.git
   cd AI_AGENT_PYTHON
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

Run the agent with a natural language prompt:

```bash
uv run main.py "your prompt here"
```

### Example Commands

```bash
# Explore and understand code
uv run main.py "how does the calculator render results to the console?"

# Analyze and fix bugs
uv run main.py "find and fix any bugs in the calculator code"

# Run tests
uv run main.py "run the tests for the calculator and show me the results"

# Code modifications
uv run main.py "add a new feature to handle division by zero gracefully"
```

### Verbose Mode

Add `--verbose` flag for detailed execution information:

```bash
uv run main.py "your prompt here" --verbose
```

## Project Structure

```
AI_AGENT_PYTHON/
├── main.py                 # Main agent entry point
├── call_function.py        # Function dispatcher
├── config.py              # Configuration settings
├── functions/              # Available functions for the agent
│   ├── get_files_info.py   # Directory listing functionality
│   ├── get_file_content.py # File reading functionality
│   ├── write_file.py       # File writing functionality
│   └── run_python_file.py  # Python execution functionality
├── calculator/             # Example project for the agent to work with
│   ├── main.py            # Calculator main program
│   ├── tests.py           # Calculator tests
│   └── pkg/               # Calculator package
│       ├── calculator.py   # Core calculation logic
│       └── render.py      # Result rendering functionality
└── tests.py              # Agent integration tests
```

## How It Works

1. **User Input**: Provide a natural language prompt describing what you want the agent to do
2. **Function Planning**: The agent analyzes the request and plans which functions to call
3. **Function Execution**: The agent executes functions in sequence, building up context
4. **Iterative Refinement**: The agent can call multiple functions and refine its approach based on results
5. **Final Response**: Once the task is complete, the agent provides a comprehensive response

## Example Interaction Flow

```
User: "how does the calculator render results to the console?"
│
├── Agent calls get_files_info to explore the directory
├── Agent calls get_file_content to read main.py
├── Agent calls get_file_content to read pkg/render.py
└── Agent provides detailed explanation of the rendering process
```

## Configuration

The agent operates within the `calculator` directory by default. This is configured in `call_function.py`:

```python
working_directory = "calculator"
```

You can modify this to work with different projects.

## Safety Features

- All file operations are constrained to the specified working directory
- Path traversal attacks are prevented through absolute path validation
- File size limits are enforced when reading content
- Maximum iteration limits prevent infinite loops

## Requirements

- Python 3.12+
- Google Gemini API key
- uv package manager

## Dependencies

- `google-genai` - Google Gemini API client
- `python-dotenv` - Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Example Projects

The repository includes a calculator project as an example of what the agent can work with:

- **Calculator**: A command-line calculator with expression parsing and formatted output
- **Tests**: Comprehensive test suite for the calculator functionality
- **Modular Design**: Separated calculation logic and rendering functionality

The agent can analyze, modify, test, and enhance this calculator or any other Python project placed in its working directory.