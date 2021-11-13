def print_book_info(title, author=None, year=None):
    if author and year:
        print(f'"{title}" was written by {author} in {year}')
    elif not author and year:
        print(f'"{title}" was written in {year}')
    elif author:
        print(f'"{title}" was written by {author}')
    else:
        print(f'"{title}"')
