# coding: utf-8
import os
import shutil
import subprocess
'''
Little helper to do pre publish tasks.
'''

DOCUMENTS = 'content/documentation'
index = []

def create_index(documentation=DOCUMENTS):
    contents = os.path.join(documentation, 'contents.lr')
    # Clean the index first.
    subprocess.call(['git', 'checkout', contents])
    # Then write the index
    for el in index:
        with open(contents, 'a') as cont:
            cont.write('- [%s](%s)\n' % (el[2:-3], el[2:-3]))


def clean_doc(documentation=DOCUMENTS):
    for root, dirs, files in os.walk(documentation, topdown=False):
        for name in dirs:
            shutil.rmtree(os.path.join(root, name))

def md2lektor(element, documentation=DOCUMENTS):
    # first create the named content folder
    new_content = os.path.join(documentation, element[2:-3])
    if not os.path.isdir(new_content):
        os.mkdir(new_content)
    new_contents = os.path.join(new_content, 'contents.lr')
    contents = os.path.join(documentation, 'contents.lr')
    with open(new_contents, 'a') as ncf:
        ncf.write('_model: documentation\n---\n')
        ncf.write(open(
            contents,
            'r').read())
        ncf.write(open(element, 'r').read())
    index.append(element)

def main():
    clean_doc()
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if root == '.' and name.endswith('.md'):
                fname_doc = os.path.join(root, name)
                md2lektor(fname_doc)
    create_index()
    return True

if __name__ == '__main__':
    main()
