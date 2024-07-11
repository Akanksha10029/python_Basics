# 2 syntax for error handling

file = open("youtube.txt","w")
try:
    file.write("Akanksha is the best")
finally:
    file.close()

    

with open("yt.txt","w") as file2:
    file2.write("Akanksha is the best")
