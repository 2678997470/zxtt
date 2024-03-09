import base64
import zlib
import pickle
encoded_data = input("请输入编码为USC2到ANSI的存档数据：")
decoded_data = base64.b64decode(encoded_data)
serialized_data = decoded_data
uncompressed_data = zlib.decompress(serialized_data)
text_data = str(uncompressed_data)
start_index = text_data.find("<saveXml")
end_index = text_data.find("</saveXml>", start_index) + len("</saveXml>")
extracted_text = text_data[start_index:end_index]
text_data =extracted_text
text_data = text_data.replace('\\n', '\n')
print(text_data)