import subprocess

# Read the cURL command from the input file
with open('input.txt', 'r') as infile:
    curl_command = infile.read().strip()

try:
    # Send a cURL request and capture the output
    output = subprocess.check_output(curl_command.split())
    
    # Check if the output contains an error message
    if b'Could not resolve host' in output:
        print('The website is down or inaccessible.')
    else:
        print('The website is available.')
except subprocess.CalledProcessError as e:
    print(f'Error: {e.output.decode()}')
