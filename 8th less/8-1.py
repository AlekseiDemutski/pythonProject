# r - read
# a - append
# w - write
# x- create
# r+ - read and white

with open('text_files/python.jpg', 'rb') as file:
    with open('text_files/python_copy.jpg', 'wb') as wfile:
        chunk_size = 4096
        file_chunk = file.read(chunk_size)
        while len(file_chunk) > 0:
            wfile.write(file_chunk)
            file_chunk = file.read(chunk_size)