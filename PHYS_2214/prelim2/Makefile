TEXFILE = prelim2

$(TEXFILE).pdf: plots $(TEXFILE).tex
	knuth build --ipython $(TEXFILE).tex

.PHONY: clean
clean:
	knuth clean
	-rm -f *.pgf

.PHONY: tidy
tidy:
	knuth clean --keep-pdf
	-rm -f *.pgf

.PHONY: sanitize
sanitize:
	knuth sanitize
	-rm -f *.pgf

.PHONY: plots
plots: beats.pgf

beats.pgf: beats.py
	python $<

view: $(TEXFILE).pdf
	if command -v evince; then evince $<; \
	elif command -v open; then open $<; \
	else echo "ERROR: unable to open pdf. Try installing evince"; fi
