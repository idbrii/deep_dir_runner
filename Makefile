MODULE = deepdir.py
MAIN = main.py
ARGS = testdata/ml

.PHONY:	run test syntax clean

run:
	python $(MAIN) $(ARGS)

test:
	python $(MODULE)
	python action.py
	python trigger.py
	python filetype.py

syntax:
	python -c "import py_compile,sys; sys.stderr=sys.stdout; py_compile.compile(r'$(MODULE)')"

tags: *.py
	ctags -R .

clean:
	-rm tags *.pyc
