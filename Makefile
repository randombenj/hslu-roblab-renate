.PHONY: doc

doc:
	PYTHONPATH=$$PYTHONPATH:. python renate/core.py doc/fsm.png
