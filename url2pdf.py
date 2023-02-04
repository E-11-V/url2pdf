import tempfile
import urllib.request
import fpdf
import socket
import time

def jpgs_to_pdf(jpg_urls, pdf_filename):
    pdf_parts = []
    processed_images = 0
    total_images = len(jpg_urls)
    start_time = time.time()
    part_number = 1
    
    while processed_images < total_images:
        pdf = fpdf.FPDF(format='letter')
        images_in_part = 0
        
        while processed_images < total_images and images_in_part < 50:
            try:
                with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as f:
                    socket.setdefaulttimeout(10) 
                    f.write(urllib.request.urlopen(jpg_urls[processed_images]).read())
                    pdf.add_page()
                    pdf.image(f.name, x=0, y=0, w=210, h=297)
                    
                    processed_images += 1
                    images_in_part += 1
                    
                    elapsed_time = time.time() - start_time
                    avg_time_per_image = elapsed_time / processed_images
                    remaining_images = total_images - processed_images
                    estimated_time_left = avg_time_per_image * remaining_images
                    
                    progress = processed_images / total_images * 100
                    print(f'Processing... {progress:.2f}% complete. Estimated time left: {estimated_time_left:.2f} seconds.', end='\r')
            except Exception as e:
                print(f'Error processing {jpg_urls[processed_images]}: {e}')
        
        pdf_parts.append(pdf)
        pdf_part_filename = f'{pdf_filename.rsplit(".", 1)[0]}_{part_number}.pdf'
        pdf.output(pdf_part_filename, 'F')
        print(f'Part {part_number} saved as {pdf_part_filename}')
        part_number += 1

jpg_urls = [
	
"https://imagenes.com/default1.jpg",
"https://imagenes.com/default2.jpg",
"https://imagenes.com/default3.jpg",
"https://imagenes.com/default4.jpg",

]

pdf_filename = "filenamehere.pdf"

jpgs_to_pdf(jpg_urls, pdf_filename)
