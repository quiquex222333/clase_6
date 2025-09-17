from playwright.sync_api import expect

def assert_visible(locator, msg="El elemento no es visible"):
    expect(locator).to_be_visible(), msg

def assert_text(locator, expected, msg="Texto no coincide"):
    expect(locator).to_have_text(expected), msg
