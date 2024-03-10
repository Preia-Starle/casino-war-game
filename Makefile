#change to `python` if python3 is not found
PYTHON ?= python3 

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

all:start

coverage:
	@$(call MESSAGE,$@)
	@printf "Running coverage unittesting and writting results to a html file...\n"
	coverage run -m unittest discover
	coverage html
	@printf "To open it run:\n"
	@printf "Mac -- open -a Google\ Chrome htmlcov/index.html\n"
	@printf "Linux -- firefox htmlcov/index.html\n"


venv:
	@$(call MESSAGE,$@)
	$(PYTHON) -m venv .venv
	@printf "Now you have to activate the virual environement.\n"
	@printf "[On Mac/Linux] -- . .venv/bin/activate\n"
	@printf "[On Windows] -- . .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate"

start:
	$(PYTHON) Main.py


clean-docs:
	@$(call MESSAGE,$@)
	rm -rf html
	rm -rf doc


clean:
	@$(call MESSAGE,$@)
	rm -rf htmlcov
	rm -rf __pycache__
	rm GameMechanics/scores.bin


install:
	@$(call MESSAGE,$@)
	$(PYTHON) -m pip install -r requirements.txt


.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	$(PYTHON) -m pydoc -w GameMechanics/*.py CardMechanics/*.py Players/*.py
	install -d doc/pydoc
	mv *.html doc/pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc --html --output-dir doc/html --force GameMechanics/*.py CardMechanics/*.py Players/*.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse GameMechanics/*.py CardMechanics/*.py Players/*.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot

docs:
	make pydoc
	make pdoc
	make pyreverse


pylint:
	@$(call MESSAGE,$@)
	-pylint GameMechanics/*.py CardMechanics/*.py Players/*.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint
