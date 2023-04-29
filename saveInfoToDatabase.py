import mysql.connector


def save_house_info(info):
    cnx = mysql.connector.connect(
        user='root',
        password='test1234',
        host='localhost',
        database='divar_test_house')

    cursor = cnx.cursor()



    insert_query = ("insert into tehno_houses "
                    "(title, exact_date, area, year, number_of_rooms, elevator, parking, cellar, totalPrice, price, floor, short_link, details)"
                    "value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    cursor.execute(insert_query,
                   (info['title'],
                    info['exactDate'],
                    info['area'],
                    info['year'],
                    info['number_of_rooms'],
                    info['elevator'],
                    info['parking'],
                    info['cellar'],
                    info['totalPrice'],
                    info['price'],
                    info['floor'],
                    info['shortLink'],
                    info['details']))

    cnx.commit()
    cursor.close()
    cnx.close()
