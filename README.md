# py-tweet
python3 기반으로 제작한 트위터 트윗 제거기<br/>
twit remover <br/>
based on python3 + tweepy<br/>
<br/>
<br/>
# 실행 환경
i just tried on linux.<br/>
리눅스에서만 테스트 해봤음.<br/>
<br/>
<br/>
# 사용법
본인 아이디, ip에 대해 api 사용 허가 키 값을 keys.py에 채워 넣는다. <br/>
그리고 아래와 같이 실행<br/>
python3 py-tweet.py<br/>
<br/>
<br/>
# 실행 예제
트윗 한 사람 :<br/>
 testerA<br/>
testerB에게 한 답멘<br/>
내용 :<br/>
 @testerB Wow its test ..<br/>
Delete? (y:delete,exit:exit, else any key:pass)<br/>
"><br/>
y 누르면 해당 트윗 지움<br/>
exit 누르면 프로그램 나감<br/>
다른키는 그냥 pass<br/>
<br/>
<br/>
# 제약 조건
트위터 api 자체가 한번에 탐라 글 20개씩만 조회한다.<br/>
full로 load 할려고 그래도, 20개 리드하고, next 호출하고 그런 방식으로 돌아감.<br/>
이건 통제 변인이 아님.<br/>
아마도 api 호출 때문에 리소스가 너무 시달리다보니 제약 걸어놓은것 같음.<br/>
<br/>
