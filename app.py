import requests
import os
import time

paths = [
    "/", "/cdn.js", "/dist/flowbite.min.js", "/favicon.ico",
    "/services", "/whatsmyip", "/upload", "/radio",
    "/dedicated-servers", "/.git/HEAD", "/.env", "/phpinfo",
    "/_profiler/phpinfo", "/info.php", "/index.html",
    "/backend/.env", "/api/.env", "/env.backup", "/phpinfo.php",
    "/main/.env", "/.env.old", "/api/config.env",
    "/.aws/credentials", "/lara/phpinfo.php", "/core/.env",
    "/application.properties", "/prod/.env", "/kyc/.env",
    "/aws/credentials", "/laravael/core/.env", "/server-info.php",
    "/docker/app/.env", "/lara/info.php", "/.env.prod",
    "/config/local.yml", "/secrets/aws_ses.env",
    "/awsstats/.env", "/admin/.env", "/config/storage.yml",
    "/settings.py", "/apps/.env", "/opt/aws/ses.env",
    "/logs/aws/ses.log", "/private/.env", "/docker-compose.yml",
    "/.AWS_/credentials", "/.env.bak", "/.env.example",
    "/.env.local", "/.env.production", "/.env.production.local",
    "/.env.sample", "/.env.stage", "/.envs/.production/.django",
    "/.travis.yml", "/.vscode/.env"
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def test_links(base_url):
    if not base_url.startswith("http"):
        base_url = "http://" + base_url

    found = []

    for i, path in enumerate(paths, 1):
        try:
            full_url = base_url.rstrip("/") + path
            r = requests.get(full_url, timeout=5)
            status = r.status_code
        except requests.RequestException:
            status = "ERROR"

        if isinstance(status, int) and status not in [404, 403]:
            found.append((path, status))

        clear_screen()
        print(f"Progress: {i}/{len(paths)}")
        print(f"Testing -> {path}")
        print(f"Response -> {status}")
        time.sleep(0.5)

    clear_screen()
    print("All found\n")
    if found:
        for path, status in found:
            print(f"{path} -> {status}")
    else:
        print("None")

if __name__ == "__main__":
    url = input("Enter base URL (e.g. http://localhost:8000): ").strip()
    test_links(url)
