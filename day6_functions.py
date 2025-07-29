def add(a, b):
    """Returns sum of a and b."""
    return a + b

def multiply(a, b=2):
    """Returns a * b; b defaults to 2."""
    return a * b

def append_item(item, lst=None):
    """Appends item to list, creating a new list if none provided."""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

def connect(host, port=5432, *, timeout=10, use_ssl=False):
    """Connect to a service with keyword-only timeout and ssl flags."""
    return f"Connecting to {host}:{port}, timeout={timeout}, ssl={use_ssl}"

def divide(a: float, b: float) -> float:
    """Divide a by b; raises if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def main():
    print("add(3,5):", add(3, 5))
    print("multiply(4):", multiply(4))
    print("multiply(4,5):", multiply(4, 5))
    print("append_item examples:", append_item(1), append_item(2))
    print(connect("db.example.com"))
    print(connect("db.example.com", timeout=20, use_ssl=True))
    print("divide(10,2):", divide(10, 2))

if __name__ == "__main__":
    main()
