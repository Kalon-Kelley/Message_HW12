from message import *

#test1:
# Create the message.
wishList = Message("Annie", "Santa")
wishList.append("For Christmas, I would like:")
wishList.append("A surf board")
wishList.append("An Arduino programming kit")
wishList.append("World peace")

# Display its contents.
print(wishList.toString())

#test2:
# Create the message.
birthdayMessage = Message("Bob", "Jim")
birthdayMessage.append("Come celebrate my birthday!")
birthdayMessage.append("It will be at my house.")
birthdayMessage.append("This Friday, 6pm.")
birthdayMessage.append("We will have pizza!")

# Display its contents.
print(birthdayMessage.toString())
