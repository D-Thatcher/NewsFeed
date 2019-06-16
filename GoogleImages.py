import time
lot = []
init = time.time()

def tick(description):
    lot.append([time.time() - init, description])

tick('Starting')
import json
import itertools
import os
import uuid
from urllib.request import urlopen, Request
from PIL import Image
from PIL import ExifTags
from bs4 import BeautifulSoup
tick('Imports')





REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.331.134 Safari/533.36"}


def get_soup(url, header):
    response = urlopen(Request(url, headers=header))
    return BeautifulSoup(response, 'html.parser')

def get_query_url(query):
    return "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query

def extract_images_from_soup(soup):
    image_elements = soup.find_all("div", {"class": "rg_meta"})
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    return link_type_records

def extract_images(query, num_images):
    url = get_query_url(query)
    soup = get_soup(url, REQUEST_HEADER)
    link_type_records = extract_images_from_soup(soup)
    return itertools.islice(link_type_records, num_images)

def get_raw_image(url):
    req = Request(url, headers=REQUEST_HEADER)
    resp = urlopen(req)
    return resp.read()

def save_image(raw_image, image_type, save_directory):
    extension = image_type if image_type else 'jpg'
    file_name = uuid.uuid4().hex
    save_path = os.path.join(save_directory, file_name+'.'+extension)
    with open(save_path, 'wb') as image_file:
        image_file.write(raw_image)


    # exifData = {}
    # img = Image.open(save_path)
    # exifDataRaw = img._getexif()
    # print(exifDataRaw)
    # for tag, value in exifDataRaw.items():
    #     decodedTag = ExifTags.TAGS.get(tag, tag)
    #     exifData[decodedTag] = value
    # print(exifData)

def download_images_to_dir(images, save_directory, num_images):
    for i, (url, image_type) in enumerate(images):
        try:
            raw_image = get_raw_image(url)
            save_image(raw_image, image_type, save_directory)
        except Exception as e:
            print(e)

def run(query, save_directory, num_images=40):
    query = '+'.join(query.split())
    images = extract_images(query, num_images)
    download_images_to_dir(images, save_directory, num_images)

def main():
    run(" caption", r"C:\Users\Dan\Desktop\view\ggl")

tick('Definitions')

main()
tick('Finished')

for i,j in lot:
    print(i)
    print(j)