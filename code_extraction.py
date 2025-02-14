import os
import ast
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def extract_python_functions(code):
    """Extracts function names from Python code using AST."""
    try:
        tree = ast.parse(code)
        return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    except:
        return []

def extract_java_methods(code):
    """Extracts method names from Java code using regex."""
    return re.findall(r"public\s+\w+\s+(\w+)\(", code)
