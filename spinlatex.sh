kicker -e '(xelatex thesis.tex) && (bibtex thesis) && (xelatex thesis.tex) && (texcount thesis.tex -inc -merge -brief)' -c
