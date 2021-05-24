

def get_email_from_message(message):
    lines = message.split('\n')
    email = ""

    for line in lines:
        if line.startswith("email:"):
            email = line.split(":")[1].strip()
            break

    return email
