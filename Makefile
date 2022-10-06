.PHONY: create show convert build view

INPUTS=$(wildcard *.py)
NBS=$(INPUTS:.py=.ipynb)
OUTPUTS=$(NBS:.ipynb=.md)


all: $(NBS) convert build view

create:
	jupytext --set-formats ipynb,py:percent --execute *.py

show:
	@echo $(OUTPUTS)

convert: $(OUTPUTS)

build:
	asciidoctor -v -t index.adoc

view:
	open index.html

%.ipynb: %.py
	jupytext --set-formats ipynb,py:percent --execute $<
	
%.md: %.ipynb
	jupyter nbconvert --to markdown $<

sync-one-file:
	jupytext --set-formats ipynb,py:percent Zip.ipynb
