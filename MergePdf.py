import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdflists):
    merger = PyPDF2.PdfFileMerger()
    for lists in pdflists:
        merger.append(lists)
    merger.write('Super.pdf')

pdf_combiner(inputs)