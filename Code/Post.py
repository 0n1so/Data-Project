from pywebio.input import input, FLOAT, select
from pywebio.output import put_text
from pywebio import start_server


def post_weight():
    length = input("Your Length(sm): ", type=FLOAT)
    width = input("Your Width(sm): ", type=FLOAT)
    height = input("Your Height(sm): ", type=FLOAT)

    dim = (length * width * height) / 4000
    dmi = (length * width * height) / 5000

    fa = input("Your FA(kg): ", type=FLOAT)
    vw = select("Choice your VW:", options=["DIM", "DMI"])

    selected_vw = dim if vw == "DIM" else dmi
    gw = max(fa, selected_vw)
    return gw


def duty():
    value = input("Your cost in €: ", type=FLOAT)
    if value > 150:
        value = value + (value - 150) * 0.32
    return value


def main():
    gw = post_weight()
    cost = duty()
    total = gw + cost
    put_text(f"Total check: {total:.2f} EUR")


if __name__ == '__main__':
    start_server(main, port=8000, debug=True)