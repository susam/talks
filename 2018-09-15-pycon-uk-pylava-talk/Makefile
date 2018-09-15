TALK = pylava-talk

all: slides clean view

slides:
	TEXMFHOME=texmf pdflatex $(TALK).tex
	TEXMFHOME=texmf pdflatex $(TALK).tex

view:
	if command -v xdg-open > /dev/null; then \
	    xdg-open "$(TALK).pdf"; \
	elif command -v open > /dev/null; then \
	    open "$(TALK).pdf"; \
	else \
	    echo Cannot find xdg-open or open.; \
	fi

deps:
	rm -rf texmf texmfvar ~/Library/texlive
	TEXMFHOME=texmf tlmgr init-usertree
	TEXMFHOME=texmf tlmgr --usermode install fontawesome || :
	TEXMFHOME=texmf TEXMFVAR=texmf updmap-user

clear:
	rm -rf *.pdf

clean:
	rm -rf *.aux *.log *.nav *.out *.snm *.toc *.vrb
	find . -name ".DS_Store" -exec rm {} +
