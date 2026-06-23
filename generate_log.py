from datetime import datetime

import requests


def fetch_data():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1", timeout=10
        )
        response.raise_for_status()
        return response.json()
    except Exception:
        return {}


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    # Example usage when executed as a script
    log_data = ["User logged in", "User updated profile", "Report exported"]
    post = fetch_data()
    if post:
        log_data.append(
            f"Fetched Post Title: {post.get('title', 'No title found')}"
        )

    generate_log(log_data)