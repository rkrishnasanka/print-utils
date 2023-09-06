from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import click



@click.command()
@click.argument('pdf_path', type=click.Path(exists=True))
def split_pdf_odd_even_pages(pdf_path: Path):
    """
    Split a PDF into two PDFs, one with the odd pages and one with the even pages.
    """

    # Open the PDF file
    pdf_file = open(pdf_path.absolute(), 'rb')

    # Create a PDF reader object
    pdf_reader = PdfReader(pdf_file)

    # Create a PDF writer object
    pdf_writer_odd = PdfWriter()
    pdf_writer_even = PdfWriter()

    # Loop through each page in the PDF file
    for page_num in range(len(pdf_reader.pages)):
        # If the page number is even, add it to the even writer
        if page_num % 2 == 0:
            pdf_writer_even.add_page(pdf_reader.pages[page_num])
        # If the page number is odd, add it to the odd writer
        else:
            pdf_writer_odd.add_page(pdf_reader.pages[page_num])

    # if the number of pages is odd, add an additional blank page to the odd writer
    if len(pdf_reader.pages) % 2 != 0:
        pdf_writer_odd.add_blank_page()

    # Write the even pages to a new PDF file
    with open(f'{pdf_path.stem}_part_1.pdf', 'wb') as f:
        pdf_writer_even.write(f)

    # Write the odd pages to a new PDF file
    with open(f'{pdf_path.stem}_part_2.pdf', 'wb') as f:
        pdf_writer_odd.write(f)

    # Close the PDF file objects
    pdf_file.close()


