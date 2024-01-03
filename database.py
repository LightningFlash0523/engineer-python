class Database:
    def __init__(self):
        self.data = {}
        self.transactions = []

    def set(self, name, value):
        self.data[name] = value

    def get(self, name):
        return self.data.get(name, "NULL")

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def count(self, value):
        return list(self.data.values()).count(value)

    def begin(self):
        self.transactions.append(dict(self.data))

    def rollback(self):
        if self.transactions:
            self.data = self.transactions.pop()
        else:
            print("TRANSACTION NOT FOUND.")

    def commit(self):
        self.transactions = []

    def execute_command(self, command):
        parts = command.split()
        operation = parts[0]

        if operation == "SET":
            self.set(parts[1], parts[2])
        elif operation == "GET":
            print(self.get(parts[1]))
        elif operation == "DELETE":
            self.delete(parts[1])
        elif operation == "COUNT":
            print(self.count(parts[1]))
        elif operation == "BEGIN":
            self.begin()
        elif operation == "ROLLBACK":
            self.rollback()
        elif operation == "COMMIT":
            self.commit()
        elif operation == "END":
            exit()

def main():
    db = Database()

    while True:
        command = input("Enter command: ")
        db.execute_command(command)

if __name__ == "__main__":
    main()
