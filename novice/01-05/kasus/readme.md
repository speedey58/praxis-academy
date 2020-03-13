1. Buat 2 buah file JSON dan XML, keduanya mempunyai struktur data dan isi yang sama.

    Diberikan data profiles dengan rincian sebagai berikut:

    Nama | Lokasi
    -----| -------------
    Ervan | Borobudur
    Agus | Dukun
    Kadek | Tabanan
    Robi | Negara

    Data di atas ditulis dalam bahasa json sbb:

```
{"profiles": [
  {"nama" : "Ervan", "lokasi" : "Borobudur"},
  {"nama" : "Agus", "lokasi" : "Dukun"},
  {"nama" : "Kadek", "lokasi" : "Tabanan"},
  {"nama" : "Robi", "lokasi" : "Negara"}
] }
```

    dalam bahasa XML sbb:

```
<profiles>
    <profile>
        <nama>Ervan</nama> <lokasi>Borobudur</lokasi>
    </profile>
    <profile>
        <nama>Agus</nama> <lokasi>Dukun</lokasi>
    </profile>
    <profile>
        <nama>Kadek</nama> <lokasi>Tabanan</lokasi>
    </profile>
    <profile>
        <nama>Robi</nama> <lokasi>Negara</lokasi>
    </profile>
</profiles>
```

2. Dengan menggunakan Python, baca data dalam masing-masing format tersebut, tampilkan isi data.

    dalam python data membaca profiles.json ditulis sbb:

```
import json

file_json = open('profiles.json')
data=json.loads(file_json.read())

print(data)
```
 
    dalam python data membaca profiles.xml ditulis sbb:
```
import re

file_xml = open("profiles.xml").read();

nama = re.findall('<nama>(.*)</nama>', file_xml)
print(nama)

lokasi = re.findall('<lokasi>(.*)</lokasi>', file_xml)
print(lokasi)
```

3. Bandingkan lama eksekusi untuk membaca file XML dan file JSON tersebut. Mana yang lebih cepat? Jelaskan mengapa demikian.

    lebih cepat eksekusi json dibanding xml karena script xml lebih panjang dibanding json
