import re

def detect_reference_misuse_in_loop(file_content):
    pattern = re.compile(
        r'for\s*\(\s*int\s+\w+\s*=\s*\d+;\s*\w+\s*<\s*\d+;\s*\+\+\w+\s*\)\s*\{'
        r'[^}]*&\s*\w+\s*=\s*\w+\s*\[\s*\w+\s*\][^}]*\}'
    )
    
    matches = pattern.finditer(file_content)
    vulnerabilities = []

    for match in matches:
        vulnerabilities.append((match.start(), match.end(), match.group()))
    
    if vulnerabilities:
        print("Potential reference misuse detected in for-loop:")
        for vuln in vulnerabilities:
            print(f"From position {vuln[0]} to {vuln[1]}:\n{vuln[2]}")
    else:
        print("No potential reference misuse detected.")

file_path = 'C++Catastrophes.cpp'  
with open(file_path, 'r') as file:
    file_content = file.read()

detect_reference_misuse_in_loop(file_content)
