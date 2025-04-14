# ChaCha (Character Chat)

## 🪄 서비스 소개
캐릭터 인격 생성을 통한 캐릭터 채팅 서비스
- 프롬포트 엔지니어링을 통하여 사용자가 원하는 캐릭터의 이름, 소개, 상황, 성격 등을 설정하고, 해당 캐릭터와 자유롭게 대화를 나눌 수 있는 서비스입니다.

## 👫 개발 기간 및 팀 구성
- 기간: 2023.10 ~ 2024.03 (6개월)
- 인원: 3명 (BE 1, FE 1, AI 1)

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

## ⚙️ 기술 스택
- Backend: FastAPI, Python, Uvicorn
- Database: MongoDB
- Infra: AWS EC2, S3, Nginx
- 협업 도구: GitHub, Figma, Slack

## 프로젝트 구조

```
backend
├─ README.md
├─ app
│  ├─ __init__.py
│  ├─ ai                        # GPT
│  │  ├─ Custom.py
│  │  ├─ Custom2.py
│  │  ├─ __init__.py
│  │  └─ badwords.json
│  ├─ controller                # CRUD 로직 구현
│  │  ├─ __init__.py
│  │  ├─ character_controller.py
│  │  ├─ chat_controller.py
│  │  ├─ situation_controller.py
│  │  └─ user_controller.py
│  ├─ main.py
│  ├─ models                    # 데이터베이스 모델 정의
│  │  ├─ __init__.py
│  │  ├─ characters.py
│  │  ├─ chats.py
│  │  ├─ situations.py
│  │  └─ users.py
│  ├─ routers                   # 라우터 정의
│  │  ├─ __init__.py
│  │  ├─ characters.py
│  │  ├─ chats.py
│  │  ├─ situations.py
│  │  └─ users.py
│  └─ schema                   # 스키마 정의
│     ├─ __init__.py
│     ├─ character_schema.py
│     ├─ chat_schema.py
│     ├─ situation_schema.py
│     └─ user_schema.py
├─ requirements.txt
└─ start.sh                   # 실행용 쉘 파일

```
