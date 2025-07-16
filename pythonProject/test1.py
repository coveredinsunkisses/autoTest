import asyncio
import re

from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=5000)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://only.digital/fields/')

        footer = page.locator('footer')
        await footer.scroll_into_view_if_needed()
        await expect(footer).to_be_visible()

        await expect(footer.get_by_role('img')).to_be_visible()
        await expect(footer.get_by_role('button', name = 'начать проект')).to_be_visible()


        await page.screenshot(path='footer_projects.png')

        await browser.close()

asyncio.run(main())
