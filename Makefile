# Define variables
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# List of Python files for servers and client
SERVER1 = server1/server1.py
SERVER2 = server2/server2.py
LOAD_BALANCER = load_balancer/load_balancer.py
CLIENT = client/client.py

# Default target: create virtual environment and install dependencies
all: install

# Create virtual environment
$(VENV_DIR)/bin/activate: requirements.txt
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	touch $(VENV_DIR)/bin/activate

# Install dependencies
install: $(VENV_DIR)/bin/activate

# Run server 1
server1: $(VENV_DIR)/bin/activate $(SERVER1)
	$(PYTHON) $(SERVER1)

# Run server 2
server2: $(VENV_DIR)/bin/activate $(SERVER2)
	$(PYTHON) $(SERVER2)

# Run load balancer
load_balancer: $(VENV_DIR)/bin/activate $(LOAD_BALANCER)
	$(PYTHON) $(LOAD_BALANCER)

# Run test client
test: $(VENV_DIR)/bin/activate $(CLIENT)
	$(PYTHON) $(CLIENT)

# Run everything together
run_all: $(VENV_DIR)/bin/activate
	$(PYTHON) server1/server1.py &
	$(PYTHON) server2/server2.py &
	sleep 2  # Give servers time to start
	$(PYTHON) load_balancer/load_balancer.py &
	sleep 2  # Give load balancer time to start
	$(PYTHON) client/client.py

# Clean virtual environment
clean:
	rm -rf $(VENV_DIR)

.PHONY: all install server1 server2 load_balancer test run_all clean