import mysql.connector

try:
    # Contoh koneksi ke database MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='registrasi'
    )

    # Memeriksa apakah koneksi berhasil
    if connection.is_connected():
        print('Berhasil terhubung ke database MySQL')

#Menampilkan informasi jika koneksi gagal
except mysql.connector.Error as err:
    print(f'Error: {err}')

#Menutup koneksi database 
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('Koneksi ditutup')