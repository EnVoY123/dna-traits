TARGETS := dna_traits/_dna_traits.so

all: $(TARGETS)

dna_traits/_dna_traits.so: src/_dna_traits.so
	cp -f $^ $@

src/_dna_traits.so:
	$(MAKE) -C src _dna_traits.so

check: all
	PYTHONPATH=. python test/test_dna_traits.py

bench: all
	PYTHONPATH=. python test/bench.py

repl: all
	PYTHONPATH=. python -i -c 'import dna_traits; genome = dna_traits.parse("../genomes/genome.txt")'

clean:
	$(MAKE) -C src clean
	rm -f $(TARGETS)
	find . \( -name '*.pyc' -or -name '*.pyo' \) -exec rm {} \;
