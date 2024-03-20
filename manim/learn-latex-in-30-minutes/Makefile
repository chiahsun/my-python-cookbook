

OUTPUTS=$(patsubst %.tex,%.pdf,$(wildcard *.tex))

all: build

build: $(OUTPUTS)

%.pdf: %.tex
	pdflatex $<

watch:
	./watch_build.sh

clean:
	rm -rf *.aux *.pdf *.log
