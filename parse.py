def parse(str):
    parts = str.split("英語")
    if(len(parts) == 1):
        return parts[0], ""
    jp = parts[0]
    jp = jp.replace("日本語", "")
    b = parts[1]
    return jp, b
