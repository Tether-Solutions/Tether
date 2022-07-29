import email, smtplib, ssl
from providers import PROVIDERS
import time
from report import EtherStream


class MessageSender:
    def __init__(self, provider: str):
        self.ether_data = EtherStream()
        self.provider = provider
        self.sender_credentials = ("cryptoanalyzerapikey@gmail.com", "nrcdalqekjkujvxp")

    def send_sms_via_email(
        self,
        number: str,
        message: str,
        provider: str,
        sender_credentials: tuple,
        subject: str = " ",
        smtp_server: str = "smtp.gmail.com",
        smtp_port: int = 465,
    ):
        sender_email, email_password = sender_credentials
        receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

        email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

        with smtplib.SMTP_SSL(
            smtp_server, smtp_port, context=ssl.create_default_context()
        ) as email:
            email.login(sender_email, email_password)
            email.sendmail(sender_email, receiver_email, email_message)

    def price_report(self, number: str):
        """Packages current Etherium info in a sms format

        Args:
            number(str): The target phone number of the sms message

        """
        # Preprocessing

        ether_price = round(self.ether_data.eth_price_report()['price_eth'], 2)
        eth_percent_change_hourly = round(self.ether_data.eth_price_report()['percent_change_hourly'] / 100, 4)

        if eth_percent_change_hourly > 0:
            # Message elements
            percentage_modifier = 1 - abs(eth_percent_change_hourly)
            previous_hour_price = round(percentage_modifier * ether_price, 2)

            message = f"Ethereum is up!\n from ${previous_hour_price} to ${ether_price} in the last hour ({eth_percent_change_hourly * 100}%)"
        else:
            percentage_modifier = 1 + abs(eth_percent_change_hourly)
            previous_hour_price = round(percentage_modifier * ether_price, 2)

            message = f"Ethereum is down!\n from ${previous_hour_price} to ${ether_price} in the last hour ({eth_percent_change_hourly * 100}%)"

        print("\nSending...")
        self.send_sms_via_email(number, message, self.provider, self.sender_credentials)
        print("\nSent")


if __name__ == "__main__":
    sender = MessageSender('T-Mobile')
    sender.price_report('8045479964')
