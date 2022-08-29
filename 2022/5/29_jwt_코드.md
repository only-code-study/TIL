
# 다시 시작
Junggle프로젝트를 시작하고 많은 준비단계에 속하는 문서를 작성했어요. SequenceDiagram, ERD등 다양한 다이어그램과 함께, API명세서 등을 작성하면서 시간으 보냈네요. Junggle 프로젝트를 위해 공부한 내용 조금과 함께 다시 TIL과 블로그 활동을 하려고 합니다. 그 첫 단계로서 JWT로 단추를 끊고자 해요.
## JWT
JWT는 Json Web Token의 약자로 이름만 보았을 때는 Json을 토대로 Web에서 쓰이는 (보안을 위한)토큰으로 보이네요. 좀 더 자세하게 볼까요?

### JWT 너 누구니?
JWT는 뭘까요? 간단히 말하면 웹서버에서 유저의 접속 정보를 관리, 유지하기 위한 방안중 하나라고 생각하면 될꺼 같아요!

[jwt.io](https://jwt.io/) 를 들어가면 다음과 같은 사이트를 볼 수 있어요.
![[스크린샷 2022-08-29 오후 11.38.16.png]]
여기서 좌측에 있는게 JWT토큰이라는 거에요.

`.`으로 `HEADER`, `PAYLOAD`, `VERIFY SIGNATURE`세부분으로 나누어 관리해요. 좌측은 Base64로 encoding한 결과이고, 이를 decoding(verify signature 빼고)하면 우측처럼 나오게 되요.

명세로 꼭 필요한 것은 다음과 같아요.
- Header: alg(암호화 할 방식), type(type)
- payload: 서버에 보낼 데이터, 유효기간
- verify signature: base64로 인코딩한 Header, payload 그리고 SECRET KEY를 더한 후 서명 된 내용

### 그럼 JWT를 쓰면 무엇이 좋나요?
개발하기가 무엇보다도 편해요. 다른 보안 방식보다도 개념이 쉽고 기존에 있는 코드에 적용하기도 쉬워요.
다만 JWT를 한번 탈취당하면, 이를 알아차리더라도 취소를 하지 못하기 때문에 유요한 시간 동안은 마음것 다른 정보에 접근이 가능해요. 이를 방지하기 위해서, 비교적 시간이 긴 Refresh JWT과 짧은 시간의 Access JWT로 나누어 구분해요.  좀 더 자세하게 보려면 [카카오 로그인](https://developers.kakao.com/docs/latest/ko/kakaologin/common) 이나, [네이버 로그인](https://developers.naver.com/docs/login/api/api.md) 의 개발 문서를 참고하면 좀 더 이해하기 수월 할 꺼 같아요.
