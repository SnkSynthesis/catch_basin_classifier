import pandas as pd
import glob
import xml.etree.ElementTree as XMLElementTree

print("Converting to CSV...")
columns = ("filename", "class", "width", "height", "xmin", "ymin", "xmax", "ymax")
rows = []
for filename in glob.glob('data/*.xml'):
    parsed_obj = XMLElementTree.parse(filename)
    root = parsed_obj.getroot()
    filename = root.find("filename").text
    for obj in root.findall("object"):
        row = []
        row.append(filename)
        row.append(obj.find("name").text)  # name => class
        row.append(root.find("size").find("width").text)
        row.append(root.find("size").find("height").text)
        for i in obj.find("bndbox"):
            row.append(int(i.text))
        rows.append(row)

df = pd.DataFrame(rows, columns=columns)
df.to_csv("labels.csv", index=False)
print("Done.")