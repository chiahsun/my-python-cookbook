.PHONY: create echo convert build view clean

INPUTS=$(wildcard *.py)
NBS=$(INPUTS:.py=.ipynb)
OUTPUTS=$(NBS:.ipynb=.md)

all: create convert build view

create: $(NBS)

echo:
	@echo $(INPUTS)
	@echo $(NBS)
	@echo $(OUTPUTS)

convert: $(OUTPUTS)

build:
	asciidoctor -v -t index.adoc

view:
	open index.html

clean:
	rm -f $(NBS) $(OUTPUTS)

%.ipynb: %.py
	jupytext --set-formats ipynb,py:percent --execute $<
	
%.md: %.ipynb
	jupyter nbconvert --to markdown $<

# Run this manually for either only ipynb or py exists
sync:
	jupytext --set-formats ipynb,py:percent --sync Sample.ipynb
