import PyPDF2

pdfiles = ['1.pdf','2.pdf']
merger =PyPDF2.PdfMerger()

for filename in pdfiles:
    pdf_file = open(filename,'rb')
    pdf_reder = PyPDF2.PdfReader(pdf_file)
    merger.append(pdf_reder)
pdf_file.close()
merger.write('output.pdf')