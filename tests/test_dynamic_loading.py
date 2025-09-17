# from playwright.sync_api import expect

# def test_dynamic_loading_hello_world(page):
#     page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
#     page.click("button")  # inicia el loading (aparece spinner)
#     finish = page.locator("#finish")
#     finish.wait_for(state="visible")  # o: expect(finish).to_be_visible()
#     expect(finish).to_contain_text("Hello World!")
