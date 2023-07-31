from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from flask import Flask, render_template,request
from google.oauth2.service_account import Credentials

from urllib.parse import urlparse
import pandas as pd
import time
import os



    
        

options = Options()
options.add_argument("--headless")
options.add_argument("content-Type=application/x-www-form-urlencoded; charset=UTF-8")
options.add_argument("user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
options.add_argument("accept-language=en-US,en;q=0.9")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
answer = True
driver = webdriver.Chrome(options=options)


