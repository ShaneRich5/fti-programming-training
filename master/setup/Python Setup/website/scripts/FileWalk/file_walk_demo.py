import os
import shutil


target_dir = os.path.join(os.getcwd(), 'directory0')
output_dir = os.path.join(os.getcwd(), 'directory1')

cache = []
for (dirpath, dirnames, filenames) in os.walk(target_dir):
    for fname in filenames:
        target_path = os.path.join(dirpath, fname)
        cache.append(target_path)
        shutil.copy2(target_path, output_dir)
        output_path = os.path.join(output_dir, fname)
        if os.path.isfile(output_path):
            print("Successfully Copied: ", fname)
        else:
            print("Unable to copy file: ", fname)
