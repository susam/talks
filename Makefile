# Setup commit history that matches the dates of the presentations.
reset:
	rm -rf .git
	git init
	git config --global user.name "Susam Pal"
	git config --global user.email susam@susam.in
	git remote add origin https://github.com/susam/talks.git
	#
	git add Makefile .gitignore
	git add 2006-09-20-owasp-top-ten-talk
	make commit D="2006-09-20 10:00:00 +0530" M="Add OWASP Top Ten talk"
	#
	git add 2014-10-03-rsa-netwitness-webinar
	make commit D="2014-10-03 19:30:00 +0530" M="Add RSA NetWitness Log Decoder webinar"
	#
	git add 2018-09-15-pycon-uk-pylava-talk
	make commit D="2018-09-15 17:30:00 +0100" M="Add PyCon UK Pylava talk"
	#
	git add README.md
	git commit -m "Add README.md with list of talks and presentations"
	#
	git log --format=fuller
	@echo
	@echo Press Enter to push the commit history.
	@echo Press Ctrl + C to cancel.
	@echo
	@read
	git push -f origin master

commit:
	GIT_COMMITTER_DATE="$(D)" GIT_AUTHOR_DATE="$(D)" git commit -m "$(M)"
