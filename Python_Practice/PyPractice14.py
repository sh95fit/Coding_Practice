# 클래스 활용 실습

#실습 문제 1
'''
영철은 스타트게임즈 회사에 개발자로 취직을 하게 되었다.
지난주 회의 결과로 신작 MMORPG 게임의 아이템 구성안을 만들었다.

아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기
장비 아이템 : 착용효과, 착용하기
소모품 아이템 : 사용효과, 사용하기

(단, 버리기는 버릴 수 있는 아이템만 가능하다)
그리고 구성안을 토대로 클래스 다이어그램을 설계하였다.

구성안과 설계도를 보고 클래스 코드로 완성해보자
(메서드 구현은 자유롭게 한다)
부모 클래스 - Item / 매개변수 : name, price, weight, isdropable / 메서드 sale() : None, discard() : None
자식 클래스1 - WearableItem / 매개변수 : effect / 메서드 wear() : None
자식 클래스2 - UsableItem / 매개변수 : effect / 메서드 use() : None
'''

class Item :
    def __init__(self, name, price, weight, isdropable) :
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def sale(self) :
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    def discard(self) :
        if self.isdropable :
            print(f"[{self.name}] 버렸습니다.")
        else :
            print(f"[{self.name}] 버릴 수 없습니다.")

class WearableItem(Item) :
    def __init__(self, name, price, weight, isdropable, effect) :
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self) :
        print(f"[{self.name}]을 착용했습니다. 효과 : {self.effect}")

class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f"[{self.name}]을 사용했습니다. 효과 : {self.effect}")

#인스턴스 생성(WearableItem)
sword = WearableItem("목검", 30000, 3.5, True, "체력 100 증가, 마력 100 증가")
sword.wear()
sword.sale()
sword.discard()

#인스턴스 생성(UsableItem)
potion = UsableItem("빨간물약", 50, 0.1, False, "체력 50 회복")
potion.discard()
potion.use()
potion.sale()



