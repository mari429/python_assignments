# 1.	Write a Python program to find words which are greater than given length k?
txt = ''' Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]

Python consistently ranks as one of the most popular programming languages '''
txt1 = ""
for i in range(len(txt)):
    if (ord(txt[i].upper())>=65 and ord(txt[i].upper())<=90) or ord(txt[i].upper())==32:
        txt1 = txt1+txt[i]
txt2 = txt1.split()
words_greater_than = 15
for i in txt2:
    if len(i) > words_greater_than:
        print(i)