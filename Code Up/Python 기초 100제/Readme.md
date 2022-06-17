### memo

```
# 16진수 정수로 인식하기
int(input(), 16)
```

```
# 16진수 대문자로 출력하기
print("%x".upper() % num)
```

```
# 유니코드를 정수로 변환
ord(input())
# 정수를 유니코드로 변환
chr(input())
```

```
나누기 /
몫 //
나머지 %
```

```
# 소수점 반올림
format(num, ".2f")
```

```
# 정수 list
num = list(map(int, sys.stdin.readline().split()))
# list 평균
sum(list)/len(list)
```

### 비스티스프 연산

몇 비트 시프트 할 것인지 입력  
<< 오른쪽에 0 추가  
\>\> 왼쪽에 양수일 경우 0 음수일 경우 1 추가, 오른쪽 1비트는 사라진다.

```
#비스시프트연산 : 두 배 값 출력
print(num<<1)
```
