
.PHONY: build view watch

build:
	asciidoctor -a stylesheet=dark.css -a highlightjsdir=highlight -v -t index.adoc
	# asciidoctor -v -t index.adoc

view:
	open index.html -a Safari
	
watch:
	./watch_build.sh

download-dark-css:
	curl -LO https://github.com/darshandsoni/asciidoctor-skins/raw/gh-pages/css/dark.css