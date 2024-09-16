with open(r'H:\Users\Haora\Pictures\img-230625064609-001.pdf', 'rb') as image_file:
    image_data = image_file.read()

with open('picture-1.PDF', 'wb') as source_file:
    source_file.write(image_data)