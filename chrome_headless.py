import os
import subprocess
import zipfile
import requests
import shutil
def download_file(url, output_file):
    response = requests.get(url, stream=True)
    with open(output_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def main():
    # Set the versions and output directory
    SELENIUM_VER = "3.141.0"
    # urllib3==1.26.15
    URLLIB3='1.26.15'
    CHROME_BINARY_VER = "v1.0.0-55"
    CHROMEDRIVER_VER = "2.43"
    OUT_DIR = os.path.join("out", "build", "chrome_headless", "python", "lib", "python3.10", "site-packages")
    OUT_DIR1 = os.path.join("out")

    # Create the output directory if it doesn't exist
    os.makedirs(OUT_DIR, exist_ok=True)

    # Install Selenium in the output directory
    subprocess.run(["pip", "install", f"selenium", "-t", OUT_DIR], check=True)
    subprocess.run(["pip", "install", f"urllib3=={URLLIB3}", "-t", OUT_DIR], check=True)
    # Copy chrome_headless.py to the output directory
    shutil.copy("chrome_headless.py", os.path.join("test.py"))

    # Download and extract ChromeDriver
    chromedriver_url = f"https://chromedriver.storage.googleapis.com/{CHROMEDRIVER_VER}/chromedriver_linux64.zip"
    download_file(chromedriver_url, "chromedriver.zip")
    with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
        zip_ref.extractall(os.path.join("build", "chrome_headless"))

    # Download and extract Headless Chromium
    headless_chromium_url = f"https://github.com/adieuadieu/serverless-chrome/releases/download/{CHROME_BINARY_VER}/stable-headless-chromium-amazonlinux-2017-03.zip"
    download_file(headless_chromium_url, "headless-chromium.zip")
    with zipfile.ZipFile("headless-chromium.zip", "r") as zip_ref:
        zip_ref.extractall(os.path.join("build", "chrome_headless"))

    # Create the chrome_headless.zip archive
    with zipfile.ZipFile("chrome_headless.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("build/chrome_headless"):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, "build/chrome_headless"))

if __name__ == "__main__":
    main()
