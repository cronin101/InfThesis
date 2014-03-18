kicker -e '(pdflatex thesis.tex) && (bibtex thesis) && (pdflatex thesis.tex) && (texcount thesis.tex -inc -merge -brief)' -c
