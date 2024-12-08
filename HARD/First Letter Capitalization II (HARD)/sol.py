import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    converted = []
    original = []
    ids = []

    for _id, text in zip(user_content["content_id"] ,user_content["content_text"]):
        ids.append(_id)
        original.append(text)
        curr = ""
        for word in text.split():
            if "-" in word:
                word = word.split("-")
                placeholder = []
                for part in word:
                    placeholder.append(part[0].upper() + part[1:].lower())
                word = "-".join(placeholder)
            else:
                word = word[0].upper() + word[1:].lower()
            curr += word + " "
        converted.append(curr[:len(curr) - 1])

    return pd.DataFrame({"content_id": ids, "original_text": original, "converted_text": converted})
