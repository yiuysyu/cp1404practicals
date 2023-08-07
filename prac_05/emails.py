"""
Emails
Estimate: 25 minutes
Actual:   40 minutes
"""

email_to_name = {}

while True:
    use_email = input("Email: ")
    if not use_email:
        break

    username = use_email.split('@')[0]
    name = username.title()

    yes_or_no = input(f"Is your name {name}? (Y/n) ").lower()

    if yes_or_no not in ['', 'y']:
        name = input("Name: ").title()

    email_to_name[use_email] = name

print("\nResults:")
for email, name in email_to_name.items():
    print(f"{name} ({email})")
