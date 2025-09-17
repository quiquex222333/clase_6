import os
from playwright.sync_api import expect

def test_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")
    file_path = os.path.abspath("data/sample.txt")
    page.set_input_files("#file-upload", file_path)
    page.click("#file-submit")
    expect(page.locator("#uploaded-files")).to_have_text("sample.txt")
