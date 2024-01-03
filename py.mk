
# https://stackoverflow.com/questions/2483182/recursive-wildcards-in-gnu-make
PYC=python
PY_FILES=$(shell find . -type f -name '*.py')
LOG_FILES=$(patsubst %.py, %.py.log, $(PY_FILES))

echo:
	@echo $(PY_FILES)
	@echo $(LOG_FILES)

compile: $(LOG_FILES)

%.py.log: %.py
	$(PYC) $< > $@

clean:
	rm -f $(LOG_FILES)
