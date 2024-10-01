MSG ?= Daily checkin

format:
	#format code
	black .

lint:
	#flake8 or #pylint
	@pylint -j 4 --rcfile=pylint.rc src/

git:
	#git push
	@git add .
	@git commit -m "$(MSG)"
	@git push

startapp:
	python -m api.src.main

dcup:
	docker-compose up --build
