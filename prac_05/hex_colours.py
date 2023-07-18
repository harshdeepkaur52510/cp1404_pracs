COLOURS_NAME = {"#0048ba": "Absolute Zero", "#00fff": "Aqua", "#f0ffff": "Azure1", "3000000": "Black",
                "#ffff99": "Canary", "#b06500": "Ginger", "#bebebe": "Gray", "#ff69b4": "HotPink", "#fffff0": "Ivory1",
                "#3eb489": "Mint"}
print(COLOURS_NAME)

colour_code = input("Enter colour: ")
while colour_code != "":
    if colour_code in COLOURS_NAME:
        print(colour_code, "is", COLOURS_NAME[colour_code])
    else:
        print("Invalid")
    colour_code = input("Enter colour: ")
