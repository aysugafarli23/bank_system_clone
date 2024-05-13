# Task bank sistemilə bağlıdı. 

# İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
# Metod olaraq 3 fərqli metoddan istifadə edəcəyik:
# Balansı artırmaq,  Pul çıxarmaq  və balansı göstərmək üçün metodlar.


# İkinci classımız isə kreditlə bağlıdır. 
# İlk classımızı bu classa inheritance eliyəcəyik və super initdən  istifadə edəcəyik.  
# Bu classda bizim 2 metodumuz olacaq. 
# Kredit vermək və kredit ödənişi. 
# Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.    
# Kredit götürüləcək məbləğ. Kredit sadəcə 1 il müddəti üçündür və faiz yoxdur (kreditinməbləği / 12=aylıq ödəniş).

class UserAccount():
    def __init__(self, iban, balance = 0):
        self.iban = iban
        self.balance = int(balance)
        
    def __str__(self):
        message = f"Your iban code:{self.iban} and your balance: {self.balance} AZN"
        return message
    
    def show_balance(self):
        return self.balance
        
    def add_balance(self, money):
        self.money = int(money)
        self.balance += self.money
    
    def take_balance(self, money):
        self.money = int(money)
        self.balance  -= self. money
        
        
class Credit(UserAccount):
    def __init__(self, iban, credit_amount):
        super().__init__(iban)
        self.credit_amount = int(credit_amount)
        
    def give_credit(self, credit_year):
        self.credit_year = int(credit_year)
          
          
    def monthly_amount(self):
        if self.credit_year == 1 :
            self.monthly_amount = self.credit_amount // 12
            self.success_message =  f"Sizə {self.credit_amount} AZN məbləğində kredit verile biler: {self.monthly_amount} AZN aylıq ödənişlə "
            return self.success_message
        else:
            return f"Zəhmət olmasa, kredit götürəcəyiniz {self.credit_year} il müddətini 1 il müddəti üçün yenidən nəzərə alın) "
    
 
 
user1 = Credit('8888888888',2000)
user1.give_credit(1)
print(user1.monthly_amount())
    
# user1 = UserAccount(5223639989457845, 56)
# print(f"Current user balance: {user1.show_balance()} AZN")
# user1.add_balance(40)
# print(f"Current user balance after the adding operation: {user1.show_balance()} AZN")
# user1.take_balance(20)
# print(f"Current user balance after the taking operation: {user1.show_balance()} AZN")

