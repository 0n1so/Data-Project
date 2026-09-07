from pywebio.input import input, FLOAT, select
from pywebio.output import put_text
from pywebio import start_server


def post_weight():
    Length = input("Your Length(sm): ", type=FLOAT)
    Width = input("Your Width(sm): ", type=FLOAT)
    Height = input("Your Height(sm): ", type=FLOAT)

    DIM = (Length * Width * Height) / 4000
    DMI = (Length * Width * Height) / 5000

    FA = input("Your FA(kg): ", type=FLOAT)
    VW = select("Choice your VW:", options=["DIM", "DMI"])

    selected_vw = DIM if VW == "DIM" else DMI
    GW = max(FA, selected_vw)

    put_text(f"GW: {GW} kg")



if __name__ == '__main__':
    start_server(post_weight, port=8000, debug=True)
    