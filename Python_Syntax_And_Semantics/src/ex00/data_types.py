def data_types():
    int_var = 13
    str_var = "Radima"
    float_var = 3.14
    bool_var = True
    list_var = [13, 7]
    dict_var = {"name": "Radima", "height": 160}
    tuple_var = ("Radima", 160)
    set_var = {1, 2, 3, 4, 5}

    types_list = [
        type(int_var).__name__,
        type(str_var).__name__,
        type(float_var).__name__,
        type(bool_var).__name__,
        type(list_var).__name__,
        type(dict_var).__name__,
        type(tuple_var).__name__,
        type(set_var).__name__,
    ]
    print(f"[{', '.join(types_list)}]")


if __name__ == "__main__":
    data_types()
