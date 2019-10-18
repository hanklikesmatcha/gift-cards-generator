import sys
from time import sleep

import xlrd
import os
from gooey import Gooey, GooeyParser
from PyPDF2 import PdfFileReader
from app.file_allocation import CreateFolder, DeleteFolder
from app.formats import Formats
from app.merge_gift_cards import MergeCards


class Generator():
    def __init__(self):
        # Interface
        args = self.interface()
        # Orders
        customer = args.name
        home = args.output
        workbook = xlrd.open_workbook(str(args.input))
        sheet = workbook.sheet_by_index(0)
        rows = range(sheet.nrows)
        gift_codes = []
        # Template
        template = PdfFileReader(open(args.format, 'rb'))
        template_location = args.format
        template_format = None
        template_size = template.getPage(0).mediaBox
        template_width_in_cm = round(float(template_size[2]) * 0.03529, 2)
        template_height_in_cm = round(float(template_size[3]) * 0.03529, 2)

        # Create folder for outputs
        CreateFolder(home, customer)
        # Filter invalid gift codes
        for row in rows:
            if len(sheet.cell_value(row, 0)) == 16:
                gift_codes.append(sheet.cell_value(row, 0))
        # Get template format
        if template_width_in_cm >= 21.0 and template_height_in_cm >= 14.8:
            template_format = 'a5_horizontal'
        elif template_width_in_cm >= 14.8 and template_height_in_cm >= 21.1:
            template_format = 'a5_portrait'
        elif template_width_in_cm >= 14.8 and template_height_in_cm >= 10.5:
            template_format = 'a6_horizontal'
        elif template_width_in_cm >= 10.5 and template_height_in_cm >= 14.8:
            template_format = 'a6_portrait'
        # Generate gift cards
        for index, row in enumerate(gift_codes):
            progress = round(100 / float(len(gift_codes)), 1)
            index = float(progress * index)
            sys.stdout.flush()
            sleep(0.05)
            print("progress: {}%".format(index))
            Formats(template_format, row, template_location)

        # Merge gift cards to one
        MergeCards(template_format, home, customer)
        # Delete folder for removing temporary files
        DeleteFolder(home, customer, template_format)

        print("{} has total orders: {} ".format(customer, len(gift_codes)))

    @Gooey(program_name='Hi! Christine! ', advanced=True, progress_regex=r"^progress: (-?\d+\.\d+)%$")
    def interface(self):
        parser = GooeyParser(description="Gift cards generator")
        parser.add_argument('name',
                            metavar='Customer Name',
                            )
        parser.add_argument('format',
                            metavar='Format',
                            widget='FileChooser',
                            )
        parser.add_argument('input',
                            metavar='Input',
                            help='Order',
                            widget='FileChooser')
        parser.add_argument('output',
                            metavar='Output',
                            help='Where to place the gift-cards',
                            widget='DirChooser',)

        args = parser.parse_args()

        return args


