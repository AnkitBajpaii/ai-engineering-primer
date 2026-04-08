.DEFAULT_GOAL := help

PYTHON := python
VENV := .venv
PIP := $(VENV)/Scripts/pip

# ── Help ──────────────────────────────────────────────────────────────────────

.PHONY: help
help:
	@echo ""
	@echo "AI Engineering Playground"
	@echo ""
	@echo "  make setup      Create virtual environment, install dependencies, copy .env"
	@echo "  make run n=1    Run a specific script, e.g. make run n=5"
	@echo "  make list       List all available scripts"
	@echo "  make clean      Remove virtual environment and cache files"
	@echo ""

# ── Setup ─────────────────────────────────────────────────────────────────────

.PHONY: setup
setup: $(VENV)/Scripts/activate .env
	@echo ""
	@echo "Setup complete. Open .env and add your OPENAI_API_KEY, then run: make run n=1"
	@echo ""

$(VENV)/Scripts/activate:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.env:
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Created .env from .env.example — add your OPENAI_API_KEY before running scripts."; \
	fi

# ── Run ───────────────────────────────────────────────────────────────────────

.PHONY: run
run:
ifndef n
	@echo "Usage: make run n=<script number>  e.g. make run n=1"
else
	@script=$$(find . -path './.venv' -prune -o -name "$(n).*.py" -print | head -1); \
	if [ -z "$$script" ]; then \
		echo "No script found for number $(n). Run 'make list' to see all scripts."; \
	else \
		echo "Running $$script ..."; \
		$(VENV)/Scripts/python $$script; \
	fi
endif

# ── List ──────────────────────────────────────────────────────────────────────

.PHONY: list
list:
	@echo ""
	@echo "Available scripts:"
	@find . -path './.venv' -prune -o -name "[0-9]*.py" -print | sort -t/ -k3 -V | while read f; do \
		concept=$$(grep "## Concept" $$f | sed 's/.*Concept *: *//'); \
		printf "  %-55s %s\n" "$$f" "$$concept"; \
	done
	@echo ""

# ── Clean ─────────────────────────────────────────────────────────────────────

.PHONY: clean
clean:
	rm -rf $(VENV) __pycache__ .pytest_cache .mypy_cache .ruff_cache
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
