import shutil, os
import os
import subprocess

PROJECTS_DIR = "C://Users/alhlv/Desktop/Projects"
cwebp = f"{PROJECTS_DIR}/libwebp-1.3.0-windows-x64/bin/cwebp.exe"

# Specify original format
orig_ext = "jpg"

# Define directory with files to convert
WORKING_DIR = f"{PROJECTS_DIR}/new-hanafuda/public/cards/hanamaki"

# Define output directory for converted files
OUTPUT_DIR = f"{WORKING_DIR}/webp"

os.chdir(WORKING_DIR)
for filename in os.listdir(f'{WORKING_DIR}/{orig_ext}'):
    new_filename = f'{filename[:-4]}.webp'
    # print(new_filename)
    subprocess.call([cwebp, '-q', '100', f'{orig_ext}/{filename}', '-o', f'webp/{new_filename}', '-resize', '120', '0'])

names = [
    "matsu-ni-tsuru", "matsu-no-tan", "matsu-no-kasu-1", "matsu-no-kasu-2",
    "ume-ni-uguisu", "ume-no-tan", "ume-no-kasu-1", "ume-no-kasu-2",
    "sakura-ni-maku", "sakura-no-tan", "sakura-no-kasu-1", "sakura-no-kasu-2",
    "fuji-ni-kakku", "fuji-no-tan", "fuji-no-kasu-1", "fuji-no-kasu-2",
    "ayame-ni-yatsuhashi", "ayame-no-tan", "ayame-no-kasu-1", "ayame-no-kasu-2",
    "botan-ni-chou", "botan-no-tan", "botan-no-kasu-1", "botan-no-kasu-2",
    "hagi-ni-inoshishi", "hagi-no-tan", "hagi-no-kasu-1", "hagi-no-kasu-2",
    "susuki-ni-tsuki", "susuki-ni-kari", "susuki-no-kasu-1", "susuki-no-kasu-2",
    "kiku-ni-sakazuki", "kiku-no-tan", "kiku-no-kasu-1", "kiku-no-kasu-2",
    "momiji-ni-shika", "momiji-no-tan", "momiji-no-kasu-1", "momiji-no-kasu-2",
    "yanagi-ni-ono-no-toufuu", "yanagi-ni-tsubame", "yanagi-no-tan", "yanagi-no-kasu",
    "kiri-ni-ho-oh", "kiri-no-kasu-1", "kiri-no-kasu-2", "kiri-no-kasu-3",
]

reversed_names = [
    "matsu-no-kasu-2", "matsu-no-kasu-1", "matsu-no-tan", "matsu-ni-tsuru", 
    "ume-no-kasu-2", "ume-no-kasu-1", "ume-no-tan", "ume-ni-uguisu", 
    "sakura-no-kasu-2", "sakura-no-kasu-1", "sakura-no-tan", "sakura-ni-maku", 
    "fuji-no-kasu-2", "fuji-no-kasu-1", "fuji-no-tan", "fuji-ni-kakku", 
    "ayame-no-kasu-2", "ayame-no-kasu-1", "ayame-no-tan", "ayame-ni-yatsuhashi", 
    "botan-no-kasu-2", "botan-no-kasu-1", "botan-no-tan", "botan-ni-chou", 
    "hagi-no-kasu-2", "hagi-no-kasu-1", "hagi-no-tan", "hagi-ni-inoshishi", 
    "susuki-no-kasu-2", "susuki-no-kasu-1", "susuki-ni-kari", "susuki-ni-tsuki", 
    "kiku-no-kasu-2", "kiku-no-kasu-1", "kiku-no-tan", "kiku-ni-sakazuki", 
    "momiji-no-kasu-2", "momiji-no-kasu-1", "momiji-no-tan", "momiji-ni-shika", 
    "yanagi-no-kasu", "yanagi-no-tan", "yanagi-ni-tsubame", "yanagi-ni-ono-no-toufuu", 
    "kiri-no-kasu-3", "kiri-no-kasu-2", "kiri-no-kasu-1", "kiri-ni-ho-oh", 
]

modern_order = [
    "matsu-no-kasu-2",
    "matsu-no-kasu-1",
    "matsu-no-tan",
    "matsu-ni-tsuru",
    "ume-no-kasu-2",
    "ume-no-kasu-1",
    "ume-no-tan",
    "ume-ni-uguisu",
    "sakura-no-kasu-2",
    "sakura-no-kasu-1",
    "sakura-no-tan",
    "sakura-ni-maku",
    "fuji-no-kasu-2",
    "fuji-no-kasu-1",
    "fuji-no-tan",
    "fuji-ni-kakku",
    "ayame-no-kasu-2",
    "ayame-no-kasu-1",
    "ayame-no-tan",
    "ayame-ni-yatsuhashi",
    "botan-no-kasu-2",
    "botan-no-kasu-1",
    "botan-no-tan",
    "botan-ni-chou",
    "hagi-no-kasu-2",
    "hagi-no-kasu-1",
    "hagi-no-tan",
    "hagi-ni-inoshishi",
    "susuki-no-kasu-2",
    "susuki-no-kasu-1",
    "susuki-ni-kari",
    "susuki-ni-tsuki",
    "kiku-no-kasu-2",
    "kiku-no-tan",
    "kiku-ni-sakazuki",
    "kiku-no-kasu-1",
    "momiji-no-kasu-2",
    "momiji-no-kasu-1",
    "momiji-no-tan",
    "momiji-ni-shika",
    "yanagi-ni-tsubame",
    "yanagi-no-tan",
    "yanagi-ni-ono-no-toufuu",
    "yanagi-no-kasu",
    "kiri-no-kasu-3",
    "kiri-ni-ho-oh",
    "kiri-no-kasu-2",
    "kiri-no-kasu-1",
]

images = os.listdir(f'{OUTPUT_DIR}')
os.chdir(OUTPUT_DIR)
for index, value in enumerate(names):
    shutil.move(images[index], f"{value}.webp")
    # print((f'0{index+1}' if index < 9 else index + 1), images[index], value)
