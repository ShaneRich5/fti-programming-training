import os
import shutil

path_to_docs = os.path.join(os.getcwd(), 'docs')
path_to_labs = os.path.join(os.getcwd(), 'master', 'labs')


def copy_rename(old_file_name, new_file_name, source_dir, dest_dir):
    src_file = os.path.join(source_dir, old_file_name)
    shutil.copy(src_file, dest_dir)

    dst_file = os.path.join(dest_dir, old_file_name)
    new_dst_file_name = os.path.join(dest_dir, new_file_name)
    os.rename(dst_file, new_dst_file_name)

if not os.path.exists(path_to_docs):
    os.mkdir(path_to_docs)


lab_folders = sorted(os.walk(path_to_labs), key=lambda data: data[0])[3:]

for (dirpath, dirnames, filenames) in lab_folders:
    print(dirpath)
    dirname = dirpath.split(os.path.sep)[-1]
    print(dirname)
    step = dirname[3:]
    filename = 'instructions.md'
    try:
        copy_rename(filename, f'{step}-{filename}', dirpath, os.path.join(path_to_docs))
    except FileNotFoundError:
        pass


