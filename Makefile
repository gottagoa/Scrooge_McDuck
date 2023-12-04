.PHONY: migrate
migrate:
	@echo "Migrating database..."
	python3 manage.py migrate --noinput


.PHONY: run
run: migrate 
	@echo "Running server..."
	python3 manage.py runserver 0.0.0.0:8000