import pytest
from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto('https://opensource-demo.orangehrmlive.com')
    page.fill('input[name="username"]', 'Admin')
    page.fill('input[name="password"]', 'admin123')
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')
    expect(page.locator('.oxd-topbar-header')).to_be_visible()
    print("✅ Login test passed")

def test_date_range_filter(page: Page):
    page.goto('https://opensource-demo.orangehrmlive.com')
    page.fill('input[name="username"]', 'Admin')
    page.fill('input[name="password"]', 'admin123')
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')

    # Click Leave from the sidebar menu
    page.get_by_role('link', name='Leave').click()
    page.wait_for_load_state('networkidle')

    # Take a screenshot so we can SEE what the page looks like
    page.screenshot(path='leave_page.png')

    # Print all input fields found on the page
    inputs = page.locator('input').all()
    print(f"\n✅ Found {len(inputs)} input fields on Leave page")
    for i, inp in enumerate(inputs):
        print(f"  Input {i}: type={inp.get_attribute('type')} "
              f"placeholder={inp.get_attribute('placeholder')} "
              f"class={inp.get_attribute('class')}")

def test_role_based_access(page: Page):
    page.goto('https://opensource-demo.orangehrmlive.com')
    page.fill('input[name="username"]', 'Admin')
    page.fill('input[name="password"]', 'admin123')
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')

    # Print ALL links in the sidebar
    links = page.get_by_role('link').all()
    print(f"\n✅ Found {len(links)} links on dashboard")
    for link in links:
        print(f"  Link: '{link.inner_text()}'")

    # Take screenshot of dashboard
    page.screenshot(path='dashboard.png')