from pathlib import Path
from time import  ctime


path=Path("my-data.txt")
print("Stats",path.stat())
print(40*"-")
print("Creation Time",ctime(path.stat().st_ctime))

#  Read the data from file

data_from_file=path.read_text()
print("Data from File")
print(40*"-")
print(data_from_file)
print(40*"-")

# Write to a file

print(40*"-")
path_to_write=Path("some_data.txt")
path_to_write.write_text(data_from_file)
print(40*"-")
print("Done")