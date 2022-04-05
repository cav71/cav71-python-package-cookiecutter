BUILDDIR=build


help:
	@echo "make {init|build|clean}"

init:
	rm -rf $(BUILDDIR)
	cookiecutter -o $(BUILDDIR) .

build:
	cookiecutter -f --replay -o $(BUILDDIR) .
	tree -a $(BUILDDIR)

clean:
	rm -rf $(BUILDDIR) && mkdir -p $(BUILDDIR)


.PHONY: build
