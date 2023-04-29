import matplotlib.pyplot as plt
import mysql.connector
import numpy as np

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test1234",
  database="divar_test_house"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the SQL query to fetch values of a column
mycursor.execute("SELECT area FROM tehno_houses")

# Fetch all rows from the result set
results = mycursor.fetchall()

# Create an empty list to store the values
square_meters = []

# Iterate over the rows and append the values to the list
for row in results:
  square_meters.append(row[0])


mycursor2 = mydb.cursor()

# Execute the SQL query to fetch values of a column
mycursor2.execute("SELECT totalPrice FROM tehno_houses")

# Fetch all rows from the result set
results = mycursor2.fetchall()

# Create an empty list to store the values
prices = []

# Iterate over the rows and append the values to the list
for row in results:
  prices.append(row[0])

square_meters = np.array(square_meters)
prices = np.array(prices)

slope, intercept = np.polyfit(square_meters, prices, 1)

# Create a scatter plot
plt.scatter(square_meters, prices)

plt.plot(square_meters, slope*square_meters + intercept, 'r')


# Add axis labels and title
plt.xlabel('Square Meters')
plt.ylabel('House Price')
plt.title('House Prices vs. Square Meters')

# Show the plot
plt.show()
