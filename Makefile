.PHONY: format lint test check

format:
	black src/ tests/
	isort src/ tests/

lint:
	flake8 src/ tests/

test:
	poetry run pytest tests/ --cov=twcal --cov-report=term-missing -v

check: format lint test
