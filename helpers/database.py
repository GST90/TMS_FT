import mysql.connector as mysql


class DB:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ""
        self.database = "litecart"
        self.port = "3307"
        self.conn = None
        self.cur = None

    def create_conn(self):
        db = mysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

        self.conn = db
        self.cur = self.conn.cursor()

    def check_order(self, order_name):
        self.cur.execute("SELECT name,quantity,price FROM lc_orders_items "
                         "ORDER BY id DESC LIMIT 1")

        order = self.cur.fetchone()
        assert order[0] == order_name and order[1] == 3 and order[2] == 20
