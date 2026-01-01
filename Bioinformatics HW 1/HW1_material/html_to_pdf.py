import asyncio
import os
from pathlib import Path
from pyppeteer import launch

async def main():
    html_path = Path('/Users/arshiyasalehi/Desktop/HW1_material/hw1_completed.html').resolve()
    pdf_path = html_path.with_suffix('.pdf')

    browser = await launch(args=['--no-sandbox'])
    page = await browser.newPage()
    # Use a file:// URL for local HTML
    file_url = f'file://{html_path}'
    await page.goto(file_url, waitUntil='networkidle0')
    await page.emulateMediaType('screen')
    await page.pdf({
        'path': str(pdf_path),
        'printBackground': True,
        'format': 'A4'
    })
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())