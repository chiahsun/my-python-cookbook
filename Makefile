.PHONY: build view convert

INPUTS=$(wildcard *.ipynb)

OUTPUTS=$(INPUTS:.ipynb=.md)


all: convert build view

show:
	@echo $(INPUTS)
	@echo $(OUTPUTS)

convert: $(OUTPUTS)

build:
	asciidoctor -v -t index.adoc

view:
	open index.html

%.xml: %.adoc
	asciidoctor -b docbook $<
	
%.md: %.ipynb
	jupyter nbconvert --to markdown $<

sync-one-file:
	jupytext --set-formats ipynb,py:percent Zip.ipynb
