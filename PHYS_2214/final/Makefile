TEXFILE = final

$(TEXFILE).pdf: $(TEXFILE).tex
	knuth build  $<

.PHONY: clean
clean:
	knuth clean

.PHONY: tidy
tidy:
	knuth clean --keep-pdf

.PHONY: sanitize
sanitize:
	knuth sanitize

view: $(TEXFILE).pdf
	if command -v evince; then evince $<; \
	elif command -v open; then open $<; \
	else echo "ERROR: unable to open pdf. Try installing evince"; fi
