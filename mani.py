def greet(name):
    return "Hello, " + name + "!"
def main():
    names = ["Mani", "Python", "World"]
    print("Greeting program")
    for name in names:
        message = greet(name)
        print(message)
    count = len(names)
    print("Total greetings:", count)
    print("Thank you!")
    print("Program finished.")
    print("Goodbye!")
if __name__ == "__main__":
    main()
