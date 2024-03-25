import os
import requests
import shutil

SOURCE_DIR = "./source"
GOOGLE_CLOUD_ICONS_URL = "https://cloud.google.com/icons/files/google-cloud-icons.zip"


def download_file_name():
    return os.path.basename(GOOGLE_CLOUD_ICONS_URL)


def zip_file_path():
    return f"{SOURCE_DIR}/icon/{download_file_name()}"


def extract_dir_path():
    return f"{SOURCE_DIR}/icon/{os.path.splitext(download_file_name())[0]}"


def download():
    print(f"extract_dir_path: {extract_dir_path()}")
    data = requests.get(GOOGLE_CLOUD_ICONS_URL).content
    with open(zip_file_path, mode='wb') as file:
        file.write(data)


def extract():
    # 解凍
    shutil.unpack_archive(
        zip_file_path(),
        extract_dir_path(),
    )


def main():
    download()
    extract()


main()
