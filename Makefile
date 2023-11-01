.PHONY: test
test:
	rm -rf ./test-gen
	mkdir test-gen
	cd ./test-gen && poetry run cookiecutter --no-input ${PWD}
