import PyPDF2
import sys

main, water = sys.argv[1], sys.argv[2]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


def pdf_watermark(pdf_file, watermark):
    input_pdf = PyPDF2.PdfFileReader(open(f'{pdf_file}', 'rb'))
    watermark_pdf = PyPDF2.PdfFileReader(open(f'{watermark}', 'rb'))
    output = PyPDF2.PdfFileWriter()


    for i in range(input_pdf.getNumPages()):
        page = input_pdf.getPage(i)
        page.mergePage(watermark_pdf.getPage(0))
        output.addPage(page)

        with open('watermarked_pdf.pdf', 'wb') as file:
            output.write(file)


pdf_watermark(main, water)
