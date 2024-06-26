# Asynchronous Website Checker
This is a simple Python program that employs asynchronous programming techniques to concurrently check the HTTP status codes of multiple websites. Asynchronous programming allows for efficient utilization of system resources by enabling tasks to execute concurrently without blocking the main execution thread.

## Features
- **Concurrent HTTP Status Checking**: The program utilizes asynchronous programming to simultaneously query multiple websites for their HTTP status codes.
- **Website Health Monitoring**: This tool aids in monitoring the health of websites by determining whether they are up or experiencing connectivity issues.
- **Efficient Resource Utilization**: Asynchronous programming enhances resource efficiency by enabling concurrent execution of tasks without unnecessary blocking, thus optimizing the program's performance.


## Prerequisites
- Python 3.7 or later
- The aiohttp library (install with pip install aiohttp)
- The logger_config module (provided separately)

## Usage
1. Install dependencies: Ensure you have the required Python packages installed. You can install them using pip:
```
pip install -r requirements.txt
```
2. Execute the program: Run the Python script to initiate the concurrent HTTP status checking process:
```
python main.py
```

The program will check the HTTP status codes of three example websites (http://example.com, http://google.com, and http://facebook.com) and log the results using the logger_config module.

## Dependencies
- **asyncio**: This module provides infrastructure for writing single-threaded concurrent code using coroutines, enabling efficient asynchronous I/O operations.
- **aiohttp**: aiohttp is a Python library for asynchronous HTTP client/server framework. It allows for efficient handling of HTTP requests and responses in an asynchronous manner.

## Program Overview
The main.py program uses the following main components:

- **The check_site coroutine**: This function takes an aiohttp.ClientSession object and a URL as input, and attempts to make an HTTP request to the URL using the session. If the request is successful, the function returns a tuple containing the URL and the HTTP status code. If an error occurs, the function logs an error message and returns a tuple containing the URL and None.

- **The main coroutine**: This function creates an aiohttp.ClientSession object and passes it to multiple check_site coroutines running concurrently using the asyncio.gather function. The results of the coroutines are logged using the logger_config module.

The program uses asynchronous programming techniques to perform multiple HTTP requests concurrently, which can improve performance compared to making requests synchronously.

## Error Handling
The program handles HTTP request errors by catching aiohttp.ClientError exceptions raised by the session.get method in the check_site coroutine. If an error occurs, the program logs an error message and returns None as the HTTP status code for that URL. The main coroutine checks for None status codes and logs an error message for those URLs.

## Logging
The program logs messages using the logger_config module, which provides a simple configuration for logging messages to the console and a file. By default, the program logs messages at the INFO level to the console and the site_status.log file in the program directory. The logging level and format can be customized by modifying the logger_config.py file.

## License
This program is licensed under the MIT License. See the LICENSE file for details.