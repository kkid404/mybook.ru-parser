from PIL import Image
import os
import time
from PyPDF4 import PdfFileMerger
import shutil

class Formatter:
    
    def convert_png_to_pdf(book : list):
        pdf = []
        start = time.time()
        for page in book:
            image = Image.open(page)
            im_1 = image.convert('RGB')
            new_image = str(page).replace("png", "pdf")
            im_1.save(new_image)
            os.remove(page)
            pdf.append(new_image)
        end = time.time() - start
        print(f"Конвертировано в PDF за {end} секунд")
        return pdf

    def create_book(book: list, name):
        start = time.time()
        merge = PdfFileMerger()

        for page in book:
            merge.append(page)
        
        merge.write(f"{name}.pdf")
        merge.close()

        end = time.time() - start
        print(f"Конвертировано в книгу за {end} секунд")
        path = os.path.abspath(name)
        shutil.rmtree(path)
        return os.path.abspath(f"{name}.pdf")