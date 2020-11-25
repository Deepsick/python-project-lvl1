install: 
	poetry install

brain-games: 
	poetry run brain-games

build: 
	poetry build

package-install: 
	pip3 install --user dist/*.whl

make lint:
	poetry run flake8 brain_games