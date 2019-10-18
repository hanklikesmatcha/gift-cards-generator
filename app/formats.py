from PyPDF2 import PdfFileWriter, PdfFileReader
from fpdf import FPDF
from pdf2image import convert_from_path


class Formats():
    def __init__(self, format, row, template_location):
        if format == 'a5_horizontal':
            A5Horizontal(row, template_location)
        elif format == 'a5_portrait':
            A5Portrait(row, template_location)
        elif format == 'a6_horizontal':
            A6Horizontal(row, template_location)
        else:
            A6Portrait(row, template_location)
            

class A5Horizontal():
    def __init__(self, row, template_location):
        gift_codes = self.get_gift_codes(row)
        self.write_into_pdf(input=gift_codes)
        for index, code in enumerate(gift_codes):
            self.create_cards(input_pdf=template_location,
                              output_pdf='./output/a5-horizontal/pdfs/gift-card-{}.pdf'.format(code),
                              watermark_pdf='./gift-codes/a5-horizontal/gift-code-{}.pdf'.format(code))

            imgs = convert_from_path('./output/a5-horizontal/pdfs/gift-card-{}.pdf'.format(code), 500)
            for img in imgs:
                img.save('./output/a5-horizontal/gift-card-{}.jpg'.format(code), 'JPEG')

    def get_gift_codes(self, row):
        order_list = []
        gift_code = row.lower()
        order_list.append(gift_code)

        return order_list

    def write_into_pdf(self, input):
        for code in input:
            print("Gift Code: ", code)
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('Raleway', '', r'./font/Raleway-SemiBold.ttf', uni=True)
            pdf.set_font(family='Raleway', size=12)
            pdf.text(85.0, 289.2, code)
            pdf.output('./gift-codes/a5-horizontal/gift-code-{}.pdf'.format(code))

    def create_cards(self, input_pdf, output_pdf, watermark_pdf):
        watermark = PdfFileReader(watermark_pdf)
        watermark_page = watermark.getPage(0)

        pdf = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()

        for page in range(pdf.getNumPages()):
            pdf_page = pdf.getPage(page)
            pdf_page.mergePage(watermark_page)
            pdf_writer.addPage(pdf_page)

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)


class A5Portrait():
    def __init__(self, row, template_location):
        gift_codes = self.get_gift_codes(row)
        self.write_into_pdf(input=gift_codes)
        for index, code in enumerate(gift_codes):
            self.create_cards(input_pdf=template_location,
                              output_pdf='./output/a5-portrait/pdfs/gift-card-{}.pdf'.format(code),
                              watermark_pdf='./gift-codes/a5-portrait/gift-code-{}.pdf'.format(code))

            imgs = convert_from_path('./output/a5-portrait/pdfs/gift-card-{}.pdf'.format(code), 500)
            for img in imgs:
                img.save('./output/a5-portrait/gift-card-{}.jpg'.format(code), 'JPEG')

    def get_gift_codes(self, row):
        order_list = []
        gift_code = row.lower()
        order_list.append(gift_code)

        return order_list

    def write_into_pdf(self, input):
        for code in input:
            print("Gift Code: ", code)
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('Raleway', '', r'./font/Raleway-SemiBold.ttf', uni=True)
            pdf.set_font(family='Raleway', size=12)
            pdf.text(59, 259.8, code)
            pdf.output('./gift-codes/a5-portrait/gift-code-{}.pdf'.format(code))

    def create_cards(self, input_pdf, output_pdf, watermark_pdf):
        watermark = PdfFileReader(watermark_pdf)
        watermark_page = watermark.getPage(0)

        pdf = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()

        for page in range(pdf.getNumPages()):
            pdf_page = pdf.getPage(page)
            pdf_page.mergePage(watermark_page)
            pdf_writer.addPage(pdf_page)

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)


class A6Horizontal():
    def __init__(self, row, template_location):
        gift_codes = self.get_gift_codes(row)
        self.write_into_pdf(input=gift_codes)
        for index, code in enumerate(gift_codes):
            self.create_cards(input_pdf=template_location,
                              output_pdf='./output/a6-horizontal/pdfs/gift-card-{}.pdf'.format(code),
                              watermark_pdf='./gift-codes/a6-horizontal/gift-code-{}.pdf'.format(code))
            imgs = convert_from_path('./output/a6-horizontal/pdfs/gift-card-{}.pdf'.format(code), 500)
            for img in imgs:
                img.save('./output/a6-horizontal/gift-card-{}.jpg'.format(code), 'JPEG')

    def get_gift_codes(self, row):
        order_list = []
        gift_code = row.lower()
        order_list.append(gift_code)

        return order_list

    def write_into_pdf(self, input):
        for code in input:
            print("Gift Code: ", code)
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('Raleway', '', r'./font/Raleway-SemiBold.ttf', uni=True)
            pdf.set_font(family='Raleway', size=9)
            pdf.text(49, 291.2, code)
            pdf.output('./gift-codes/a6-horizontal/gift-code-{}.pdf'.format(code))

    def create_cards(self, input_pdf, output_pdf, watermark_pdf):
        watermark = PdfFileReader(watermark_pdf)
        watermark_page = watermark.getPage(0)

        pdf = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()

        for page in range(pdf.getNumPages()):
            pdf_page = pdf.getPage(page)
            pdf_page.mergePage(watermark_page)
            pdf_writer.addPage(pdf_page)

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)


class A6Portrait():
    def __init__(self, row, template_location):
        gift_codes = self.get_gift_codes(row)
        self.write_into_pdf(input=gift_codes)
        for index, code in enumerate(gift_codes):
            self.create_cards(input_pdf=template_location,
                              output_pdf='./output/a6-portrait/pdfs/gift-card-{}.pdf'.format(code),
                              watermark_pdf='./gift-codes/a6-portrait/gift-code-{}.pdf'.format(code))
            imgs = convert_from_path('./output/a6-portrait/pdfs/gift-card-{}.pdf'.format(code), 500)
            for img in imgs:
                img.save('./output/a6-portrait/gift-card-{}.jpg'.format(code), 'JPEG')

    def get_gift_codes(self, row):
        order_list = []
        gift_code = row.lower()
        order_list.append(gift_code)

        return order_list

    def write_into_pdf(self, input):
        for code in input:
            print("Gift Code: ", code)
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('Raleway', '', r'./font/Raleway-SemiBold.ttf', uni=True)
            pdf.set_font(family='Raleway', size=9)
            pdf.text(39.4, 276.1, code)
            pdf.output('./gift-codes/a6-portrait/gift-code-{}.pdf'.format(code))

    def create_cards(self, input_pdf, output_pdf, watermark_pdf):
        watermark = PdfFileReader(watermark_pdf)
        watermark_page = watermark.getPage(0)

        pdf = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()

        for page in range(pdf.getNumPages()):
            pdf_page = pdf.getPage(page)
            pdf_page.mergePage(watermark_page)
            pdf_writer.addPage(pdf_page)

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)
