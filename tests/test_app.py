from selenium import webdriver
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)
print("asdok")


driver = webdriver.Chrome(
    "C:/Users/MadsKris/Documents/source/mkos/chrome-win64/chrome.exe"
)


def test_answer():
    print(dir_path)
