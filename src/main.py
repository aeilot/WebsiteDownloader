from playwright.sync_api import sync_playwright
from pdf2docx import Converter

download_list = ['https://hsefz.aeilot.top/拳击boxing']


def run(playwright, link, num):
    chromium = playwright.chromium
    browser = chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(link)
    page.emulate_media(media="print")
    page.pdf(path=("%d.pdf") % num, scale=0.8)
    browser.close()


playwright = sync_playwright().start()

for i in range(len(download_list)):
    link = download_list[i]
    run(playwright, link, i)

playwright.stop()

for i in range(len(download_list)):
    pdf_file = "%d.pdf" % i
    docx_file = "%d.docx" % i
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

print("Converted: %d Websites" % len(download_list))
