# https://www.acmicpc.net/problem/10167

# 금광 
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 3 초	256 MB	2741	791	483	27.304%

# 문제

# 황금의 땅이라는 별명을 가진 나라가 있다. 
# 이 나라에는 개발 되지 않은 많은 금광들이 존재한다. 
# 이 금광들을 지도상에 표시할 때, 평면상의 점들로 표현한다. 


# 각 점 pi에는 양수 또는 음수의 정수 값 wi가 주어진다. 
# 이 wi는 금광을 개발한다면 얻게 되는 이익 또는 손해를 나타낸다. 
# wi가 양수이면, wi만큼의 이익이 발생함을 나타낸다. 
# wi가 음수이면, |wi| 만큼의 손해가 발생함을 나타낸다. 

# 금광 개발업자는 x축 또는 y축과 평행한 변들을 가진 직사각형 모양의 땅 R을 사서 R에 포함된 금광들을 모두 개발할 것이다. 
# 이때 금광들을 개발하여 얻게 되는 개발 이익은 금광들의 wi들의 합이다. 
# 개발업자는 R에 포함된 금광들의 개발 이익이 최대가 되는 직사각형 영역 R을 찾을 것이다. 
# 예를 들어서, 위의 그림-1에서 개발 이익이 최대가 되는 영역 R은 그림-2에서 보여 지는 것과 같고 개발 이익은 7이다. 
# 금광들의 좌표와 금광을 개발하면 얻게 되는 이익 또는 손해가 주어질 때, 직사각형 모양의 땅을 사서 얻게 되는 최대 개발 이익을 출력하는 프로그램을 작성하시오.


# 그림-2

# 입력
# 첫 줄에는 금광들의 개수 N (1 ≤ N ≤ 3,000)이 주어진다. 이어지는 N개의 줄 각각에는 금광의 좌표 (x, y)를 나타내는 음이 아닌 두 정수 x와 y(0 ≤ x, y ≤ 109), 그리고 금광을 개발하면 얻게 되는 이익 또는 손해를 나타내는 정수 w(-109 ≤ w ≤ 109)가 주어진다. 금광의 좌표는 모두 서로 다르며 w > 0인 금광은 적어도 하나 존재한다.

# 출력
# 출력은 한 줄로 이루어진다. 금광 개발업자가 직사각형 모양의 땅 R을 사서 얻을 수 있는 최대 개발 이익을 출력한다. 계산 과정에서 32비트 정수 변수가 표현할 수 있는 범위를 넘어서 64비트 정수 변수(long long type)를 사용해야 할 수도 있음에 주의하라.

# 서브태스크
# 번호	배점	제한
# 1	11	
# N ≤ 100

# 2	23	
# N ≤ 500

# 3	9	
# wi < 0인 점은 단 하나만 존재한다.

# 4	15	
# 모든 점들에 대해서 y = 0이다.

# 5	42	
# 원래의 제약조건 이외에 아무 제약조건이 없다.

# 예제 입력 1 
# 7
# 2 8 2
# 5 5 3
# 3 3 -1
# 10 2 5
# 9 7 -2
# 6 7 -1
# 7 3 -1
# 예제 출력 1 
# 7
# 예제 입력 2 
# 10
# 4 9 2
# 6 10 -1
# 6 8 3
# 5 6 5
# 8 5 10
# 7 6 -7
# 9 10 4
# 20 1 1
# 10 8 6
# 10 6 -5
# 예제 출력 2 
# 18
