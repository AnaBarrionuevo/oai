import asyncio

from input_images import IMAGE_URLS
from oai_image_alt import generate_image_alts

if __name__ == "__main__":
    print(asyncio.run(generate_image_alts(IMAGE_URLS)))
