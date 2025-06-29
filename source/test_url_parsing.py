import re
from urllib.parse import urlparse

# Test URLs including problematic ones
test_urls = [
    "https://www.scientificlinux.org/ (EOL)",
    "http://www.slackware.com/",
    "http://vinelinux.org/ (Largely historical)",
    "invalid-url-without-scheme.com",
    "just-a-domain",
    "https://github.com/microsoft/CBL-Mariner",
    "/local/path/without/scheme"
]

for url in test_urls:
    print(f"Original URL: {url}")
    
    # Clean the URL by removing comments in parentheses
    clean_url = re.sub(r'\s*\(.*?\)\s*', '', url).strip()
    print(f"  After cleaning: {clean_url}")
    
    # Make sure the URL has a scheme, add http:// if missing
    if not clean_url.startswith(('http://', 'https://', 'ftp://')):
        clean_url = f'http://{clean_url}'
    print(f"  With scheme: {clean_url}")
    
    # Parse website to get the domain
    parsed_url = urlparse(clean_url)
    domain = parsed_url.netloc
    
    # Skip malformed URLs that don't have a valid domain
    if not domain:
        domain = 'invalid-domain'
    else:
        # Remove 'www.' if present for a cleaner look
        if domain.startswith('www.'):
            domain = domain[4:]
    
    print(f"  Extracted domain: {domain}")
    print("")