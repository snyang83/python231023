# DemoStr.py
strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p",7))
print(strB.startswith("python"))
print(strB.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isalnum())

data = "<<< spam and ham >>>"
result = data.strip("<>")
print(data)
print(result)
result2 = result.replace("spam","spam egg")
print(result2)
lst = result2.split()
print("리스트:", lst)
print("---다시 합치기---")
print(":).".join(lst))
print(" ".join(lst))