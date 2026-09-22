# Book and Paper-Box Recycling Platform

A six-person Scrum coursework project (2021–2022) exploring a web interface for recycling books and paper boxes. This repository contains the available Flask prototype, not a completed commercial recycling service.

## Personal contribution and team context
Lanjie Tang (Donna) contributed to interface interactions and registration input validation, and participated in backlog refinement, sprint planning and reviews. Flask backend code and database models are shared team work; this repository does not claim sole authorship. Private team meeting files and skills matrices are excluded.

## Included prototype
- Homepage, registration and login templates.
- Registration validation and hashed-password storage.
- Book-collection booking interface and draft order model.
- JavaScript form feedback and modal interactions.

## Local investigation
```sh
python -m venv .venv
# Activate the environment.
python -m pip install -r requirements.txt
cd app
python app.py
```

Set `DATABASE_URL` and `SECRET_KEY` in the shell first; see `.env.example`. Original MySQL credentials have been removed. Requirements are inferred from imports and are not a tested lockfile.

## Known gaps in the supplied snapshot
The draft order model uses `db.varchar`, which is not a standard Flask-SQLAlchemy attribute and prevents normal startup until corrected. Login has only a GET route; order submission is not implemented. Modal registration expects a JSON response but the backend redirects. The signup form does not propagate the JavaScript validator's return value. These are recorded as historical limitations rather than presented as completed functionality.

## 中文简介
六人 Scrum 团队课业，展示回收预约界面、注册校验和迭代协作。个人贡献与团队成果分别说明，原始团队内部文件和数据库密码不上传。
