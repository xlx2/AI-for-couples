# AI-for-couples


### Alembic控制数据库
```
uv run alembic init -t async alembic # 初始化
uv run alembic revision --autogenerate -m "Initial migration" #
uv run alembic upgrade head # 完成迁移
uv run alembic downgrade -1 # 回退到上一个版本 e.g. -2 -3 或版本号
```