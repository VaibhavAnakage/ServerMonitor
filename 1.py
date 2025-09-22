import ssl
import socket
from datetime import datetime

def get_ssl_expiry_date(hostname, port=443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssl_info = ssock.getpeercert()
                expiry_str = ssl_info['notAfter']
                expiry_date = datetime.strptime(expiry_str, '%b %d %H:%M:%S %Y %Z')
                return expiry_date
    except Exception as e:
        print(f"Error retrieving SSL certificate for {hostname}: {e}")
        return None

# Example usage
hostname = 'mhealuat.renesas.com'
expiry = get_ssl_expiry_date(hostname)
if expiry:
    print(f"SSL certificate for {hostname} expires on: {expiry}")
