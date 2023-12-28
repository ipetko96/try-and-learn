from pypdf import PdfReader


def crack_pdf(input_path, password):
    with open(input_path, "rb") as input_file:
        reader = PdfReader(input_file)

        for i in range(9999 + 1):
            suffix = str(i).rjust(4, "0")
            print(password + suffix)
            if reader.decrypt(password + suffix):
                print(f"password is: {password + suffix}")
                break


if __name__ == "__main__":
    crack_pdf("pdf.pdf", "")
