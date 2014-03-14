chruby 2.2
kicker -e '(pdflatex thesis.tex) && (bibtex thesis) && (pdflatex thesis.tex)' -c
