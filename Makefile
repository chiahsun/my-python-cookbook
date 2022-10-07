.PHONY: create show convert build view clean

INPUTS=$(wildcard *.py)
NBS=$(INPUTS:.py=.ipynb)
OUTPUTS=$(NBS:.ipynb=.md)


all: create convert build view

create: $(NBS)

show:
	@echo $(OUTPUTS)

convert: $(OUTPUTS)

build:
	asciidoctor -v -t index.adoc

view:
	open index.html

clean:
	rm *.md *.ipynb

%.ipynb: %.py
	jupytext --set-formats ipynb,py:percent --execute $<
	
%.md: %.ipynb
	jupyter nbconvert --to markdown $<

