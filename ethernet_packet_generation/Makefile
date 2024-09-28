# Variables
PYTHON = python
SRC_DIR = src
TEST_DIR = tests
OUTPUT_DIR = output
CONFIG_FILE = config/config.txt

# Default target
all: test

# Set environment variable and run tests
test:
	@echo "Running tests..."
	set PYTHONPATH=$(SRC_DIR) && $(PYTHON) -m unittest discover -s $(TEST_DIR)

# Clean the output directory
clean:
	@echo "Cleaning output directory..."
	del /Q $(OUTPUT_DIR)\*.json
	del /Q /S $(SRC_DIR)\__pycache__
	del /Q /S $(TEST_DIR)\__pycache__

# Run packet generation (example command)
run:
	@echo "Running packet generation..."
	set PYTHONPATH=$(SRC_DIR) && $(PYTHON) $(SRC_DIR)\main.py $(CONFIG_FILE)

.PHONY: all test clean run install
