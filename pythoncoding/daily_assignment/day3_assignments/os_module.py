#os module
import os
print("current directory:",os.getcwd())
os.makedirs("simple_dir",exist_ok=True)
print("directory exists:",os.path.isdir("sample_dir"))
print("contents:",os.listdir("."))