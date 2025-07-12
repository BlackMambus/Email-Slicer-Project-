def email_slicer(email):
    try:
        username, domain = email.split("@")
        return username, domain
    except ValueError:
        return None, None

def main():
    print("📧 Email Slicer")
    email = input("Enter your email address: ").strip()

    username, domain = email_slicer(email)

    if username and domain:
        print(f"👤 Username: {username}")
        print(f"🌐 Domain: {domain}")
    else:
        print("❌ Invalid email format. Please try again.")

if __name__ == "__main__":
    main()



