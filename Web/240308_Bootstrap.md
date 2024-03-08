# Bootstrap

css 프론트엔드 프레임워크

미리 만들어진 다양한 디자인 요소들을 제공하여 웹사이트를 빠르고 쉽게 개발할 수 있도록 함

### CDN(Content Delivery Network)

지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술

- 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화(웹페이지 로드 속도를 높임)
- 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

### bootstrap

- `<p class='mt-5'>Hello, world!</p>`  → mt-5: {property}{sides}-{size}
- 클래스 이름으로 Spacing을 표현하는 방법
    - property
        - m : margin
        - p : padding
    - sides
        - t : top
        - b : bottom
        - s : left
        - e : right
        - y : top, bottom
        - x : left, right
        - blank : 4 sides
    - size
        - 0 : 0 rem : 0 px
        - 1 : 0.25 rem : 4 px
        - 2 : 0.5 rem : 8 px
        - 3 : 1 rem : 16 px
        - 4 : 1.5 rem : 24 px
        - 5 : 3 rem : 48 px
        - auto : auto : auto
        

bootstrap에는 특정한 규칙이 있는 클래스 이름으로 스타일 및 레이아웃이 미리 작성되어 있음

## Reset CSS

모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트

- HTML elemet, table, list등의 요소들에 일관성있게 스타일을 적용시키는 기본 단계
- 브라우저는 각자의 user agent stylesheet를 가지고 있음
    - 문제는 이 설정이 브라우저마다 상이함
- 모든 브라우저에서 웹사이트를 동일하게 보이게 만들어야 하는 개발자에겐 골치아픈 일!!!
    
    → 모두 똑같은 스타일 상태로 만들고 스타일 개발 시작!!!!
    

- Normalize CSS
    - reset css 방법 중 대표적인 방법
    - 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법
- bootstrap에서는 bootstrap-reboot.css라는 파일명으로 normalize.css를 자체적으로 커스텀해서 사용하고 있음

## bootstrap 활용

### typography

제목, 본문 텍스트, 목록 등

- display headings
    - 기존 heading보다 더 눈에 띄는 제목이 필요한 경우 (더 크고 약간 다른 스타일)
- inline text elements
    - HTML inline 요소에 대한 스타일
- lists
    - HTML list 요소에 대한 스타일

### colors

색상 시스템

text, border, background 및 다양한 요소에 사용하는 bootstrap의 색상 키워드

- text colors
- background colors

### component

UI 관련 요소 ( UI = 버튼, 네비게이션 바, 카드, 폼, 드롭다운)

- Alerts
- Badges
- Buttons
- Cards
- Navbar
- carousel
    - id값과 각 버튼의 data-bs-target이 같은지 확인해야한다!!!!
- modal
    - modal id 값과 버튼의 data-bs-target이 각각 올바르게 일치하는지 확인해야함!!!!
    - 주의사항 
      1. modal 코드와 button 코드가 반드시 함께 다닐 필요는 없다
      2. modal 코드가 다른 코드 안쪽에 중촙되어 들어가버리면 modal이 켜졌을때 회색 화면 뒤로 감쳐질 수 있음
      3. modal 코드는 주로 body태그가 닫히는 곳에 모아두는 것을 권장

- 이점 : 일관된 디자인을 제공하여 웹사이트의 구성 요소를 구축하는 데 유용하게 활용

## 참고

- bootstrap 사용하는 이유
    - 가장 많이 사용되는 CSS 프레임워크
    - 사전에 디자인된 다양한 컴포넌트 및 기능
        - 빠른 개발과 유지보수
    - 손쉬운 반응형 웹 디자인 구현
    - 커스터마이징이 용이
    - 크로스 브라우징 지원
        - 모든 주요 브라우저에서 작동하도록 설계되어 있음
    - 자유도가 제한되기는 함…

## semantic web

웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

### Semantic in HTML

- HTML 요소가 의미를 가진다는 것
    
    `<p style="font-size: 30px;">Heading</p>` : 단순히 제목처럼 보이게 큰 글자로 만드는 것
    
    `<h1>Heading</h1>` : 페이지 내 최상위 제목이라는 의미를 제공하는 요소 h1.
    
    - 브라우저에 의해 스타일이 지정됨
- HTML semantic element
    - 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소
    - 검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록

- 대표적인 semantic element
    - header
    - nav
    - main
    - article
    - section
    - aside
    - footer

### semantic in css

css를 효율적이고 유지보수가 용이하게 작성하기 위한 일련의 가이드라인

- OOCSS(Object Oriented CSS) : 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론
    - 기본 원칙
        1. 구조와 스킨을 분리
            - 구조와 스킨을 분리함으로써 재사용 가능성을 높임
            - 모든 버튼의 공통 구조를 정의 + 각각의 스킨(배경색, 폰트 색상)을 정의
        2. 컨테이너와 콘텐츠를 분리
            - 객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용
            - 스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 함
            - 콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지