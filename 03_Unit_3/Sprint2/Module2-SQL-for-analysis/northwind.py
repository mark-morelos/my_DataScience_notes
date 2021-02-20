### Part 2 - The Northwind Database
# Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.
import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

cursor = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
most_exp = cursor.execute('SELECT ProductName, UnitPrice FROM Product \
    ORDER BY UnitPrice DESC LIMIT 10').fetchall()

print(most_exp)
"""
[('Côte de Blaye', 263.5), 
('Thüringer Rostbratwurst', 123.79), 
('Mishi Kobe Niku', 97), 
("Sir Rodney's Marmalade", 81), 
('Carnarvon Tigers', 62.5), 
('Raclette Courdavault', 55), 
('Manjimup Dried Apples', 53), 
('Tarte au sucre', 49.3), 
('Ipoh Coffee', 46), 
('Rössle Sauerkraut', 45.6)]
"""

# What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)

avg_age = cursor.execute("SELECT avg(HireDate -BirthDate) \
FROM Employee").fetchall()

print(avg_age[0][0])
# 37.22222222222222

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

cursor = conn.cursor()

### Part 3 - Sailing the Northwind Seas
# Using `sqlite3` in `northwind.py`, answer the following:
# What are the ten most expensive items (per unit price) in the database *and*
# their suppliers?
supplier_ten = cursor.execute("SELECT ProductName, UnitPrice, CompanyName \
FROM Product \
INNER JOIN Supplier on Supplier.Id = Product.SupplierID \
ORDER BY UnitPrice DESC LIMIT 10").fetchall()

print(supplier_ten)

"""[
('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'), 
('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), 
('Mishi Kobe Niku', 97, 'Tokyo Traders'), 
("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), 
('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'), 
('Raclette Courdavault', 55, 'Gai pâturage'), 
('Manjimup Dried Apples', 53, "G'day, Mate"), 
('Tarte au sucre', 49.3, "Forêts d'érables"), 
('Ipoh Coffee', 46, 'Leka Trading'), 
('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')
]"""

# What is the largest category (by number of unique products in it)?
large_category = cursor.execute("SELECT CategoryName, COUNT(DISTINCT Product.Id) \
FROM Product \
INNER JOIN Category on Category.Id = Product.CategoryID \
GROUP BY CategoryName \
ORDER BY COUNT(DISTINCT Product.Id) DESC LIMIT 1 ").fetchall()
print(large_category[0][0])
# Confections

conn.commit()
conn.close()

### Part 4 - Questions (and your Answers)

# In the Northwind database, what is the type of relationship between the 
# `Employee` and `Territory` tables?
### Answer: The relationship of the Employee and Territory tables is Many-to-Many
###         It shows that Employees can be in multiple territories, and vice versa
###         Another table (Employee Territories) links the two tables because of
###         this type of relationship.

# What is a situation where a document store (like MongoDB) is appropriate, and
# what is a situation where it is not appropriate?
### Answer: A document store like MongoDB is appropriate in dealing with large, varying
###         types of databases. For smaller scale databases, MongoDB and the likes
###         are inappropriate for use as a relational database would be more practical.

# What is "NewSQL", and what is it trying to achieve?
### Answer: NewSQL is a class of relational database management systems
###         that allows large databases to retain ACID guarantees. It is designed
###         to be used on multiple servers and achieves better results than
###         traditional SQL.