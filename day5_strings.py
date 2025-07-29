def string_methods_demo():
    text = "  Data Engineering with Python is FUN!  "

    # Strip whitespace
    stripped = text.strip()
    print("Stripped:", repr(stripped))

    # Case transformations
    print("Lowercase:", stripped.lower())
    print("Uppercase:", stripped.upper())
    print("Title Case:", stripped.title())

    # Count and find
    print("Count of 'i':", stripped.count('i'))
    print("Index of 'Python':", stripped.find('Python'))

    # Replacement
    replaced = stripped.replace("FUN", "awesome")
    print("Replaced:", replaced)

    # Splitting and joining
    words = stripped.split()
    print("Words list:", words)
    joined = "-".join(words)
    print("Joined with hyphens:", joined)

def fstring_demo():
    language = "Python"
    version = 3.12
    tasks_completed = 5

    # Basic interpolation
    print(f"Learning {language} version {version} is exciting!")

    # Expressions inside f-strings
    print(f"Tasks done: {tasks_completed}. Next task in {7 - tasks_completed} days.")

    # Formatting numbers
    pi = 3.1415926535
    print(f"Pi rounded to 2 decimals: {pi:.2f}")

    # Multiline f-string
    user = "xerus"
    repo = "road_map"
    print(f'''
    User: {user}
    Repository: {repo}
    Status: 🚀 On track with Day 5
    ''')

def main():
    string_methods_demo()
    print("-" * 40)
    fstring_demo()

if __name__ == "__main__":
    main()
