
TEXFILE = p1

$(TEXFILE).pdf: $(TEXFILE).tex
	knuth build $<

.PHONY: clean
clean:
	knuth clean

view: $(TEXFILE).pdf
	if command -v evince; then evince $<; \
	elif command -v open; then open $<; \
	else echo "ERROR: unable to open pdf. Try installing evince"; fi

