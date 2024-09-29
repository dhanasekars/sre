format:
	#format code
	black .

lint:
	#flake8 or #pylint
	pylint -j 4 --rcfile=pylint.rc

git:
	#git push
	@git add .
	@git commit -m "$(MSG)"
	@git push origin working-tree
