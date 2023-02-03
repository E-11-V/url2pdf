import requests
from fpdf import FPDF
import io

def url_to_image(url):
    return io.BytesIO(requests.get(url).content)

def jpgs_to_pdf(urls, output_file):
    pdf = FPDF()
    for url in urls:
        img = url_to_image(url)
        pdf.add_page()
        pdf.image(img, x=0, y=0, w=210, h=297)
    pdf.output(output_file, "F")

jpg_urls = [
    "https://via.placeholder.com/150x200",
    "https://via.placeholder.com/200x150",
    "https://via.placeholder.com/300x200"
]

jpgs_to_pdf(jpg_urls, "images.pdf")
