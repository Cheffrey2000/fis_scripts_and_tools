"""
This script is designed to take in a local directory of a cloned lesson repo and the lesson number
It will then:
    -checkout the canvas branch
    -fix the LaTeX rendering in the README.md
    -and update the lesson on canvas with the provided course number
Example: bash latex-to-canvas.sh /dsc-bayes-theorem 343  - this will change directory into /dsc-bayes-theorem and pass 343 as the course id
Requires github-to-canvas gem and latex-to-canvas.py script
"""


if [ $# -eq 0 ] || [ $# -eq 1 ]
  then
    echo "Three arguments required - the folder name and the canvas course id"
    echo "Example: bash latex-to-canvas.sh /dsc-bayes-theorem 343"
    exit 1
fi



  
cd $PWD/$1
git checkout -b canvas

python ~/latex-to-canvas.py ~/$1/README.md

git add .
git commit -m 'Corrected LaTeX rendering on canvas branch with latex-to-canvas script'

  
github-to-canvas -a --course $2 -lr -b canvas

# Avoid limits with sleep for large amounts of repos
sleep 5;
done



