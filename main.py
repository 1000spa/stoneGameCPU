"""from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)
"""
import random
def findNearNum(exList, values):
    answer = [0 for _ in range(2)] # answer 리스트 0으로 초기화

    minValue = min(exList, key=lambda x:abs(x-values))
    minIndex = exList.index(minValue)
    answer[0] = minIndex
    answer[1] = minValue
    if minValue > values:
      answer[1] = exList[answer[0]-1]
    return answer[1]

def cn(s):
  answer = 3
  losing = [1,5,9,13,17,21,25,29,33,37]
  if s in losing:
    answer = False
  else:
    answer = s-findNearNum(losing,s)
  return answer
stone = random.randint(16, 40)

print("마지막에 돌을 가져가는 사람이 집니다")
print("1인당 1개에서 3개의 돌을 가져갈 수 있습니다.")
while stone > 0:
  print(f"{stone}개의 돌이 있습니다. 당신의 차례입니다. 몇 개를 가져가시겠습니까?")
  a = int(input("1에서 3 사이의 수를 입력하세요(1,2,3): "))
  if not 1 <= a <= 3:
    print("저리가세요.")
    break
  else:
    stone -= a
    if stone <= 0:
      print("컴퓨터의 승리입니다.")
      break
    print(f"남은 개수는 {stone}개 입니다.")
    if cn(stone) != False:
      stone -= cn(stone)
    else:
      print("컴퓨터가 게임을 안하겠답니다. 당신의 승리입니다.")
      break
    if stone <= 0:
      print("당신의 승리입니다.")
      break
    print(f"컴퓨터가 3개를 가져갑니다. 남은 개수: {stone}")
    
