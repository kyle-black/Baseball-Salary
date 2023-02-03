
def parenth(n):

    parenth_dict ={}
    for i in range(n):
        parenth_dict[f"{i}_left"] = "("
        parenth_dict[f"{i}_right"] = ")"
    print(parenth_dict)
    


parenth(3)