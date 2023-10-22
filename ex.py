def parse_url(url):
    parts = []

    # Separate protocol
    if "://" in url:
        protocol, url = url.split("://", 1)
        parts.append(protocol)

    # Separate hostname
    if "/" in url:
        hostname, url = url.split("/", 1)
        parts.append(hostname)

    # Separate key-value pairs
    query_params = []
    if "?" in url:
        url, query_string = url.split("?", 1)
        pairs = query_string.split("&")
        for pair in pairs:
            key, value = pair.split("=", 1)
            query_params.append(f'[{key}:{value}]')
    parts.extend(query_params)

    # Separate other parts separated by slashes
    path_segments = [segment for segment in url.split("/") if segment]
    parts.extend(path_segments)

    return " ".join(parts)

url = "https://www.example.com/path/to/resource?param1=value1&param2=value2"
formatted_url = parse_url(url)
print(formatted_url)
