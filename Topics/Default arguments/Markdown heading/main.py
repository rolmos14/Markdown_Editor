def heading(text, level=1):
    level = max(level, 1)
    level = min(level, 6)
    return level * "#" + " " + text
