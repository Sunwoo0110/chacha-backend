# ChaCha (Character Chat)

## 🪄 서비스 소개
캐릭터 인격 생성을 통한 캐릭터 채팅 서비스
- 프롬포트 엔지니어링을 통하여 사용자가 원하는 캐릭터의 이름, 소개, 상황, 성격 등을 설정하고, 해당 캐릭터와 자유롭게 대화를 나눌 수 있는 서비스입니다.

## 📌 주요 기능
<table>
  <tr>
    <td><img width="500" alt="image" src=https://github.com/TeamOTK/.github/assets/79784618/31f29dd8-6cdf-42d9-9fb4-56e3390ead71>
</td>
    <td><img width="500" alt="image" src=https://github.com/TeamOTK/.github/assets/79784618/c22e701c-daac-4852-bc45-b74f88434e78>
</td>
  </tr>
  <tr>
    <td align="center"><b>캐릭터 목록</b></td>
    <td align="center"><b>캐릭터 상세 설정 확인</b></td>
  </tr>
</table>
<table>
  <tr>
    <td><img width="500" alt="image" src=https://github.com/TeamOTK/.github/assets/79784618/a4080160-b32b-4598-bfb3-7d9ca4689eca>
</td>
    <td><img width="500" alt="image" src=https://github.com/TeamOTK/.github/assets/79784618/8e5049c8-dac8-48c8-9fd3-35b9b970676c>
</td>
  </tr>
  <tr>
    <td align="center"><b>캐릭터 생성</b></td>
    <td align="center"><b>캐릭터 대화</b></td>
  </tr>
</table>

## Skills & Frameworks
- Python
- FastAPI, MongoDB
- AWS EC2, AWS S3

## 프로젝트 구조
```
backend/
├── app/
│   ├── main.py              # FastAPI 엔트리 포인트
│   ├── models/              # 데이터베이스 모델 정의
│   ├── schema/              # 스키마 정의
│   ├── controller/          # CRUD 로직 구현
│   ├── routers/
│   │   ├── __init__.py      
│   │   ├── users.py         # 사용자 관련 엔드포인트
│   │   ├── situcations.py   # 상황 관련 엔드포인트
│   │   ├── characters.py    # 캐릭터 관련 엔드포인트
│   │   └── chats.py         # 채팅 관련 엔드포인트
│   └── ai/                  # GPT
├── requirements.txt         # 프로젝트 의존성 목록
├── start.sh                 # 실행용 쉘 파일
└── README.md                # 프로젝트 설명서
```
