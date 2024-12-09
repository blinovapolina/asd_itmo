import os
import subprocess

if __name__ == '__main__':
    current_directory = os.getcwd()
    for file in os.listdir(current_directory):
        if file.startswith('lab') and file != 'lab0' and file != 'lab1':
            lab_directory = os.path.join(current_directory, file)
            run_path = 'run_lab.py'
            print(f'======= RUNNING {lab_directory.split("/")[-1]} =======')
            python_interpreter = "/usr/local/bin/python3.13"
            subprocess.run([python_interpreter, run_path], cwd=lab_directory)
            print('\n')