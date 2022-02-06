from _io import TextIOWrapper
import time
import os
import psutil
import pandas as pd

# below 'import pandas_bokeh' is needed, because it extends pandas
import pandas_bokeh


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


def get_time() -> str:
    loc_time = time.localtime()
    loc_time_out = [
        "0" + time_elem if len(time_elem) == 1 else time_elem
        for time_elem in [
            str(loc_time.tm_hour),
            str(loc_time.tm_min),
            str(loc_time.tm_sec),
        ]
    ]
    return ":".join(loc_time_out)


if __name__ == "__main__":
    out_name = __file__.split("\\")[-1].split(".")[0] + ".csv"
    with XmlParser("Wpisy_Rpm.xml") as xml_file_iterator, open(
        out_name, "w"
    ) as out_file:
        out_file.write("Time, Used_Memory\n")
        pid = os.getpid()
        python_process = psutil.Process(pid)
        for line_number, text_line in enumerate(xml_file_iterator):
            print(text_line)
            if not line_number % 50:
                memory_use = python_process.memory_info()[0] / 2.0 ** 30
                # total memory used
                # out_file.write(get_time() + "," + str(psutil.virtual_memory()[2]))
                out_file.write(get_time() + "," + str(int(memory_use * 1024)))
                out_file.write("\n")

    df = pd.read_csv(out_name)
    print(df)
    df.plot_bokeh(
        kind="bar",
        x="Time",
        y=" Used_Memory",
        xlabel="Time",
        ylabel="Used_Memory",
        title="Used_Memory - Class Iterator based approach",
    )
