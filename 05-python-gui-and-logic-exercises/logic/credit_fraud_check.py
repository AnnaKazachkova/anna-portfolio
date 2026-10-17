"""Rule-based credit card fraud check.

Pseudocode
  TRY: ask for number of transactions today and purchase amount,
       raise ValueError for negative entries
  IF the transaction is not from the home country THEN fraud
  IF transactions > 5 OR purchase > 500 THEN verification required
     IF not confirmed THEN fraud alert, ELIF confirmed THEN approved
  ELSE approved
  EXCEPT ValueError: display the error
"""


def credit_fraud():
    try:
        transaction = int(input("how many transactions have been made today "))
        purchase_amounts = float(input("how much was the purchase "))
        if transaction < 0 or purchase_amounts < 0:
            raise ValueError("enter a non-negative number")

        location_match = input(
            "is the transaction from your home country? (yes/no) "
        ).strip().lower()
        if location_match == "no":
            print("fraud detected, account blocked")
            return

        if transaction > 5 or purchase_amounts > 500:
            print("verification required")
            verification = input("do you confirm the purchase? (yes or no) ").strip().lower()
            if verification not in ("yes", "no"):
                raise ValueError("wrong entry")
            if verification == "no":
                print("purchase is not confirmed -> fraud alert")
            else:
                print("approved")
        else:
            print("approved, transaction cleared")
    except ValueError as error:
        print("error:", error)


if __name__ == "__main__":
    credit_fraud()
