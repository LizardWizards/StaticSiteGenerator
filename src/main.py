from textnode import TextNode
from parentnode import ParentNode
from leafnode import LeafNode
import util_inline
import util_blocks
import os
import shutil

public_dir = "./public"
static_dir = "./static"
def main():
    copy_static_to_public()
    

# copies files from static to public
def copy_static_to_public():
    # delete contents in destination directory
    if os.path.exists(public_dir):
        print("removing")
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

    dir_entries = os.listdir(static_dir)
    # for each thing in this directory, copy_files(thing)
    for entry in dir_entries:
        copy_files(entry, public_dir, static_dir)


# recursively copies files from source to public directory
def copy_files(entry, to_dir, form_dir):
    # if this is a directory, make one w same name
    print(f"---Going to copy {entry} to {to_dir}---")

    from_path = os.path.join(form_dir, entry)
    to_path = os.path.join(to_dir, entry)
    print(f"From path: {from_path}")
    print(f"To path: {to_path}")

    if(os.path.isdir(from_path)):
        print("It's a dir")
        new_dir = os.path.join(to_dir, entry)
        print("New dir:")
        print(new_dir)
        os.mkdir(new_dir)
        dir_entries = os.listdir(from_path)
        # for each thing in this directory, copy_files(thing)
        for entry in dir_entries:
            copy_files(entry, to_path, from_path)
    # if this is a file, copy it
    if(os.path.isfile(from_path)):
        print("It's a file")
        new_file = os.path.join(to_dir, entry)
        print(f"New path: {new_file}")
        shutil.copyfile(from_path, new_file)


main()