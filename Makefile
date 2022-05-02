lint:
	poetry run flake8 gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json
complex:
	poetry run gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json
simple:
	poetry run gendiff ./tests/fixtures/short_file1.json ./tests/fixtures/short_file2.json
json_complex:
	poetry run gendiff -f json ./tests/fixtures/file1.json ./tests/fixtures/file2.json
json_simple:
	poetry run gendiff -f json ./tests/fixtures/short_file1.yml ./tests/fixtures/short_file2.yml
plain_complex:
	poetry run gendiff -f plain ./tests/fixtures/file1.json ./tests/fixtures/file2.json
plain_simple:
	poetry run gendiff -f plain ./tests/fixtures/short_file1.yml ./tests/fixtures/short_file2.yml
