message = input("Please enter a string: ")
message_length = len(message)
mid = message_length // 2
first_half = message[:mid]
second_half = message[mid:]
capitalized_message = second_half.upper()
print(first_half + capitalized_message)

