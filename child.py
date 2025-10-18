import os
import subprocess

def wait_for_debugger():
    import debugpy
    print("PYTHON_DEBUG is set. Waiting for debugger to attach...")
    debugpy.listen(("localhost", 5678))  # VS Code debugger will attach here
    debugpy.wait_for_client()
    print("Debugger attached!")

def powershell_function_exists(function_name, module_path):
    check_cmd = f"Import-Module '{module_path}'; Get-Command {function_name}"
    result = subprocess.run(
        ["powershell", "-Command", check_cmd],
        capture_output=True, text=True
    )
    return result.returncode == 0 and function_name in result.stdout

def call_powershell_function(function_name, args="", module_path=None):
    import_cmd = f"Import-Module '{module_path}'; " if module_path else ""
    call_cmd = f"{import_cmd}{function_name} {args}"
    try:
        subprocess.run(["powershell", "-Command", call_cmd], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error calling PowerShell function '{function_name}': {e}")

def main():
    # Check for debugger
    if os.getenv("PYTHON_DEBUG", "0") != "0":
        wait_for_debugger()

    # Resolve module path
    module_path = os.path.join(os.getcwd(), "MyFunctions.psm1")

    # Check and invoke PowerShell functions
    for func in ["Show-Trace", "Show-Greeting"]:
        if powershell_function_exists(func, module_path):
            print(f"Function '{func}' found. Invoking...")
            call_powershell_function(func, "'Called from Python'", module_path)
        else:
            print(f"Function '{func}' not found in PowerShell.")

if __name__ == "__main__":
    main()
