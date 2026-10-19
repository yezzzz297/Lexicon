Exercise 1

I would store the reviews inside the book document because they are shown together, if there are not too many reviews. I would store members separately and use their IDs because one member can borrow many books.

Exercise 2

One good thing is that the order keeps the product name used when the customer bought it, even if the name changes later. One bad thing is that copying the name uses more space and the copies may have different names later.

Exercise 11

The original function does not check what the user sends as the status. A user can send a MongoDB condition instead of a status like new, so the query can return all orders. The fixed function checks that the status is text and returns an empty list if it is not.

Exercise 14

The customer's name, email, phone number, and city are personal data. The customer ID, join date, and newsletter choice are also linked to the person. Using only customer_id in orders means there are fewer copies of the customer's details to remove when they ask to be deleted. We still need to check the ID because it can link the orders to that person. I would not copy the email and city into every order because this makes the personal data harder to update, protect, and delete.
