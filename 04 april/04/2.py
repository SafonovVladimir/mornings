import random


def generate_color_rgb() -> str:
    return "#%06x" % random.randint(0, 0xFFFFFF)


print(generate_color_rgb())
"#ffffff"
"#FffFffFf"
"#25a403"
"#000001"
