build:
	python3 -m build
	python3 -m twine upload --repository testpypi dist/*

install:
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps markdown-writer-atidyshirt

clean:
	-rm -rf dist
	-rm -rf src/markdown_writer_atidyshirt.egg-info

