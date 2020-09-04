.PHONY: archive test list clean


archive: 
	@make clean ; tar czf p0.tar.gz *

clean:
	@rm -R *.tar.gz *.pyc __pycache__ *~* *#* */*~* */*#* .DS_Store || true
