import os
import shutil


class CreateFolder():
    def __init__(self, home, customer):
        try:
            os.mkdir('./gift-codes')
            os.mkdir('./gift-codes/a5-portrait')
            os.mkdir('./gift-codes/a6-horizontal')
            os.mkdir('./gift-codes/a5-horizontal')
            os.mkdir('./gift-codes/a6-portrait')
        except OSError:
            shutil.rmtree("./gift-codes")
            os.mkdir('./gift-codes')
            os.mkdir('./gift-codes/a5-portrait')
            os.mkdir('./gift-codes/a6-horizontal')
            os.mkdir('./gift-codes/a5-horizontal')
            os.mkdir('./gift-codes/a6-portrait')
            pass
        try:
            os.mkdir('./output')
            os.mkdir('./output/a5-portrait')
            os.mkdir('./output/a5-portrait/pdfs')
            os.mkdir('./output/a6-horizontal')
            os.mkdir('./output/a6-horizontal/pdfs')
            os.mkdir('./output/a5-horizontal')
            os.mkdir('./output/a5-horizontal/pdfs')
            os.mkdir('./output/a6-portrait')
            os.mkdir('./output/a6-portrait/pdfs')
            pass
        except OSError:
            shutil.rmtree("./output")
            os.mkdir('./output')
            os.mkdir('./output/a5-portrait')
            os.mkdir('./output/a5-portrait/pdfs')
            os.mkdir('./output/a6-horizontal')
            os.mkdir('./output/a6-horizontal/pdfs')
            os.mkdir('./output/a5-horizontal')
            os.mkdir('./output/a5-horizontal/pdfs')
            os.mkdir('./output/a6-portrait')
            os.mkdir('./output/a6-portrait/pdfs')
            pass
        try:
            os.mkdir('{}/{}-gift-cards'.format(home, customer))
            os.mkdir('{}/{}-gift-cards/a5-portrait'.format(home, customer))
            os.mkdir('{}/{}-gift-cards/a6-horizontal'.format(home, customer))
            os.mkdir('{}/{}-gift-cards/a5-horizontal'.format(home, customer))
            os.mkdir('{}/{}-gift-cards/a6-portrait'.format(home, customer))
        except:
            shutil.rmtree("{}/{}-gift-cards".format(home, customer))
            os.mkdir('{}/{}-gift-cards'.format(home, customer))
            os.mkdir('{}/{}-gift-cards/a5-portrait'.format(home, customer))
            os.mkdir('{}/{}-gift-cards/a6-horizontal'.format(home, customer))
            os.mkdir('{}/{}-gift-cards/a5-horizontal'.format(home, customer))
            os.mkdir('{}/{}-gift-cards/a6-portrait'.format(home, customer))
            pass


class DeleteFolder():
    def __init__(self, home, customer, template_format):
        shutil.rmtree("./output")
        shutil.rmtree("./gift-codes")
        if template_format == 'a5_horizontal':
            shutil.rmtree('{}/{}-gift-cards/a5-portrait'.format(home, customer))
            shutil.rmtree('{}/{}-gift-cards/a6-horizontal'.format(home, customer))
            shutil.rmtree('{}/{}-gift-cards/a6-portrait'.format(home, customer))
        elif template_format == 'a5_portrait':
            shutil.rmtree('{}/{}-gift-cards/a5-horizontal'.format(home, customer))
            shutil.rmtree('{}/{}-gift-cards/a6-horizontal'.format(home, customer))
            shutil.rmtree('{}/{}-gift-cards/a6-portrait'.format(home, customer))
        elif template_format == 'a6_horizontal':
            shutil.rmtree('{}/{}-gift-cards/a5-horizontal'.format(home, customer))
            shutil.rmtree('{}/{}-gift-cards/a5-portrait'.format(home, customer))
            shutil.rmtree('{}/{}-gift-cards/a6-portrait'.format(home, customer))
        else:
            shutil.rmtree('{}/{}-gift-cards/a5-horizontal'.format(home, customer))
            shutil.rmtree('{}/{}-gift-cards/a5-portrait'.format(home, customer))
            shutil.rmtree('{}/{}-gift-cards/a6-horizontal'.format(home, customer))
