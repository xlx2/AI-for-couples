# AI-for-Couples 🍽️💕

### 目的
为了解决情侣沟通中的会出现的各种小问题，如不知道吃什么、一起学习监督等问题。

---
### 需求

#### 不知道吃什么
🎯 核心痛点
- **选择困难**："随便"="不知道吃什么"
- **沟通障碍**：猜不透对方想吃什么
- **时间浪费**：反复讨论30分钟还没决定
- **体验单调**：缺少互动和趣味性

先让两人分别用 3 个 emoji 形容今晚的胃口（🌶️🍜🥩），系统用 emoji 向量相似度做匹配，再转一次“加权转盘”——默契度越高，共同想吃的菜系在转盘上面积越大。把“吃什么”拆成两步：先默契测试，再随机惊喜，既解决选择困难，又增加互动。

---


#### 我们的解决方案
> **AI驱动的"默契测试+惊喜转盘"双步模式**

---
### 🚀 核心功能

#### 🤝 Emoji默契测试
让两人分别用3个emoji形容今晚的胃口（🌶️🍜🥩），系统通过emoji向量相似度计算默契值。

#### 🎡 加权惊喜转盘
默契度越高，共同偏好的菜系在转盘上面积越大，既解决选择困难，又增加互动乐趣。

#### 📊 智能推荐系统
基于地理位置、用餐时间、预算范围，精准推荐两人都喜欢的餐厅。

---
### 🔄 核心流程图

```
graph TD
    A[启动App] --> B{是否首次使用?}
    B -->|是| C[甜蜜引导页 💕]
    B -->|否| D[主页: 开始默契测试]
    
    C --> D
    
    D --> E[Partner A: 选择3个emoji]
    E --> F[邀请另一半 💌]
    F --> G[Partner B: 选择3个emoji]
    G --> H[AI计算默契度]
    H --> I[生成专属转盘]
    I --> J[🎡 转盘大冒险]
    J --> K[显示推荐结果]
    K --> L[导航到餐厅]
```


### 📋 功能需求清单
#### 1️⃣ 用户系统 👥
| 功能模块     | 详细描述             | 优先级   | 开发周期 |
| -------- | ---------------- | ----- | ---- |
| **快速注册** | 手机号/微信/QQ一键登录    | 🔴 P0 | 2天   |
| **情侣绑定** | 二维码/邀请码配对，支持微信分享 | 🔴 P0 | 2天   |
| **个人档案** | 头像、昵称、饮食偏好标签     | 🟡 P1 | 1天   |
| **历史记录** | 查看过去的推荐结果和用餐历史   | 🟢 P2 | 1天   |

#### 2️⃣ Emoji默契测试系统 😊
| 功能模块       | 详细描述                | 优先级   | 技术要点           |
| ---------- | ------------------- | ----- | -------------- |
| **Emoji库** | 50+食物相关emoji，智能分类展示 | 🔴 P0 | Unicode向量映射    |
| **选择限制**   | 每人必须选3个emoji，实时计数   | 🔴 P0 | 前端状态管理         |
| **实时同步**   | Partner选择状态实时更新     | 🔴 P0 | WebSocket通信    |
| **相似度算法**  | 基于语义向量的AI匹配算法       | 🔴 P0 | Python Flask服务 |

#### 3️⃣ 加权转盘系统 🎪
| 功能模块     | 详细描述           | 优先级   | 视觉效果      |
| -------- | -------------- | ----- | --------- |
| **动态权重** | 默契度越高，偏好菜系扇区越大 | 🔴 P0 | 3D渐变色彩    |
| **转盘动画** | 流畅3D旋转，可控制速度   | 🟡 P1 | Lottie动画库 |
| **结果展示** | 菜系+餐厅+距离+评分    | 🔴 P0 | 卡片式UI     |
| **重新转盘** | 不满意可无限次重试      | 🟡 P1 | 防误触设计     |

#### 4️⃣ 智能推荐系统 🧠
| 功能模块      | 详细描述         | 优先级   | 数据来源    |
| --------- | ------------ | ----- | ------- |
| **餐厅数据**  | 接入美团/大众点评API | 🔴 P0 | 第三方API  |
| **智能过滤**  | 时间、距离、预算三重筛选 | 🟡 P1 | 用户位置+偏好 |
| **个性化学习** | 记录反馈，持续优化推荐  | 🟢 P2 | 机器学习算法  |


### 🛠️ 技术架构
#### 前端技术栈 📱
```yaml
框架: Vue 3.x (组合式 API)
状态管理: Pinia
路由管理: Vue Router 4.x
UI组件库: Element Plus / Vuetify
动画引擎: CSS3 + GSAP / Framer Motion
实时通信: Socket.io-client
构建工具: Vite 4.x
```

#### 后端技术栈
```yaml
主框架: Python 3.11+ + FastAPI 0.104+
数据库: SQLAlchemy 2.0 (支持异步) + SQLite/PostgreSQL
数据库迁移: Alembic (异步模板)
缓存: Redis (可选，用于会话管理)
实时通信: FastAPI WebSocket
推荐算法: Python 3.11 + NumPy + SciPy
文件存储: AWS S3 / 本地存储
服务器: Uvicorn ASGI服务器
依赖管理: uv / pip
```

### AI算法核心 🧮
#### Emoji语义向量化
```python
# 基于食物属性的多维度向量映射
emoji_food_vectors = {
    "🌶️": [1.0, 0.2, 0.1, 0.8, 0.9],  # 辣度、温度、甜度、刺激度、复杂度
    "🍜": [0.3, 0.9, 0.4, 0.2, 0.6],  # 汤面类
    "🥩": [0.2, 0.7, 0.1, 0.5, 0.8],  # 肉类
    "🍰": [0.1, 0.3, 0.9, 0.1, 0.7],  # 甜点类
    # ... 更多emoji向量 (共50+)
}

def calculate_compatibility(partner_a_emojis, partner_b_emojis):
    """计算情侣间的用餐默契度"""
    vector_a = np.mean([emoji_food_vectors[e] for e in partner_a_emojis], axis=0)
    vector_b = np.mean([emoji_food_vectors[e] for e in partner_b_emojis], axis=0)
    
    # 余弦相似度计算
    similarity = np.dot(vector_a, vector_b) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))
    
    # 映射到0-100的默契度分数
    compatibility_score = int((similarity + 1) * 50)
    return min(100, max(0, compatibility_score))
```

#### 加权转盘算法
```python
def generate_weighted_wheel(compatibility_score, common_preferences):
    """生成基于默契度的加权转盘配置"""
    
    # 基础菜系权重
    base_cuisines = {
        '川菜': 0.2, '粤菜': 0.15, '西餐': 0.15, '日料': 0.12,
        '火锅': 0.1, '烧烤': 0.1, '韩料': 0.08, '东南亚': 0.08
    }
    
    # 根据默契度调整权重
    adjustment_factor = compatibility_score / 100.0
    
    # 共同偏好菜系获得更高权重
    for cuisine in common_preferences:
        if cuisine in base_cuisines:
            base_cuisines[cuisine] *= (1 + adjustment_factor)
    
    # 归一化权重
    total_weight = sum(base_cuisines.values())
    weighted_cuisines = {k: v/total_weight for k, v in base_cuisines.items()}
    
    return create_wheel_sectors(weighted_cuisines)
```

### 🎨 UI/UX设计系统
#### 色彩规范 🌈
```css
/* 主色调 */
--primary-love: #FF6B6B;      /* 温暖红色 - 代表爱情 */
--primary-food: #4ECDC4;      /* 清新青色 - 代表食物 */
--accent-gold: #FFD93D;       /* 活力黄色 - 强调色 */

/* 中性色 */
--text-primary: #2C3E50;      /* 主文本 */
--text-secondary: #7F8C8D;    /* 次要文本 */
--background: #FFFFFF;        /* 纯白背景 */
--surface: #F8F9FA;           /* 卡片背景 */
--border: #E9ECEF;            /* 边框色 */
```

#### 字体系统 📝
```css
/* 字体层级 */
--font-title: 28px/36px PingFang SC, Bold;      /* 大标题 */
--font-heading: 20px/28px PingFang SC, Medium;  /* 小标题 */
--font-body: 16px/24px PingFang SC, Regular;    /* 正文 */
--font-caption: 14px/20px PingFang SC, Light;   /* 说明文字 */
--font-button: 18px/26px PingFang SC, Medium;   /* 按钮文字 */
```

### 交互原则 ⚡
3秒原则：任何操作必须在3秒内给出反馈
一键直达：核心功能不超过2步操作
情感化反馈：成功动画、失败安慰、加载趣味提示


### 💾 数据库设计
#### 用户表 (users)
```json
{
  "_id": "ObjectId",
  "phone": "+86-138-0000-0000",
  "nickname": "小吃货",
  "avatar": "https://s3.amazonaws.com/avatars/123.jpg",
  "partner_id": "ObjectId",
  "bound_at": "ISODate",
  "food_preferences": ["川菜", "日料", "甜品"],
  "location": {
    "type": "Point",
    "coordinates": [116.4074, 39.9042]
  },
  "created_at": "ISODate",
  "last_active": "ISODate"
}
```

#### 默契记录表 (compatibility_records)
```json
{
  "_id": "ObjectId",
  "couple_id": "couple_123_456",
  "partner_a": {
    "user_id": "ObjectId",
    "emojis": ["🌶️", "🍜", "🥩"],
    "submitted_at": "ISODate"
  },
  "partner_b": {
    "user_id": "ObjectId", 
    "emojis": ["🌶️", "🍰", "🍕"],
    "submitted_at": "ISODate"
  },
  "compatibility_score": 85,
  "recommended_cuisines": ["川菜", "火锅"],
  "final_choice": {
    "cuisine": "川菜",
    "restaurant": "蜀大侠火锅",
    "rating": 4.8,
    "distance": 1.2
  },
  "feedback": 5,  // 1-5星评价
  "created_at": "ISODate"
}
```

### 🔌 API接口设计
#### 用户模块 👤
```
POST /api/users/register - 用户注册
POST /api/users/login - 用户登录
POST /api/users/bind-partner - 绑定情侣
GET /api/users/profile - 获取用户信息
```
#### Emoji默契测试 😊
```
POST /api/emoji/submit - 提交emoji选择
GET /api/emoji/waiting-partner - 等待partner选择
GET /api/emoji/result - 获取相似度结果
```
### 智能推荐 🎯
```
POST /api/recommendation/wheel-config - 获取转盘配置
POST /api/recommendation/spin - 执行转盘
GET /api/recommendation/restaurants - 获取餐厅详情
```

### 📅 30天开发路线图
第1周：基础架构 🏗️ (Day 1-7)

Day 1-2  📋 项目初始化
- ✨ 技术栈确认和环境搭建
- 📁 项目结构设计和Git仓库初始化
- 🔧 ESLint/Prettier代码规范配置

Day 3-4  👥 用户系统开发
- 📱 注册/登录UI界面开发
- 🔐 手机号验证和JWT认证
- 💾 用户数据模型设计

Day 5-7  🎨 基础框架搭建
- 🧭 底部导航和路由配置
- 🎨 UI组件库集成和主题配置
- 📱 响应式布局适配


第2周：核心功能 💝 (Day 8-14)

Day 8-10  😊 Emoji选择模块
- 🎯 Emoji分类展示界面
- ✨ 选择交互和状态管理
- 📊 已选emoji展示和删除功能

Day 11-12  🧮 AI算法集成
- 🔢 Emoji向量化算法实现
- 🎯 相似度计算服务部署
- 🧪 算法准确性测试和调优

Day 13-14  ⚡ 实时同步
- 🔄 WebSocket连接管理
- 💌 情侣状态实时更新
- ⏰ 超时处理和重试机制


第3周：转盘体验 🎪 (Day 15-21)

Day 15-17  🎡 转盘UI开发
- 🎨 3D转盘界面设计和实现
- ✨ Lottie动画集成和优化
- 🎯 触摸交互和旋转控制

Day 18-19  ⚖️ 加权算法
- 📊 动态权重计算逻辑
- 🎨 转盘扇区渲染优化
- 🎯 结果随机算法实现

Day 20-21  🏪 餐厅推荐
- 🔌 美团/大众点评API对接
- 📍 地理位置和距离计算
- ⭐ 评分和筛选算法


第4周：优化上线 🚀 (Day 22-30)

Day 22-24  ✨ 体验优化
- 🎯 加载速度优化和缓存策略
- 💫 交互动画和过渡效果
- 🎨 UI细节打磨和适配优化

Day 25-27  🐛 测试修复
- 🔍 功能测试和Bug修复
- 📱 多设备兼容性测试
- ⚡ 性能优化和内存管理

Day 28-30  🚀 发布准备
- 📋 应用商店资料准备
- 🧪 内测用户反馈收集
- 🎯 最终版本打包和发布



🧪 质量保证方案
功能测试清单 ✅

- [✅] 单人选择emoji后正确等待partner响应
- [✅] 相似度计算结果始终在0-100范围内
- [✅] 转盘扇区大小与默契度成正比关系
- [✅] 推荐餐厅信息完整（名称、评分、距离、人均）
- [✅] 网络断开时显示友好错误提示
- [✅] 超时处理机制正常工作
- [✅] 用户反馈能够正确记录和分析

### 🔄 运营维护计划

应用名称：吃什么-情侣版 | AI默契测试
副标题：解决选择困难，发现美食默契
关键词：情侣,吃什么,美食推荐,默契测试,转盘,餐厅
应用描述：
"还在纠结今晚吃什么？用emoji测测你们的用餐默契！
- 😊 选择3个emoji表达心情
- 🎡 AI生成专属加权转盘  
- 🏪 智能推荐双方都爱的餐厅
- 💕 让每一顿饭都充满惊喜和默契"

### 截图设计：
1. 情侣emoji选择界面 - 突出趣味性
2. 转盘旋转动画 - 展示核心玩法  
3. 餐厅推荐结果 - 体现实用价值
4. 用户好评反馈 - 建立信任感

### 用户反馈渠道 💬
📧 邮箱支持：support@ai-for-couples.com
💬 微信客服：AI-for-couples (工作日9-18点)
📱 应用内反馈：设置-意见反馈 (带截图功能)
🎯 用户调研：每月一次问卷调研
🏆 种子用户群：核心用户微信群运营

### 版本迭代计划 🚀

V1.1 (发布后1个月)
- 🎯 新增"纪念日推荐"功能
- 📊 完善用户画像和推荐算法
- 🎨 优化UI细节和动画效果

V1.2 (发布后2个月) 
- 📸 拍照识别食物热量功能
- 💰 集成优惠券和团购信息
- 🏆 新增"默契排行榜"

V1.3 (发布后3个月)
- 🎵 背景音乐和音效
- 📱 桌面小组件支持
- 🔐 隐私保护功能增强

💡 未来扩展方向

短期(3个月)
- 📸 拍照识图：拍食材推荐做法
- 💰 优惠聚合：整合各平台优惠券  
- 🏆 成就系统：用餐里程碑奖励

中期(6个月)
- 🌍 多城市支持：全国热门城市覆盖
- 🎵 音乐推荐：根据用餐心情播音乐
- 📱 智能小组件：桌面快速推荐

长期(12个月)
- 🏪 线下合作：与餐厅深度合作
- 🤖 AI助手：语音交互和智能对话
- 🌍 海外拓展：国际化版本发布

### 商业模式 
#### 免费版功能
- ✅ 基础emoji默契测试
- ✅ 每日3次转盘推荐
- ✅ 基础餐厅推荐

#### 会员版功能 ($9.9/月)
- 🎯 无限次转盘使用
- 📊 高级推荐算法
- 💰 专属优惠券
- 📱 优先客服支持

#### 企业合作
- 🏪 餐厅推广合作
- 📊 用户行为数据分析
- 🎯 精准广告投放

### 📞 联系我们

产品团队：AI-for-Couples Development Team
📧 邮箱：team@ai-for-couples.com
💬 微信：AI-for-Couples
🌐 官网：www.ai-for-couples.com
📱 内测群：扫码加入微信群(备注"情侣App")
"让每一顿饭都充满爱与惊喜" 💕
本文档最后更新：2026年1月13日
版本：v1.0
状态：开发进行中 🚀
