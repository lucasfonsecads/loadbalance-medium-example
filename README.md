# Python Load Balancer Example

## Overview

This project demonstrates a simple load balancer using Python's built-in libraries. The load balancer uses the Round Robin algorithm to distribute client requests across multiple backend servers. It includes a load balancer, two backend servers, and a test client.

## Author

[Lucas Fonseca](https://github.com/lucasfonsecads/loadbalance-medium-example)

## Directory Structure

.
├── Makefile
├── README.md
├── client
│   └── client.py
├── load_balancer
│   └── load_balancer.py
├── requirements.txt
├── server1
│   └── server1.py
└── server2
    └── server2.py


## Requirements

- Python 3.6 or higher
- `requests` library

## Setup Instructions

1. **Clone the repository:**

    - `git clone https://github.com/lucasfonsecads/loadbalance-medium-example`
    
    - `cd load-balancer-example`
    

2. **Create and activate the virtual environment, and install dependencies:**

    ```bash
    make install
    ```

## Running the Components

### Run Backend Servers

Open two separate terminal windows and run each server:

```bash
make server1
```

```bash
make server2
```

### Run Load Balancer

In a third terminal window, run the load balancer:

```bash
make load_balancer
```

### Run Test Client

In a fourth terminal window, run the test client to verify the load balancer:

```bash
make test
``` 

### Run Everything Together

To run everything together in the same terminal:

```bash
make run_all
```

⁠This command will start both backend servers, the load balancer, and the test client sequentially, all in the same terminal.

## Clean Up

To clean the virtual environment:

```bash
make clean
```

## Explanation

- **Load Balancer**: Distributes client requests using the Round Robin algorithm.
- **Backend Servers**: Simple HTTP servers that respond with different messages.
- **Test Client**: Sends requests to the load balancer to verify that requests are being distributed correctly.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

```
This ⁠ README.md ⁠ file provides an overview of the project, setup instructions, and commands to run the servers, load balancer, and client. It also includes cleanup instructions and information on contributing and licensing.
```