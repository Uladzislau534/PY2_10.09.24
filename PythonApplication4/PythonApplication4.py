def count_unique_characters(message: str) -> int:
   
    unique_chars = set(filter(lambda c: c.isalpha(), map(lambda c: c.lower(), message)))
    return len(unique_chars)

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)

