# URL2PDF
URL2PDF

Disclaimer: this script was written by ChatGPT. I have no knowledge of python.

URL2PDF converts a list of urls containing images into a pdf. It is useful to download books and manuscripts that are digitized and available in repositories that do now allow the download of the entire book/manuscript.

For this purpose, it is recommended that those interested make their own excel template to generate the urls, as each repository will use different urls and will require some degrees of fine tuning. 

This updated version implements two new features:
  1. it provides a visual representation of the progress and an estimatation of the time left
  2. the code is optimized to use a more efficient way to add images to the PDF
  3. once 50 pages are reached, it saves the outcome and it starts a new pdf. These pdfs are labeled in sequence, allowing an easy navigation between them. This avoids heavy, unusable pdfs in case of archiving-quality sources.

Happy to provide assistance with this (for educational purposes) for the repositories of the Bib.Vatic., El Escorial, and Bologna's Colegio de España.
