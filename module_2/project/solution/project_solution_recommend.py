from prefect import flow


@flow(log_prints=True)
def recommend_shares(temp: float = 0):
    """A function that uses a highly sophisticated rule to determine how many shares of stock should be purchased.
    The function takes a parameter named temp,
    which consists of the next predicted temperature in New York City.
    The default argument value is 19 for now.
    If the value received is over 20,
    then the recommendation is to buy the same number of shares as the temperature times 1,000.
    So a temperature of 20 would lead to a recommendation to buy 20,000 shares.
    Again, this is not investment advice anyone should follow - but they're the client, right? 🤣
    The code prints, logs, and returns the recommend number of shares to purchase.
    """
    shares = 0
    if temp > 0:
        shares = temp * 1_000
    print(f"Model says: buy {shares} shares")
    return shares


if __name__ == "__main__":
    recommend_shares()
