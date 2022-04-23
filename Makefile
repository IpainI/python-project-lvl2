lint:
	poetry run flake8 gendiff file1.json file2.json
complex:
	poetry run gendiff file1.json file2.json
simple:
	poetry run gendiff short_file1.json short_file2.json
json_complex:
	poetry run gendiff -f json file1.json file2.json
json_simple:
	poetry run gendiff -f json short_file1.yml short_file2.yml
plain_complex:
	poetry run gendiff -f plain file1.json file2.json
plain_simple:
	poetry run gendiff -f plain short_file1.yml short_file2.yml
