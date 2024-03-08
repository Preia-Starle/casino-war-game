
#change to `python` if python3 is not found
PYTHON=python3

all:start

coverage:
	@printf "Running coverage unittesting and writting results to a html file...\n"
	coverage run -m unittest discover
	coverage html
	@printf "To open it run:\n"
	@printf "Mac -- open -a Google\ Chrome htmlcov/index.html\n"
	@printf "Linux -- firefox htmlcov/index.html\n"

docs:
	pdoc --html --output-dir docs/pdoc *.py

venv:
	$(PYTHON) -m venv .venv
	@printf "Now you have to activate the virual environement.\n"
	@printf "[On Mac/Linux] -- . .venv/bin/activate\n"
	@printf "[On Windows] -- . .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate"

start:
	$(PYTHON) Main.py


clean-docs:
	rm -rf html
	rm -rf docs


clean:
	rm -rf htmlcov
	rm -rf __pycache__

install:
	$(PYTHON) -m pip install -r requirements.txt

