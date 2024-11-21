def first(n1, n2):
    print("첫 번째 함수 실행중 a = %d, b = %d" % (n2, n1))
    print("첫 번째 함수 실행후 a = %d, b = %d" % (n1, n2))

def second(n1, n2):
    print("두 번째 함수 실행중 a = %d, b = %d" % (n2, n1))
    print("두 번째 함수 실행후 a = %d, b = %d" % (n2, n1))

num1, num2 = map(int, input("두 수를 입력하세요. ").split())
first(num1, num2)
second(num1, num2)