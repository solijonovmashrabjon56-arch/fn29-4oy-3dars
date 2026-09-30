class User:
    def __init__(self, name, phone, balance):
        self.name = name
        self._phone = phone
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, vel):
        if vel < 0:
            print("Balans manfiy bo'lishi mumkin emas!")
        else:
            self.__balance = vel

    def __str__(self):
        return f"{self.name}, Balance: {self.__balance} so'm"

    def __repr__(self):
        return f"User(name={self.name}, phone={self._phone})"

# ---------------------------------

class Client(User):
    def __init__(self, name, phone, balance, card_number):
        super().__init__(name, phone, balance)
        self.card_number = card_number

    def deposit(self, vel):
        if vel > 0:
            self.balance += vel
            print(f"{vel} so'm qoshildi balansga")
        else:
            print("Qoshilayotgan summa 0 dan katta bo'lishi kerak")


    def withdraw(self, vel):
        if vel <= 0:
            print("Yechib olinadigon summa 0 dan katta bo'lishi kerak")
        elif vel > self.balance:
            print("Hisobingizda mablag' yetarli emas!!")
        else:
            self.balance -= vel
            print(f"{vel} so'm muvaffaqiyatli yechildi")


    def info(self):
        print(f"Mijoz: {self.name}, Talefon: {self._phone}, Karta raqam: {self.card_number}, Balans: {self.balance}")

# ------------------------------

class Employee(User):
    def __init__(self, name, phone, balance, employee_id, salary):
        super().__init__(name, phone, balance)
        self.employee_id = employee_id
        self.salary = salary


    def work(self):
        print(f"{self.name} bank xodimi sifatida ishlayapti")


    def info(self):
        print(f"Xodim: {self.name}, Telefon: {self._phone}, Employee ID: {self.employee_id}, Maosh: {self.salary} so'm")

# -------------------------------

class Bank:
    def __init__(self):
        self.clients = []
        self.employees = []


    def add_clients(self, client):
        self.clients.append(client)


    def add_employees(self, employee):
        self.employees.append(employee)


    def show_client(self):
        print("\n--- BARCHA MIJOZLAR ---")
        for client in self.clients:
            print(client)


    def show_employee(self):
        print("\n--- BARCHA XODIMLAR ---")
        for employee in self.employees:
            print(employee)


    def find_client(self, vel):
        for client in self.clients:
            if client._phone == vel or client.card_number == vel:
                return client


        return None

# ----------------------------------

bank = Bank()


c1 = Client("Sobir", "901234567", 1500000, "8600123456789012")
c2 = Client("Vali", "902345678", 2000000, "8600234567890123")
c3 = Client("Hasan", "903456789", 1000000, "8600345678901234")


e1 = Employee("Toxir", "904567890", 0, "E111", 5000000)
e2 = Employee("Ali", "905678901", 0, "E222", 6000000)


bank.add_clients(c1)
bank.add_clients(c2)
bank.add_clients(c3)

bank.add_employees(e1)
bank.add_employees(e2)


print("\n--- DEPOSIT ---")
c1.deposit(500000)


print("\n--- WITHDRAW ---")
c2.withdraw(300000)


print("\n--- BALANS ---")
print(f"{c1.name} balansi: {c1.balance} so'm")
print(f"{c2.name} balansi: {c2.balance} so'm")


bank.show_client()


bank.show_employee()


print("\n--- POLIMORFIZM ---")

users = [
    c1,
    c2,
    e1,
    e2
]

for user in users:
    user.info()


print("\n--- WORK ---")
e1.work()
e2.work()


print("\n--- STR ---")
print(str(c1))

print("\n--- REPR ---")
print(repr(c1))


print("\n--- ENCAPSULATION ---")


print("Private __balance tashqaridan to'g'ridan-to'g'ri olinmaydi.")
print("Balans bilan property orqali ishlaymiz:", c1.balance)


print("\n--- FIND CLIENT ---")

found = bank.find_client("901234567")

if found:
    print("Mijoz topildi:")
    found.info()
else:
    print("Mijoz topilmadi.")