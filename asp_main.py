import subprocess
import json

clingo_path = '.\\clingo-5.4.0-win64\\clingo.exe'
clingo_options = ['--outf=2','-n 0']
clingo_command = [clingo_path] + clingo_options

def solve(program):
    input = program.encode()
    process = subprocess.Popen(clingo_command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, error = process.communicate(input)
    result = json.loads(output.decode())
    if result['Result'] == 'SATISFIABLE':
        return [value['Value'] for value in result['Call'][0]['Witnesses']]
    else:
        return None
    
if __name__ == '__main__':
    print('Enter File Name (with extension): ')
    x = input()
    with open('./ASP_DL/'+x,'r') as file:
        theory = file.read().replace('\n','')
    print(solve(theory))