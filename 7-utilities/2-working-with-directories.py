from pathlib import Path


path=Path("../ecommerce")
test_path=Path("../test")

print(test_path.exists())

if test_path.exists():
    test_path.rmdir()
else:
    test_path.mkdir()

print(path.iterdir())

files=[p for p in path.iterdir()]
print(files)

directories=[p for p in path.iterdir() if p.is_dir()]
print("Dir:",directories)

