from _io import TextIOWrapper
from time import sleep


class XmlParser:

    def __init__(self, filename: str) -> None:
        self.xml_file: TextIOWrapper = open(filename, mode="r", encoding="utf-8")
        self.line_counter: int = 0
        self.file_position: int = 0

    def __iter__(self):
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.xml_file.close()

    def __next__(self) -> str:
        self.line_counter += 1
        text_line: str = self.xml_file.readline()
        if self.file_position == self.xml_file.tell():
            raise StopIteration
        self.file_position = self.xml_file.tell()
        return text_line


if __name__ == "__main__":
    with XmlParser("hello.txt") as xml_file_iterator:
        for text in xml_file_iterator:
            print(xml_file_iterator.line_counter)
            sleep(1)
            print(repr(text))
            print()
