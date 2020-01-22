# pcc
Python connection creator

## Overview
Python script to create TCP connections for testing and validation purposes.

## Usage
```
usage: pcc.py [-h] -dst DESTINATION -dport DESTINATION_PORT [-t TIMEOUT]

Python Connection Creator (pcc) v1.0

required arguments:
  -dst DESTINATION, --destination DESTINATION
                        DNS name or IP address for destination
  -dport DESTINATION_PORT, --destination-port DESTINATION_PORT
                        Port number for destination

optional arguments:
  -t TIMEOUT, --timeout TIMEOUT
                        Username to access the API
```

## Examples
* Successful
  ```
    python pcc.py --destination "www.reuters.com" --destination-port "80"
    ***
    *** Python Connection Creator (pcc) v1.0
    ***
    --- [17:13:37] Attempting a TCP connection with a 10.0 second timeout to www.reuters.com on port 80...
    ... [17:13:37] Connection completed successfully.
  ```
* Bad DNS
  ```
    python pcc.py --destination "www365.reuters.com" --destination-port "80"
    ***
    *** Python Connection Creator (pcc) v1.0
    ***
    --- [17:15:19] Attempting a TCP connection with a 10.0 second timeout to www365.reuters.com on port 80...
    !!! [17:15:20] Error: [Errno 11001] getaddrinfo failed
  ```
* Bad Port
  ```
    python pcc.py --destination "www.reuters.com" --destination-port "8086"
    ***
    *** Python Connection Creator (pcc) v1.0
    ***
    --- [17:16:50] Attempting a TCP connection with a 10.0 second timeout to www.reuters.com on port 8086...
    !!! [17:17:00] Error: timed out
  ```