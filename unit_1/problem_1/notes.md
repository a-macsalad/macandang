### Be advised, the repl editor within the edX wants to see code without function definition, likes this:

```
vowels = "aeiou"
count = 0

for char in s:
    for vow in vowels:
        if char is vow:
            count += 1

print(count)
```

While I wrote it using a function definition (and typing):

```
def count_in_substring(text: str) -> int:
    count = 0

    for char in text:
        for vow in vowels:
            if char is vow:
                count += 1

    return count
```

Then, I refactored to use list comprehensions: 

```
def count_in_substring(text: str) -> int:
    final_count = [char for char in text if char in vowels]
    return len(final_count)
```