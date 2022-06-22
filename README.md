# py-tweet
python3 기반으로 제작한 트위터 트윗 제거기
twit remover 
based on python3 + tweepy

# OS
i just tried on linux.
리눅스에서만 테스트 해봤음.

# usage(사용법)
본인 아이디, 
ip에 대해 api 사용 허가 키 값을 keys.py에 채워 넣는다.
그리고 아래와 같이 실행
python3 py-tweet.py

# restricted condtion
한번에 탐라 글 20개씩만 조회한다.
full로 load 할려고 그래도, 20개 리드하고, next 호출하고 그런 방식으로 돌아감.
통제 변인이 아님.
