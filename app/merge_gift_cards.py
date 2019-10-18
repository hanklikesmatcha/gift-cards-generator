import glob
import os

from PyPDF2 import PdfFileMerger
from fpdf import FPDF


class MergeCards():
    def __init__(self, format, home, customer):
        if format == 'a5_horizontal':
            MergeA5HorizontalCards(home, customer)
        elif format == 'a5_portrait':
            MergeA5PortraitCards(home, customer)
        elif format == 'a6_horizontal':
            MergeA6HorizontalCards(home, customer)
        elif format == 'a6_portrait':
            MergeA6PortraitCards(home, customer)


class MergeA5HorizontalCards():
    def __init__(self, home, customer):
        directory = os.listdir('./output/a5-horizontal')
        files = filter(lambda f: "gift-card-" in f, directory)
        files = sorted(files, key=lambda f: f)

        number_of_a5_horizontal = len(files)
        count = 0
        gift_card_number = 1
        while number_of_a5_horizontal > 0:
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()
            pdf.image('./output/a5-horizontal/{}'.format(files[count]), x=0, y=0, w=210, h=148)
            pdf.image('./output/a5-horizontal/{}'.format(files[count+1]), x=0, y=148, w=210, h=148)
            pdf.output("{}/{}-gift-cards/a5-horizontal/{}-a5-horizontal-{}.pdf".format(home, customer, customer, gift_card_number))
            count += 2
            number_of_a5_horizontal -= 2
            gift_card_number += 1
            if number_of_a5_horizontal < 2:
                break
        if number_of_a5_horizontal == 1:
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()
            pdf.image('./output/a5-horizontal/{}'.format(files[count]), x=0, y=0, w=210, h=148)
            pdf.output("{}/{}-gift-cards/a5-horizontal/{}-a5-horizontal-{}.pdf".format(home, customer, customer, gift_card_number))
            number_of_a5_horizontal -= 1
        else:
            MergePDFS(home=home, customer=customer, format='a5-horizontal')


class MergeA5PortraitCards():
    def __init__(self, home, customer):
        directory = os.listdir('./output/a5-portrait')
        files = filter(lambda f: "gift-card-" in f, directory)
        files = sorted(files, key=lambda f: f)

        number_of_a5_portrait = len(files)
        count = 0
        gift_card_number = 1
        while number_of_a5_portrait > 0:
            pdf = FPDF(orientation='L', unit='mm', format='A4')
            pdf.add_page()
            pdf.image('./output/a5-portrait/{}'.format(files[count]), x=0, y=0, w=148)
            pdf.image('./output/a5-portrait/{}'.format(files[count + 1]), x=148, y=0, w=148)
            pdf.output("{}/{}-gift-cards/a5-portrait/{}-a5-portrait-{}.pdf".format(home, customer, customer, gift_card_number))
            count += 2
            number_of_a5_portrait -= 2
            gift_card_number += 1
            if number_of_a5_portrait < 2:
                break
        if number_of_a5_portrait == 1:
            pdf = FPDF(orientation='L', unit='mm', format='A4')
            pdf.add_page()
            pdf.image('./output/a5-portrait/{}'.format(files[count]), x=0, y=0, w=148)
            pdf.output("{}/{}-gift-cards/a5-portrait/{}-a5-portrait-{}.pdf".format(home, customer, customer, gift_card_number))
            number_of_a5_portrait -= 1
        else:
            MergePDFS(home=home, customer=customer, format='a5-portrait')


class MergeA6HorizontalCards():
    def __init__(self, home, customer):
        directory = os.listdir('./output/a6-horizontal')
        files = filter(lambda f: "gift-card-" in f, directory)
        files = sorted(files, key=lambda f: f)

        number_of_a6_horizontal = len(files)
        count = 0
        gift_card_number = 1
        while number_of_a6_horizontal > 0:
            pdf = FPDF(orientation='L', unit='mm', format='A4')
            pdf.add_page()
            pdf.image('./output/a6-horizontal/{}'.format(files[count]), x=0, y=0, w=148)
            pdf.image('./output/a6-horizontal/{}'.format(files[count + 1]), x=148, y=0, w=148)
            pdf.image('./output/a6-horizontal/{}'.format(files[count + 2]), x=0, y=105, w=148)
            pdf.image('./output/a6-horizontal/{}'.format(files[count + 3]), x=148, y=105, w=148)
            pdf.output("{}/{}-gift-cards/a6-horizontal/{}-a6-horizontal-{}.pdf".format(home, customer, customer, gift_card_number))
            count += 4
            number_of_a6_horizontal -= 4
            gift_card_number += 1
            if number_of_a6_horizontal < 4:
                if number_of_a6_horizontal == 3:
                    pdf = FPDF(orientation='L', unit='mm', format='A4')
                    pdf.add_page()
                    pdf.image('./output/a6-horizontal/{}'.format(files[count]), x=0, y=0, w=148)
                    pdf.image('./output/a6-horizontal/{}'.format(files[count + 1]), x=148, y=0, w=148)
                    pdf.image('./output/a6-horizontal/{}'.format(files[count + 2]), x=0, y=105, w=148)
                    pdf.output("{}/{}-gift-cards/a6-horizontal/{}-a6-horizontal-{}.pdf".format(home, customer, customer, gift_card_number))
                    number_of_a6_horizontal -= 3
                elif number_of_a6_horizontal == 2:
                    pdf = FPDF(orientation='L', unit='mm', format='A4')
                    pdf.add_page()
                    pdf.image('./output/a6-horizontal/{}'.format(files[count]), x=0, y=0, w=148)
                    pdf.image('./output/a6-horizontal/{}'.format(files[count + 1]), x=148, y=0, w=148)
                    pdf.output("{}/{}-gift-cards/a6-horizontal/{}-a6-horizontal-{}.pdf".format(home, customer, customer, gift_card_number))
                    number_of_a6_horizontal -= 2
                elif number_of_a6_horizontal == 1:
                    pdf = FPDF(orientation='L', unit='mm', format='A4')
                    pdf.add_page()
                    pdf.image('./output/a6-horizontal/{}'.format(files[count]), x=0, y=0, w=148)
                    pdf.output("{}/{}-gift-cards/a6-horizontal/{}-a6-horizontal-{}.pdf".format(home, customer, customer, gift_card_number))
                    number_of_a6_horizontal -= 1
        MergePDFS(home=home, customer=customer, format='a6-horizontal')


class MergeA6PortraitCards():
    def __init__(self, home, customer):
        directory = os.listdir('./output/a6-portrait')
        files = filter(lambda f: "gift-card-" in f, directory)
        files = sorted(files, key=lambda f: f)

        number_of_a6_portrait = len(files)
        count = 0
        gift_card_number = 1
        while number_of_a6_portrait > 0:
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()
            pdf.image('./output/a6-portrait/{}'.format(files[count]), x=0, y=0, w=105, h=148)
            pdf.image('./output/a6-portrait/{}'.format(files[count + 1]), x=105, y=0, w=105, h=148)
            pdf.image('./output/a6-portrait/{}'.format(files[count + 2]), x=0, y=148, w=105, h=148)
            pdf.image('./output/a6-portrait/{}'.format(files[count + 3]), x=105, y=148, w=105, h=148)
            pdf.output("{}/{}-gift-cards/a6-portrait/{}-a6-portrait-{}.pdf".format(home, customer, customer, gift_card_number))
            count += 4
            number_of_a6_portrait -= 4
            gift_card_number += 1
            if number_of_a6_portrait < 4:
                if number_of_a6_portrait == 3:
                    pdf = FPDF(orientation='P', unit='mm', format='A4')
                    pdf.add_page()
                    pdf.image('./output/a6-portrait/{}'.format(files[count]), x=0, y=0, w=105, h=148)
                    pdf.image('./output/a6-portrait/{}'.format(files[count + 1]), x=105, y=0, w=105, h=148)
                    pdf.image('./output/a6-portrait/{}'.format(files[count + 2]), x=0, y=148, w=105, h=148)
                    pdf.output("{}/{}-gift-cards/a6-portrait/{}-a6-portrait-{}.pdf".format(home, customer, customer, gift_card_number))
                    number_of_a6_portrait -= 3
                elif number_of_a6_portrait == 2:
                    pdf = FPDF(orientation='P', unit='mm', format='A4')
                    pdf.add_page()
                    pdf.image('./output/a6-portrait/{}'.format(files[count]), x=0, y=0, w=105, h=148)
                    pdf.image('./output/a6-portrait/{}'.format(files[count + 1]), x=105, y=0, w=105, h=148)
                    pdf.output("{}/{}-gift-cards/a6-portrait/{}-a6-portrait-{}.pdf".format(home, customer, customer, gift_card_number))
                    number_of_a6_portrait -= 2
                elif number_of_a6_portrait == 1:
                    pdf = FPDF(orientation='P', unit='mm', format='A4')
                    pdf.add_page()
                    pdf.image('./output/a6-portrait/{}'.format(files[count]), x=0, y=0, w=105, h=148)
                    pdf.output("{}/{}-gift-cards/a6-portrait/{}-a6-portrait-{}.pdf".format(home, customer, customer, gift_card_number))
                    number_of_a6_portrait -= 1
        MergePDFS(home=home, customer=customer, format='a6-portrait')


class MergePDFS():
    def __init__(self, home, customer, format):
        path = "{}/{}-gift-cards/{}".format(home, customer, format)
        pdfs = [f for f in glob.glob(path + "/*.pdf")]
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merger.write('{}/{}-gift-cards/{}.pdf'.format(home, customer, customer))
        merger.close()