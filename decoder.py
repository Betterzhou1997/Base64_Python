import base64

# 定义经过 Base64 编码的命令
import chardet

encoded_command = "aHR0cHM6Ly92YWxvcmFudG95dW4uY29tL3Rlc3R5YXBpb3pxd2V4ZC5leGU="


# 解码命令
decoded_command = base64.b64decode(encoded_command)
result = chardet.detect(decoded_command)
coding = result['encoding']
print(coding)
decoded_command = decoded_command.decode(encoding='utf-8', errors="ignore")

# 输出解码后的命令
print(decoded_command)
