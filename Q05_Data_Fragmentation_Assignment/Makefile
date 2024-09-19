# Define the compiler and flags
CXX = g++
CXXFLAGS = -Iinclude -Wall -g

# Define directories
SRC_DIR = src
INCLUDE_DIR = include
BUILD_DIR = build
TEST_DIR = test

# Define source files and object files
SRCS = $(wildcard $(SRC_DIR)/*.cpp)
SRCS_TEST = $(wildcard $(TEST_DIR)/*.cpp)
OBJS = $(patsubst $(SRC_DIR)/%.cpp, $(BUILD_DIR)/%.o, $(filter-out $(SRC_DIR)/main.cpp, $(SRCS)))

# Define the executables
EXEC = $(BUILD_DIR)/main
TEST_EXEC = $(BUILD_DIR)/test_program

# Detect platform (Windows or Unix)
ifeq ($(OS),Windows_NT)
    MKDIR = if not exist $(BUILD_DIR) mkdir $(BUILD_DIR)
    RMDIR = if exist $(BUILD_DIR) rmdir /s /q $(BUILD_DIR)
else
    MKDIR = mkdir -p $(BUILD_DIR)
    RMDIR = rm -rf $(BUILD_DIR)
endif

# Default target to build the executable
all: $(EXEC)

# Rule to build the executable
$(EXEC): $(OBJS) $(SRC_DIR)/main.cpp
	$(MKDIR)
	$(CXX) $(CXXFLAGS) $(OBJS) $(SRC_DIR)/main.cpp -o $(EXEC)

# Rule to compile source files into object files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(MKDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Rule to compile test program
$(BUILD_DIR)/test_program: $(OBJS) $(TEST_DIR)/test_program.cpp
	$(MKDIR)
	$(CXX) $(CXXFLAGS) $(OBJS) $(TEST_DIR)/test_program.cpp -o $(TEST_EXEC)

# Clean target to remove compiled files
clean:
	$(RMDIR)

# Run target to execute the program with command-line arguments
run: $(EXEC)
	$(EXEC) $(ARGS)

# Test target to compile and run the test program
test: $(BUILD_DIR)/test_program
	$(TEST_EXEC) $(TEST_ARGS)

# PHONY prevents make from confusing targets with filenames
.PHONY: all clean run test
