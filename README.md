# py-tweet
python3 기반으로 제작한 트위터 트윗 제거기<br/>
twit remover <br/>
based on python3 + tweepy<br/>

# OS
i just tried on linux.<br/>
리눅스에서만 테스트 해봤음.<br/>

# usage(사용법)
본인 아이디, ip에 대해 api 사용 허가 키 값을 keys.py에 채워 넣는다. <br/>
그리고 아래와 같이 실행<br/>
python3 py-tweet.py<br/>


# 실행 예제
트윗 한 사람 :<br/>
 testerA<br/>
testerB에게 한 답멘<br/>
내용 :<br/>
 @testerB Wow its test ..<br/>
Delete? (y:delete,exit:exit, else any key:pass)<br/>
><br/>



# restricted condtion
한번에 탐라 글 20개씩만 조회한다.<br/>
full로 load 할려고 그래도, 20개 리드하고, next 호출하고 그런 방식으로 돌아감.<br/>
이건 통제 변인이 아님.<br/>
