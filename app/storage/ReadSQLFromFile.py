class ReadSQLFromFile():
    self.connection = sqlite3.connect(self.database)
    self.cursor = self.connection.cursor()
    with open(self.query) as queryfile:
        self.cursor.executescript(queryfile.read())
