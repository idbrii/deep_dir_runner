MODULE = deepdir.py
MAIN = main.py
ARGS = ml

.PHONY:	run test syntax clean

run:
	python $(MAIN) $(ARGS)

test:
	python $(MODULE)

syntax:
	python -c "import py_compile,sys; sys.stderr=sys.stdout; py_compile.compile(r'$(MODULE)')"

tags: *.py
	ctags -R .

clean:
	-rm tags *.pyc
