def shipping_label(*args, greeting="hi", **kwargs):

    print(greeting)

    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "po_box" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('po_box')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('county')}")
    # for value in kwargs.values():
    #     print(value, end=" ")

shipping_label("Eng.", "Linus", "Bwana",
               greeting="Niaje",
               street="0618 Ruaraka.",
               po_box = "PO BOX 264",
               city = "Clay City",
               state="Kasarani",
               county="Nairobi")