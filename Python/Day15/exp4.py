import webbrowser

user_term = input("Enter a search term : ")
# even replace we can use
# user_term = input("Enter a search term : ").replace(" ", "+")
webbrowser.open(f"/www.google.com/search?q={user_term}")