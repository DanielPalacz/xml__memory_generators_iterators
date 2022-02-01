import mmap


class XmlParser:

    def __init__(self, filename: str) -> None:
        self.xml_file = open(filename, mode="r", encoding="utf-8")
        self.memory_file = mmap.mmap(self.xml_file.fileno(), 0, access=mmap.ACCESS_READ)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.memory_file.close()
        self.xml_file.close()

    def __iter__(self):
        while True:
            yield self.memory_file[:]



def parser(xml):
    return "Slowo slow"

# w generatorach - leniwa ewaulacja -- plik jest wczytywany linia po linii
# w iteratorze obiekt cały wczytywany na raz (w obiektówce)


# open
# iterator
# generator
# generator + mmap

# +

if __name__ == "__main__":
    with XmlParser("Wpisy_Rpm.xml") as xml_file_iterator:
        for text in xml_file_iterator:
            print(text)

