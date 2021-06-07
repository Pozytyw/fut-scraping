from pyppeteer import launch
from pyppeteer import errors
from time import sleep
import asyncio
import get_script
import json


async def enumerationByLink(url, start, end):
    browser = await launch(headless=False)
    script = get_script.getScript("script.js")

    output = []
    i = start
    pages = await browser.pages()
    await asyncio.gather(*[browser.newPage() for i in range(5 - len(pages))])

    while i <= end:
        pages = await browser.pages()
        if i + 4 <= end:
            await asyncio.gather(
                goAndRender(output, pages[0], url + str(i), script),
                goAndRender(output, pages[1], url + str(i + 1), script),
                goAndRender(output, pages[2], url + str(i + 2), script),
                goAndRender(output, pages[3], url + str(i + 3), script),
                goAndRender(output, pages[4], url + str(i + 4), script),
            )
            i += 4
        else:
            await goAndRender(output, pages[0], url + str(i), script)
            i += 1
    await browser.close()
    return output


async def goAndRender(output, page, url, script):
    try:
        print("Going to and render - " + url)
        # go to url
        # remove cookies
        cookies = await page.cookies()
        await page.deleteCookie(* cookies)
        # set user agent
        await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")

        response = await page.goto(url, timeout=9000)
        while response.status == 429:
            response = await page.goto(url, timeout=9000)
            sleep(1)
        else:
            # render script and and append result to output
            output += await page.evaluate(script)

    except errors.TimeoutError or errors.NetworkError:
        print("TimeoutError")
        new_page = await page.browser.newPage()
        await page.close()
        await goAndRender(output, new_page, url, script)

file = open("output.json", "+w")
returned = asyncio.get_event_loop().run_until_complete(
    enumerationByLink("https://www.futwiz.com/en/fifa21/players?page=", 0, 701))
file.write(json.dumps(returned))
