env:
	pip freeze > requirements.txt
	python --version
	python -m venv tcc
	source tcc/Scripts/activate
	pip install --upgrade pip
	pip install -r requirements.txt

dev:
	uvicorn --port 8080 src.api.main:app --reload

run:
	uvicorn --port 8080 src.api.main:app
