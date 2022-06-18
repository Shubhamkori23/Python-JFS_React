# decorators are used to add functionality to an existing code.

# a function can be nested inside another function it can also be returned
def outer_function():
    # Assign task to student

    task = 'Read Python book chapter 3.'

    def inner_function():
        print(task)

    return inner_function


homework = outer_function()
homework()


# A function can be passed to another function as an argument
def friendly_reminder(func):
    func()
    print('Don\'t forget to bring your wallet!')


def action():
    print('I am going to the store to buy you something nice.')


# Calling the friendly_reminder function with the action function used as an argument.

friendly_reminder(action)
