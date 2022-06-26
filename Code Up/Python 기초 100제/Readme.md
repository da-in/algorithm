### memo

```
# 16진수 정수로 인식하기
int(input(), 16)
```

```
# 16진수 대문자로 출력하기
print("%x".upper() % num)
print(f'{format(n, "X")}')
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

<br/>

### 비트단위(bitwise) 연산자

**bitwise not**  
`~`  
**bitwise and**  
`&`  
**bitwise or**  
`|`  
**bitwise xor**  
`^`  
**bitwise left shift**  
`<<` 오른쪽에 0 추가  
**bitwise right shift**  
`>>` 왼쪽에 양수일 경우 0 음수일 경우 1 추가, 오른쪽 1비트는 사라진다.

```
#비트시프트연산 : 두 배 값 출력
print(num<<1)
```

<br/>

### 2의 보수법

1의 보수법은 +0과 -0이 같이 존재한다는 문제점이 있다.  
2의 보수법은 1의보수법에 +1을 한 것이다.  
1의 보수법은 0은 1로 1은 0으로 바꾸어주는 것이다.  
(1의 보수법으로 만든 두 수를 더하면 모든 비트가 1이 된다. 거기에서 1을 더하면 모든 비트가 0이된다!)

<br/>

### 3항 연산자

바로 해결 못한 문제 [CodeUp 6064](https://codeup.kr/problem.php?id=6064&rid=0)

```
# 3항 연산자 큰 수 출력하기
print(a if a>b else b)
```
