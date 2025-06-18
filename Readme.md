## PDFtoCSV 

This is simple Python Script to convert pdf to csv file.

### How'to or Procedure

- Create Virtual Environment as it keeps thing tidy and clean.
`python3 -m venv pdftocsv`

- Install Required Pakages
`pip3 -r requirements.txt

# or 

pip install pdfplumber pandas
`

- Run the Script 
`python3 pdf_to_csv.py`


### Note

== This Script does not work for the image based pdfs. For them you need to first go through Optical Character Recognition applied to PDF documents, even after this the extration of data might be wrongly intended after extraction so one might need to manually fix it. ==


### Other 
The pre-process.py file help in modifying csv file by separating the text in column written in 2 line to 2 columns.
