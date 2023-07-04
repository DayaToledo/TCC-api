env:
	pip freeze > requirements.txt
	python --version
	python -m venv tcc
	source tcc/Scripts/activate

	pip install --upgrade pip
	python -m pip install --upgrade pip

	pip install -r requirements.txt
	python src/scripts/train.py LogisticRegression
	python src/scripts/train.py KNeighborsClassifier
	python src/scripts/train.py GaussianNB
	python src/scripts/train.py DecisionTreeClassifier
	python src/scripts/train.py AdaBoostClassifier
	python src/scripts/train.py SVC
	python src/scripts/train_LogisticRegression_responsible.py

dev:
	uvicorn --port 8080 src.api.main:app --reload

run:
	uvicorn --port 8080 src.api.main:app
