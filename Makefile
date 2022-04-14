lint:
	poetry run flake8 gendiff file1.json file2.json
lrun:
	potry run gendiff scripts.file1.json scripts.file2.json
run:
	poetry run gendiff file1.json file2.json
yrun:
	poetry run gendiff f1.yml f2.yml

