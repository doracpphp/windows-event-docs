#chatgpt-md-translator .\content\en\auditing\event-4624.md -o ./event-4624.md
import os
import subprocess

dir_path = "content\\en\\auditing"
out_path = "content\\ja\\auditing"
files_file = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith(".md")
] 

for f in files_file:
    if not os.path.isfile(os.path.join(out_path, f)):
        print(os.path.join(out_path, f))
        command = "chatgpt-md-translator -f 4096 " + os.path.join(dir_path, f) +" -o "+ os.path.join(out_path, f)
        ret = subprocess.run(command, shell=True)