import imaplib

mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
mail.login("mmfazilkhan786@gmail.com", "ohai swqr htum ootl")
mail.select("inbox")
status, messages = mail.search(None, "ALL")
print(messages)
