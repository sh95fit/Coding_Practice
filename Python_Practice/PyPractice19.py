# 클래스 실습
'''
Player 클래스 구현
1) 속성 : 닉네임, 미네랄, 가스, 유닛리스트
2) 메서드 : 생산하기
    produce(이름, 미네랄, 가스, 체력, 방어막, 공격력)

    - Player의 미네랄과 가스가 충분한 경우
     -> 유닛 객체를 생성하고 유닛리스트에 추가한다
    - Player의 미네랄이 부족한 경우
     -> "미네랄이 부족합니다."를 출력
    - Player의 가스가 부족한 경우
     -> "가스가 부족합니다."를 출력

Tip! 클래스들 간의 관계

is-a 관계(상속관계를 의미함)
자식클래스 is-a 부모클래스
has-a 관계(포함관계를 의미함)
A has-a B   A는 B를 가지고 있다

'''

#유닛 정보
unit_info = {
    "probe" : {
        "name" : "프로브",
        "mineral" : 50,
        "gas" : 0,
        "hp" : 20,
        "shield" : 20,
        "damage" : 5
    },
    "zealot" : {
        "name" : "질럿",
        "mineral" : 100,
        "gas" : 0,
        "hp" : 100,
        "shield" : 60,
        "damage" : 16
    },
    "dragoon" : {
        "name" : "드라군",
        "mineral" : 125,
        "gas" : 50,
        "hp" : 100,
        "shield" : 80,
        "damage" : 20
    }
}

# 딕셔너리에서 유닛 정보 받아오기 - 테스트
#print(list(unit_info['dragoon'].values()))

# 유닛 클래스
class Unit :
    '''
    속성 : 이름, 체력, 방어막, 공격력
    '''
    def __init__(self, name, hp, shield, damage) :
        self.name = name
        self.hp = hp
        self.shield = shield
        self.damage = damage


# 플레이어 클래스
class Player :
    '''
    속성 : 닉네임, 미네랄, 가스, 유닛리스트
    메서드 : 유닛 생산하기
    '''
    def __init__(self, nickname, mineral, gas, unit_list=[]) :
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list

    def produce(self, name, mineral, gas, hp, shield, damage) : 
        if self.mineral - mineral < 0 :
            print("미네랄이 부족합니다.")
        elif self.gas - gas < 0 :
            print("가스가 부족합니다.")
        else :
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name, hp, shield, damage)
            self.unit_list.append(unit)
            print(f"[{name}]을(를) 생산합니다.")

# 플레이어 생성
player1 = Player("홍길동", 400, 50)

# 유닛 생성
player1.produce(unit_info['probe']['name'], unit_info['probe']['mineral'], unit_info['probe']['gas'], unit_info['probe']['hp'], 
                unit_info['probe']['shield'], unit_info['probe']['damage'])

# 유닛 생성
player1.produce(unit_info['zealot']['name'], unit_info['zealot']['mineral'], unit_info['zealot']['gas'], unit_info['zealot']['hp'], 
                unit_info['zealot']['shield'], unit_info['zealot']['damage'])

# 유닛 생성
player1.produce(unit_info['dragoon']['name'], unit_info['dragoon']['mineral'], unit_info['dragoon']['gas'], unit_info['dragoon']['hp'], 
                unit_info['dragoon']['shield'], unit_info['dragoon']['damage'])   


# 생성된 유닛 확인
for unit in player1.unit_list :
    print(f"[{unit.name}] 체력 : {unit.hp}, 방어막 : {unit.shield}, 공격력 : {unit.damage}")