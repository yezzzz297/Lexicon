# Lab 7: Queries and updates

These solutions follow `Exercises_Queries_and_updates.pdf`.
Each exercise has its own Python file with short explanations.
Your earlier exercises remain in `../Lab_6/`.

## Run the exercises

Start your local MongoDB server, then open a terminal in this folder:

```sh
cd Databases/Lab_7
python3 -m pip install pymongo
python3 seed_webshop.py
python3 exercise_1.py
```

Change `exercise_1.py` to the exercise you want to run.
The seed script resets the webshop customers, products and orders.
Exercises 8–10 change data. Run them once in order, then run
`python3 seed_webshop.py` again to restore the practice data.
Running exercise 8 again increases prices by another 20 kr;
running exercise 10 again finds no matching orders after they were deleted.

## Expected results with fresh seed data

| Exercise | What you practise | Expected result |
| --- | --- | --- |
| 1 | `$gt`: greater than | 3 products |
| 2 | `$ne`: not equal | 8 orders |
| 3 | `$in`: one of several values | 3 customers |
| 4 | Dot notation in objects | 3 white products |
| 5 | Array matching and projection | 3 products, only name and tags |
| 6 | Sorting and limiting | Socks, Water Bottle, Beanie, Cap, T-shirt |
| 7 | Dot notation in arrays | Orders 4, 8, 10, 15 |
| 8 | `$inc`: increase a number | Cap 219, Water Bottle 169, Backpack 769, Beanie 199 kr |
| 9 | `$addToSet` and `$set` | Rain Jacket with new tag and current restock date |
| 10 | Count and delete with a filter | 2 matching orders, 2 deleted (12 and 13) |

In a query, `{}` means all documents. A projection chooses which fields
are returned; it does not change the stored document.
