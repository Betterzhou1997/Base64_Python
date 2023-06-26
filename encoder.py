import base64

# 要编码的字符串
text = "www.baidu.com"

# 将字符串编码成bytes类型
text_bytes = text.encode('utf-8')

# 对bytes类型进行base64编码
base64_bytes = base64.b64encode(text_bytes)

# 将base64编码后的bytes类型转换成字符串
base64_str = base64_bytes.decode('utf-8')

print(base64_str)
