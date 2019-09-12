TALK = matplotlib-talk

all: pdf view clean

pdf:
	TEXMFHOME=texmf pdflatex $(TALK).tex
	TEXMFHOME=texmf pdflatex $(TALK).tex

view:
	xdg-open "$(TALK).pdf" 2> /dev/null || \
	open -a firefox "$(TALK).pdf" 2> /dev/null || \
	open "$(TALK).pdf" 2> /dev/null || \
	echo Cannot find a program to open file.

deps:
	rm -rf texmf texmfvar ~/Library/texlive
	TEXMFHOME=texmf tlmgr init-usertree
	TEXMFHOME=texmf tlmgr --usermode install fontawesome textpos || :
	TEXMFHOME=texmf TEXMFVAR=texmf updmap-user

venv: FORCE
	rm -rf ~/.venv/$(TALK)
	python3 -m venv ~/.venv/$(TALK)
	echo . ~/.venv/$(TALK)/bin/activate > venv
	. ./venv && pip install matplotlib pylama pylama-pylint

lint:
	. ./venv && isort --quiet --diff
	. ./venv && pylama -l pycodestyle,pyflakes,mccabe,pylint,isort \
	                   -i C0103,C0111

ex%:
	T=$@; . ./venv && python3 examples/$${T#ex}*.py
	xdg-open out.png 2> /dev/null || \
	open out.png 2> /dev/null || \
	echo Cannot find a program to open file.

heart:
	for i in 0 2 3 4 5 6 7 8; do \
	    . ./venv && python3 examples/heart$$i.py && \
	    mv out.png img/heart$$i.png; done

clean:
	rm -rf *.aux *.log *.nav *.out *.snm *.toc *.vrb
	find . -name ".DS_Store" -exec rm {} +

FORCE:
