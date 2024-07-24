import subprocess

# Run the image analyzer
result1 = subprocess.run(['python3', 'imageanalyzer.py'], capture_output=True, text=True)

# Check if image analyzer ran successfully
if result1.returncode == 0:
    print("imageanalyzer.py ran successfully.")
else:
    print(f"imageanalyzer.py encountered an error: {result1.stderr}")
    exit(1)

# Run violations determiner 
result2 = subprocess.run(['python3', 'violationsdeterminer.py'], capture_output=True, text=True)

# Check if violations determiner ran successfully
if result2.returncode == 0:
    print("violationsdeterminer.py ran successfully.")
else:
    print(f"violationsdeterminer.py encountered an error: {result2.stderr}")
    exit(1)
