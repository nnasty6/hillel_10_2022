from uuid import UUID

from lesson_abc_providers import PayPalAPI


class User:
    def __init__(self, name: str) -> None:
        self.name = name


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


def authorize_in_paypal(user: User) -> UUID:
    token: UUID = PayPalAPI.get_token()
    # ...
    print(f"Authorized with PayPal... \n\tToken={token}")

    return token


def checkout_with_paypal(token: UUID, user: User, product: Product):
    print(
        f"{user.name} is buying {product.name} "
        f"for {product.price} $ with PayPal..."
    )


def checkout_with_stripe(token: UUID, user: User, product: Product):
    print(
        f"{user.name} is buying {product.name} "
        f"for {product.price} $ with Stripe..."
    )


def main():
    john = User(name="John")
    micro = Product(name="Razor", price=1000)
    payment_type = input("Enter payment type: ")

    if payment_type == "paypal":
        paypal_token: UUID = authorize_in_paypal(john)
        checkout_with_paypal(paypal_token, john, micro)
    if payment_type == "stripe":
        checkout_with_stripe(john, micro)


if __name__ == "__main__":
    main()
