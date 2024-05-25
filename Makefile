clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache

loc:
	find . -name '*.py' | sort | xargs wc -l

test:
	@pytest -rA -vv
