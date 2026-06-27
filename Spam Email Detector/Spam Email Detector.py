# Simple Spam Email Detector

# List of spam words
spam_words = ["win", "free", "prize", "money", "click", "offer"]

# User input
email = input("Enter email message: ")

# Convert to lowercase
email = email.lower()

# Check spam
is_spam = False

for word in spam_words:
    if word in email:
        is_spam = True
        break

# Result
if is_spam:
    print("This is a SPAM email")
else:
    print("This is NOT a spam email")