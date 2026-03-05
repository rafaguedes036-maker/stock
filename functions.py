from service import connect
def insert_product(name, category, price, quantity = 1, provider = None): #Create
    with connect().cursor() as cursor:
        cursor.execute('''
            INSERT INTO products (name, category, price, quantity, provider)
                       VALUES (%s, %s, %s, %s, %s)''',
                       (name, category, price, quantity, provider))
        


def list_products():   #Read
    with connect().cursor() as cursor:
        cursor.execute('SELECT * FROM products')
        return cursor.fetchall()
    


def update_product(id, name, category, price, quantity, provider):  #Update
    with connect().cursor() as cursor:
        cursor.execute('''
            UPDATE products
               SET name = %s, category = %s, price = %s, quantity = %s, provider = %s
             WHERE id = %s''',
             (name, category, price, quantity, provider, id))



def delete_product(id):  #Delete 
    with connect().cursor() as cursor:
        cursor.execute('DELETE FROM products WHERE id = %s', (id,))


    

