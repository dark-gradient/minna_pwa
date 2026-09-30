import os
import urllib.request

DEST_DIR = "mock_tests"

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

files_to_download = [
    # 2012
    ("https://www.jlpt.jp/e/samples/pdf/N5-Mondai.pdf", "2012_N5_Mondai.pdf"),
    ("https://www.jlpt.jp/e/samples/pdf/N5-Kaitou.pdf", "2012_N5_Kaitou.pdf"),
    ("https://www.jlpt.jp/e/samples/pdf/N5-Choukai.pdf", "2012_N5_Choukai.pdf"),
    # 2018
    ("https://www.jlpt.jp/samples/pdf/N5-mondai.pdf", "2018_N5_Mondai.pdf"),
    ("https://www.jlpt.jp/samples/pdf/N5-kaitou.pdf", "2018_N5_Kaitou.pdf"),
    ("https://www.jlpt.jp/samples/pdf/N5-choukai.pdf", "2018_N5_Choukai.pdf"),
]

for url, filename in files_to_download:
    dest_path = os.path.join(DEST_DIR, filename)
    print(f"Downloading {url} to {dest_path}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
            out_file.write(response.read())
        print("Success.")
    except Exception as e:
        print(f"Failed: {e}")
