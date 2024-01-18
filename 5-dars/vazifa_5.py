def create_like_text(names):
    num_likes = len(names)
    if num_likes == 0:
        return "No one likes this"
    elif num_likes == 1:
        return f"{names[0]} likes this"
    elif num_likes == 2:
        return f"{names[0]} and {names[1]} like it"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]}, and {names[2]} like it"
    else:
        remaining_likes = num_likes - 2
        return f"{', '.join(names[:2])} and {remaining_likes} more like it"

likes = ["Javahir", "Boburjon", "Azizbek", "Ilyosbek","Diyorbek", "Murodjon"]
like_text = create_like_text(likes)
print(like_text)  # Output: "Javahir, Boburjon and 2 more like it"