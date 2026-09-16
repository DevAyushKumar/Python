from pypdf import PdfWriter

listOfPdf = [r"Questions/pdf/file1.pdf", r"Questions/pdf/file2.pdf", r"Questions/pdf/file3.pdf"]

merge = PdfWriter()

for files in listOfPdf:
    merge.append(files)

merge.write("Questions/pdf/all_pdf_merged.pdf")

merge.close()

print("All the files are merged")