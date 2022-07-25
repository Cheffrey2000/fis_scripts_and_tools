# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import argparse
import os

parser = argparse.ArgumentParser(description='A course number, and fix the LaTeX rendering in the file itself')

#parser.add_argument('file_location', help='Provide the location of the repo to fix')

parser.add_argument('course_number', help='Provide the canvas course number')

args = parser.parse_args()

os.system('git checkout -b canvas')

course_num = args.course_number
for character in ('$$', '$'):
    file_name = 'README.md'
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    sep = character
    sep_clean = sep + " "
    data = data.replace(sep_clean, sep)

    if r"\begin{align}" in data:
        data.replace(r'\begin{align}', '&')

    if r"\end{align}" in data:
        data.replace(r'\end{align}', '&')
    data_split = data.split(sep)
    special_characters = ["\backslash", "\subset", "\subseteq", "\cap", "\cup"]
    for i in range(len(data_split)):
        if i %2 !=0:
            for item in special_characters:
                data_split[i] = data_split[i].replace(item,(' '+item))
            if "prod" in data_split[i]:
                data_split[i] = data_split[i].replace('prod', 'displaystyle\prod')
            
            if "sum" in data_split[i]:
                data_split[i] = data_split[i].replace('prod', 'displaystyle\sum')
            
            if "+" in data_split[i]:
                data_split[i] = data_split[i].replace('+', '%2b')
                
            data_split[i] = ' <img src="https://render.githubusercontent.com/render/math?math='+data_split[i]+'"> '


    # %%
    final = ''.join(data_split)


    # %%
    f = open(file_name, 'w')
    f.write(final)
    f.close()

add = 'git add .'
os.system(add)
commit = "git commit -m 'Corrected LaTeX rendering on canvas branch with latex-to-canvas script'"
os.system(commit)
push = 'git push origin canvas'
os.system(push)

canvas_command = 'github-to-canvas -a --course '+str(course_num)+' -slr -b canvas'
  
os.system(canvas_command)


# %%



# %%


