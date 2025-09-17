# from playwright.sync_api import expect

# def test_js_alert_accept(page):
#     messages = []

#     def on_dialog(dialog):
#         messages.append(dialog.message)
#         dialog.accept()

#     page.on("dialog", on_dialog)
#     page.goto("https://the-internet.herokuapp.com/javascript_alerts")
#     page.click("text=Click for JS Alert")
#     expect(page.locator("#result")).to_have_text("You successfully clicked an alert")
#     assert any("JS" in m for m in messages)
