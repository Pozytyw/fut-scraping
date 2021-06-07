from pyppeteer import launch
from pyppeteer import errors
import asyncio
import get_script
import json


async def render_in_list(urls_list):
    browser = await launch(headless=False)
    getter = get_script.getScript("getter.js")
    download = get_script.getScript("download.js")

    scripts = [getter, download]

    pages = await browser.pages()
    await asyncio.gather(*[browser.newPage() for i in range(5 - len(pages))])
    i = 0
    while len(urls_list) > 0:
        print(i)
        pages = await browser.pages()
        if len(urls_list) >= 5:
            await asyncio.gather(
                goAndRender(pages[0], urls_list[0], scripts),
                goAndRender(pages[1], urls_list[1], scripts),
                goAndRender(pages[2], urls_list[2], scripts),
                goAndRender(pages[3], urls_list[3], scripts),
                goAndRender(pages[4], urls_list[4], scripts),
            )
            i += 5
            del urls_list[:5]
        else:
            await goAndRender(pages[0], urls_list, scripts),
            i += 1
            del urls_list[0]
    await browser.close()


async def goAndRender(page, url_at, scripts):
    try:
        print("Going to and render - " + url_at[1])
        # go to url
        # remove cookies
        cookies = await page.cookies()
        await page.deleteCookie(* cookies)
        # set user agent
        await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
        await page.goto(url_at[0], timeout=9000)

        # render script and and append result to output
        await page.addScriptTag(url="https://html2canvas.hertzen.com/dist/html2canvas.min.js")
        save = await page.evaluate(scripts[0])
        await page.waitForSelector("#output")
        await page.evaluate(scripts[1])
        opened = open("players/" + save['file_name'][:-4] + ".json", "w+")
        opened.write(json.dumps(save))

    except errors.TimeoutError:
        print("TimeoutError")
        new_page = await page.browser.newPage()
        await page.close()
        await goAndRender(new_page, url_at, scripts)

file = open("output.json")
table = json.load(file)
asyncio.get_event_loop().run_until_complete(render_in_list(table[5005:]))
