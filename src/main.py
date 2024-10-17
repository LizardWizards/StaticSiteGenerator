import util_blocks
import os
import shutil

public_dir = "./public"
static_dir = "./static"
def main():
    copy_static_to_public()
    generate_pages_recursive("./content", "./template.html", "./public")

# crawls every entry in the content directory and generates a new .html file for each markdown file found
# writes generated pages to the pulic directory
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_entries = os.listdir(dir_path_content)

    for entry in dir_entries:
        from_path = os.path.join(dir_path_content, entry)
        to_path = os.path.join(dest_dir_path, entry)
        if(os.path.isdir(from_path)):
            new_dir = os.path.join(dest_dir_path, entry)
            
            os.mkdir(new_dir)

            dir_entries = os.listdir(from_path)
            # for each thing in this directory, copy_files(thing)
            for entry in dir_entries:
                generate_pages_recursive(from_path, template_path, to_path)

        # if this is a file, copy it
        if(os.path.isfile(from_path)):
            html_version = entry[:-2]
            html_version += "html"
            new_file = os.path.join(dest_dir_path, html_version)
            generate_page(from_path, template_path, new_file)


# pulls the h1 header from the markdown file and reurns it
def extract_title(markdown):
    docNode = util_blocks.markdown_to_html_node(markdown)
    for node in docNode.children:
        if node.tag == "h1":
            return node.value
    
    raise ModuleNotFoundError("Heading not found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_contents = ""
    template_contents = ""
    with open(from_path) as markdown:
        markdown_contents = markdown.read()
        markdown.close()

    with open(template_path) as template:
        template_contents = template.read()
        template.close()

    docNode = util_blocks.markdown_to_html_node(str(markdown_contents))
    docHTML = docNode.to_html()
    header = extract_title(markdown_contents)

    finalFile = template_contents.replace("{{ Title }}", header)
    finalFile = finalFile.replace("{{ Content }}", str(docHTML))

    with open(dest_path, "w") as f:
        # File is created or overwritten if it exists
        f.write(finalFile)

    return finalFile


# copies files from static to public
def copy_static_to_public():
    # delete contents in destination directory
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

    dir_entries = os.listdir(static_dir)
    # for each thing in this directory, copy_files(thing)
    for entry in dir_entries:
        copy_files(entry, public_dir, static_dir)


# recursively copies files from source to public directory
def copy_files(entry, to_dir, form_dir):
    # if this is a directory, make one w same name

    from_path = os.path.join(form_dir, entry)
    to_path = os.path.join(to_dir, entry)

    if(os.path.isdir(from_path)):
        new_dir = os.path.join(to_dir, entry)
        os.mkdir(new_dir)
        dir_entries = os.listdir(from_path)
        # for each thing in this directory, copy_files(thing)
        for entry in dir_entries:
            copy_files(entry, to_path, from_path)
    # if this is a file, copy it
    if(os.path.isfile(from_path)):
        new_file = os.path.join(to_dir, entry)
        shutil.copyfile(from_path, new_file)

main()