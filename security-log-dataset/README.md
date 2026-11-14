# Sample Security Log Dataset

## 1. Overview
This folder contains a small synthetic dataset of authentication and network security events prepared for initial testing of the project's threat detection pipeline.

All IP addresses, usernames, timestamps and events are illustrative sample data. They are not collected from real users, machines or networks.

## 2. Dataset Contents

| File | Description | Records |
|---|---|---:|
| data/authentication_logs.csv | Login, logout, password-change and failed-login events | 10 |
| data/network_security_logs.csv | Network connections, DNS activity, port scanning and unusual transfers | 10 |
| data/security_logs.json | Combined structured representation of the sample events | 20 |

## 3. Labels
- **Normal:** Illustrative routine activity.
- **Suspicious:** Illustrative activity with characteristics that may warrant investigation.

These labels are sample annotations for initial testing, not verified threat intelligence or definitive proof of an attack.

## 4. Authentication Log Fields
- `event_id`: Unique event identifier.
- `timestamp`: Event time in UTC (ISO 8601).
- `source_ip`: Originating IP address.
- `username`: Account involved.
- `event_type`: Authentication-related activity.
- `status`: Success or failure.
- `failed_attempts`: Number of failed attempts represented by the event.
- `severity`: Illustrative severity level.
- `label`: Normal or Suspicious.

## 5. Network Log Fields
- `event_id`: Unique event identifier.
- `timestamp`: Event time in UTC (ISO 8601).
- `source_ip`: Source address.
- `destination_ip`: Destination address.
- `protocol`: Network protocol.
- `destination_port`: Destination port.
- `bytes_transferred`: Illustrative transfer size, where available.
- `event_type`: Type of network activity.
- `severity`: Illustrative severity level.
- `label`: Normal or Suspicious.

## 6. Suspicious Patterns Represented
- Repeated authentication failures.
- Attempts to access privileged accounts.
- Repeated connection attempts.
- Port scanning behaviour.
- Attempts to connect to remote-access services.
- Unusually large data transfers.

## 7. Usage
The CSV files can be loaded using Python pandas. The JSON file can be loaded using Python's built-in `json` module.

Example:
```python
import pandas as pd
import json

authentication = pd.read_csv("data/authentication_logs.csv")
network = pd.read_csv("data/network_security_logs.csv")

with open("data/security_logs.json", "r") as file:
    security_data = json.load(file)

print(authentication.head())
print(network.head())
print(len(security_data["records"]))
```

## 8. Limitations
This is a small synthetic starter dataset. It does not represent the full diversity, volume or complexity of real enterprise security logs. The suspicious labels are illustrative and should not be treated as ground truth for production security decisions.

## 9. Project Relevance
The dataset provides initial labelled examples for understanding system activity and developing and testing the project's threat detection pipeline. It can later be expanded with additional event types, realistic log formats and carefully validated labels.
