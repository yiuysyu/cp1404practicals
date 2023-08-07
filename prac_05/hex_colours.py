COLOR_TO_NAME = {"Bright Lavender": "#BF94e4", "Bright Green": "#66ff00", "Bright Navy Blue": "#1974d2",
                 "Bright Ube": "#d19ef", "Bubble Gum": "#ffc1cc", "Buff": "#f0dc82", "Burgundy": "#800020",
                 "CadetBlue": "#5f9ea0", "Cameo Pink": "#efbbcc", "Canary": "#ffff99"}

while True:
    color_name = input("Please enter the color name: ")
    if not color_name:
        break

    try:
        code = COLOR_TO_NAME[color_name]
        print(f"{code}")
    except KeyError:
        print("Invalid name")
