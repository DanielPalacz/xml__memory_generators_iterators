from _io import TextIOWrapper
from time import sleep


class XmlParser:

    def __init__(self, filename: str) -> None:
        self.xml_file: TextIOWrapper = open(filename, mode="r", encoding="utf-8")
        self.line_counter: int = 0

    def __iter__(self):
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.xml_file.close()

    def __next__(self):
        self.line_counter += 1
        return self.xml_file.readline()


if __name__ == "__main__":
    with XmlParser("Wpisy_Rpm.xml") as xml_file_iterator:
        for text in xml_file_iterator:
            print(xml_file_iterator.line_counter)
            sleep(1)
            print(text)
            print()
