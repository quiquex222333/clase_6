# from playwright.sync_api import expect

# def test_iframe_edit(page):
#     page.goto("https://the-internet.herokuapp.com/iframe")
#     frame = page.frame_locator("iframe[id='mce_0_ifr']")
#     editor = frame.locator("#tinymce")
#     editor.click()
#     editor.fill("Hola desde Playwright!")
#     expect(editor).to_contain_text("Hola")
