# xmlExercise


## Different approaches to read huge xml file (Jun/Feb 2022):

* big_xml_open_function.py (simply by using open function)
* big_xml_class_based_iterator.py (by using class based iterator, but in the end it uses open function)
* big_xml_generator_mmap (by using class with generator implemented with mmap.mmap)


## Updates (Feb/March 2025):
* I see that initial exercise (Jun/Feb 2022) was lacking two important points
    * deeper understanding about how memory is used here
    * specific conclusions what was achieved here
* So, lets redo this exercise and learn something new about memory management in Python.
    * I get a little teary-eyed when I see my Python learning curve/path. Programming is vast area / Things are not easy :)
    * I have 326M XML file with geographical objects 'objects.xml' which I will be using here - it should be enough.


## big_xml_open_function.py / big_xml_class_based_iterator.py
  * open()
    * provides Iterator (not generator), and similar to generators it is not loading full file to RAM (unless you want)

  * using class based iterator, but in the end it uses open function

  * exercise was not correctly stated :)
    * there was not 'prove' that open provided Iterator works as expected ...
    * adding in loop 'lines.append(text_line)' causes RAM usage ...


## mmap (memory-mapped)
  * allows to load file directly to RAM memory => fast access without reading all file
  * mmap can be treated as mutable bytes => file can be modified by playing on mmap bytes 


## Areas for exploration:
  * open builtin function implementation (CPython), UNIX/Linux syscalls, libc
  * looking into mmap library, there can be interesting things
