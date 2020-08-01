import base64

text='Hello world'

byte_text_encode=text.encode('ascii')

base64_bytes=base64.b64encode(byte_text_encode)

base_text_decode=base64_bytes.decode('ascii')

print(base_text_decode,byte_text_encode,base64_bytes)

base64_bytes = base_text_decode.encode('ascii')
text_bytes = base64.b64decode(base64_bytes)
strings = text_bytes.decode('ascii')
print(strings)