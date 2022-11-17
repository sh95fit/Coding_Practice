#리스트 내포 실습1
'''
리스트 내포를 사용해서 word_list에 들어 있는 문자열 중
첫 글자가 a인 것만 뽑아서 리스트로 만드세요.

변경 전
['apple', 'watch', 'apolo', 'star', 'abocado']

변경 후
['apple', 'apolo', 'abocado']
'''

list = ['apple', 'watch', 'apolo', 'star', 'abocado']

list = [i for i in list if i[0] == 'a']
print(list)


#리스트 내포 실습2
'''
리스트 내포를 사용해서 다음과 같이 변경해보자.

변경 전
['오메가', None, '비타민C500', None, '홍삼절편']

변경 후
['오메가', '비타민C500', '홍삼절편']

** 만약 if문 뿐만 아니라 else나 elif도 반영이 되어야 하는 경우 for문보다 앞에 쓴다!
'''

list = ['오메가', None, '비타민C500', None, '홍삼절편']

list = [i for i in list if i != None]
print(list)