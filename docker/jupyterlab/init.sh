cp .jalinebreak.sty ~/texmf/tex/latex/local/jalinebreak.sty
cp .base.tplx /usr/local/lib/python3.8/dist-packages/nbconvert/templates/latex/base.tplx

jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token=''