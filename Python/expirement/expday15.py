def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """
    # Get the two values in a list
    parts = user_input.split(",")
    print(parts, "List value")
    # Store the two values in variables 
    lower_bound = float(parts[0])
    upper_bound = float(parts[1])
    print(lower_bound)
    print(upper_bound)

    # Inject the values in a dictionary
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}


if __name__ =="__main__":
    user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10) : ")
    print(parse(user_input))