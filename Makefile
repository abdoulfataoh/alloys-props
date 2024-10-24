help:
	@echo "make help            	- Prints this help message"
	@echo "make flake8		- Test flake8"
	@echo "make mypy		- Test mypy"
	@echo "make pytest		- Test with pytest"


flake8:
	flake8 alloys_props


mypy:
	mypy alloys_props


pytest:
	pytest tests
