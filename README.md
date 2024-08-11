# Web Reconnaissance Tools

This repository contains a collection of Python-based tools designed for web reconnaissance. These tools assist in discovering directories, subdomains, crawling websites, and detecting common web vulnerabilities.

## Tools Overview

1. **dirbuster.py**: A multi-threaded directory brute-forcing tool.
2. **subdomain_finder.py**: A subdomain enumeration tool with multi-threaded support.
3. **web_crawler.py**: A web crawler to map out the structure of a target domain.
4. **web_vuln_scanner.py**: A vulnerability scanner for SQL Injection and XSS attacks.

## Installation

1. **Clone the repository**
   
   ```
   git clone https://github.com/JayGaba/Web-Reconnaissance-Tools.git
   ```
   
3. **Navigate to the project directory**

    ```
    cd Web-Reconnaissance-Tools
    ```

3. **Install the required dependencies**

    To install the required dependencies, use the following command:
    ```
    pip install -r requirements.txt
    ```
## Usage

### dirbuster.py
Usage: 

```
python dirbuster.py <host> <threads> [<extension>]
```

- `<host>`: The target host URL.
- `<threads>`: The number of threads to use for scanning.
- `<extension>`: Optional file extension to append to directory names.

### subdomain_finder.py
Usage: 

```
python subdomain_finder.py <host> <threads>
```

- `<host>`: The target domain to find subdomains for.
- `<threads>`: The number of threads to use for subdomain enumeration.

### web_crawler.py
Usage: 

```
python web_crawler.py <domain>
```
- `<domain>`: The domain to crawl and map.

### web_vuln_scanner.py
Usage: 

```
python web_vuln_scanner.py <domain>
```

- `<domain>`: The domain to scan for SQL Injection and XSS vulnerabilities.

## Future Scope

### dirbuster.py
- **Custom Wordlists**: Integrate functionality to dynamically select and use different wordlists.
- **Advanced Detection**: Implement detection for more status codes and advanced error handling.
- **Performance Enhancements**: Optimize thread management and request handling for faster scans.

### subdomain_finder.py
- **DNS Query Support**: Add support for DNS-based enumeration methods to enhance subdomain discovery.
- **API Integrations**: Integrate with external services for more comprehensive subdomain enumeration.
- **Rate Limiting**: Implement rate limiting to avoid hitting API request limits or getting blocked.

### web_crawler.py
- **Depth Control**: Add functionality to control the depth of crawling.
- **Link Filtering**: Implement filters to exclude specific types of links or domains.
- **Concurrency**: Optimize crawling performance with asynchronous requests or parallel processing.

### web_vuln_scanner.py
- **Enhanced Payloads**: Expand payload lists for more comprehensive SQL Injection and XSS testing.
- **Vulnerability Reporting**: Generate detailed reports with evidence for detected vulnerabilities.
- **Form Handling**: Improve form handling to support more complex scenarios and form types.


