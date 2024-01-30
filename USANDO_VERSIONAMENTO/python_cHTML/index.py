
def find(id):
    with open(file="index.html", mode="r", encoding="utf8") as file:
        while True:
            row = file.readline()
            if id in row:
                print(row)
                break

find("nome")