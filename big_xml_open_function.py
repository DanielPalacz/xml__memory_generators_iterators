from _io import TextIOWrapper
import time
import os
import psutil
import pandas as pd

# below 'import pandas_bokeh' is needed, because it extends pandas
import pandas_bokeh


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
    with open("objects.xml", encoding="utf-8") as xml_file_read, open(
        out_name, "w"
    ) as out_file:
        out_file.write("Time, Used_Memory\n")
        pid = os.getpid()
        python_process = psutil.Process(pid)
        lines = []
        for line_number, text_line in enumerate(xml_file_read):
            # print(text_line)
            # lines.append(text_line)
            if not line_number % 50000:
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
        title="Used_Memory - only open() function used",
    )
