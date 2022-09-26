"""*******************************************************
CS 104: Message
Description: message with sender recipient and body
Date: 12/4/2019
Author(s): Lucas Kelley
*******************************************************"""


class Message:
    def __init__(self, sender, recipient):
        self._sender = sender
        self._recipient = recipient
        self._body = ""

    def append(self, body):
        self._body = self._body + body + "\n"

    def toString(self):
        header = "From: " + self._sender + "\nTo: " + self._recipient + "\n"
        return header + self._body