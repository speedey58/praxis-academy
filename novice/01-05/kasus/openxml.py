import re

file_xml = open("profiles.xml").read();

nama = re.findall('<nama>(.*)</nama>', file_xml)
print(nama)

lokasi = re.findall('<lokasi>(.*)</lokasi>', file_xml)
print(lokasi)