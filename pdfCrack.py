from pypdf import PdfWriter, PdfReader


def add_encryption(input_pdf, output_pdf, password):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(input_pdf)

    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])

    pdf_writer.encrypt(user_password=password, owner_pwd=None, use_128bit=True)

    with open(output_pdf, "wb") as fh:
        pdf_writer.write(fh)


# if __name__ == "__main__":
#     add_encryption(
#         input_pdf="testpdf.pdf",
#         output_pdf="testpdf_encrypted.pdf",
#         password="9610231433",
#     )


def crack_pdf(input_path, password):
    with open(input_path, "rb") as input_file:
        reader = PdfReader(input_file)

        for i in range(9999 + 1):
            suffix = str(i).rjust(4, "0")
            if reader.decrypt(password + suffix):
                print(f"password is: {password + suffix}")
                break


if __name__ == "__main__":
    # example usage:
    crack_pdf("encrypted.pdf", "700403")
