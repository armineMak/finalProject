import random
import string


EMAIL_DOMAINS = ["mailinator.com", "yopmail.com"]
letters_digits = string.ascii_letters + string.digits
letters_for_account = string.ascii_letters


def get_random_name(letters_for_account, length):
    return ''.join(random.choice(letters_for_account) for _ in range(length))


def get_random_domain(EMAIL_DOMAINS):
    return random.choice(EMAIL_DOMAINS)


only_domain_gen = get_random_domain(EMAIL_DOMAINS)


def get_random_name(letters_digits, length):
    return ''.join(random.choice(letters_digits) for _ in range(length))


def generate_random_emails(length):
    return get_random_name(letters_digits, length) + '@' + only_domain_gen


def get_random_password(length):
    return ''.join((random.choice(letters_digits) for _ in range(length)))


def email_domains_link():
    mailinator_link = "https://www.mailinator.com/v3/#/#inboxpane"
    yopmail_link = "http://www.yopmail.com/en/"

    if only_domain_gen == "mailinator.com":
        return mailinator_link
    elif only_domain_gen == "yopmail.com":
        return yopmail_link


def replace_domain(url):
    change_link = url.replace("https://www.cinimi.com/", "http://35.173.232.240/")
    return change_link

