# 🚀 上线操作指南

## 你的线上资产

| 资产 | 链接/位置 | 状态 |
|------|-----------|------|
| 🌐 作品集网站 | https://fearless876.github.io/devforge-portfolio/ | ✅ 已上线 |
| 📦 GitHub 仓库 | https://github.com/fearless876/devforge-portfolio | ✅ 已部署 |
| 📧 联系邮箱 | fungchun837@gmail.com | ✅ |
| 🎯 Fiverr 主页 | https://www.fiverr.com/fungchun | ⬜ 需完善 |
| 🛍️ Gumroad 产品 | 待创建 | ⬜ 下面操作 |

---

## 📝 第一部分：Fiverr 上架（预计 1 小时）

### Step 1: 完善 Fiverr 个人资料
1. 打开 https://www.fiverr.com/fungchun
2. 上传专业头像（正式但不死板）
3. 写一段个人简介：
```
I'm a full-stack developer specializing in AI automation, Python scripting, and document generation. I help businesses save 10+ hours/week through custom workflows and smart tools.
```
4. 技能标签：Python, AI Automation, Web Scraping, OpenAI, Data Processing
5. 语言：English (Fluent), Chinese (Native)

### Step 2: 创建 3 个 Gig
打开 `fiverr-gigs.md`，里面有完整的文案（标题、描述、FAQ、定价、搜索标签）。

**定价策略（新手价）**：
| Gig | Basic | Standard | Premium |
|-----|-------|----------|---------|
| Python 自动化 | $15 | $50 | $150 |
| AI Chatbot | $25 | $100 | $350 |
| PPT/文档自动化 | $15 | $75 | $250 |

> 💡 前 10 单用低价策略，拿到 5+ 好评后涨价

### Step 3: 上传 Gig 封面图
封面图已生成，在 `gumroad-product/` 目录下：
- `gig-python-automation.png` → Gig 1 封面
- `gig-ai-chatbot.png` → Gig 2 封面
- `gig-doc-automation.png` → Gig 3 封面

### Step 4: 每个 Gig 加上作品集链接
在每个 Gig 描述末尾加上：
```
📂 Portfolio: https://fearless876.github.io/devforge-portfolio/
```

---

## 🛍️ 第二部分：Gumroad 上架（预计 30 分钟）

### Step 1: 注册 Gumroad
1. 打开 https://gumroad.com
2. 用 fungchun837@gmail.com 注册
3. 设置 payout（PayPal 即可）

### Step 2: 创建产品
1. 点 "Products" → "New product"
2. 填入以下信息：

**Product name:**
```
200+ AI Prompts for Work, Business & Creativity — ChatGPT & Claude Ready
```

**Price:** $9.99（首周可设 $4.99）

**Description:** 打开 `gumroad-product.md` 复制完整文案

**Cover image:** 上传 `gumroad-product/gumroad-cover.png`

### Step 3: 上传产品文件
上传以下文件到 Gumroad：
1. `gumroad-product/ai-prompts-collection.pdf`（主产品）
2. `gumroad-product/prompts-plain.txt`（纯文本版）
3. `gumroad-product/prompts-content.md`（Markdown 版）

### Step 4: 发布
1. 点 "Publish"
2. 获得产品链接，如：`https://fungchun.gumroad.com/l/ai-prompts`
3. 把链接更新到作品集网站（下面操作）

---

## 🔗 第三部分：串联所有渠道

### 更新作品集网站链接
等 Gumroad 产品链接生成后，修改 `index.html` 中的 Gumroad 链接：
```html
<!-- 找到这一行，把 href 改成你的实际链接 -->
<a href="https://fungchun.gumroad.com/l/ai-prompts" ...>Get It on Gumroad →</a>
```

然后提交更新：
```bash
cd ~/Desktop/portfolio-site
git add -A && git commit -m "Update Gumroad link" && git push
```

### 你的获客漏斗
```
Twitter/X / Reddit / LinkedIn
         ↓
   作品集网站（信任建立）
      ↙        ↘
  Fiverr 接单    Gumroad 卖产品
```

---

## 📢 第四部分：推广计划

### 第 1 周：冷启动
- [ ] Twitter/X 每天发 1 条 AI 技巧 + 作品集链接
- [ ] Reddit 发帖到 r/forhire、r/ChatGPT、r/PromptEngineering
- [ ] 用 Fiverr "Buyer Requests" 主动找单
- [ ] 产品首发价 $4.99，快速冲评价

### 第 2 周：放大
- [ ] 收到评价后截图发社交媒体
- [ ] 在 Fiverr 把 Basic 价格提到 $25
- [ ] 给之前买家发消息 offer 定制服务
- [ ] 产品恢复 $9.99 正常价

### 第 3-4 周：稳定运营
- [ ] 每天 30 分钟回复 Fiverr 消息（保持 24h 响应率）
- [ ] 每周发 2-3 条 AI 相关内容
- [ ] 积累 10+ Fiverr 评价 → 开通更多 Gig

---

## 💰 收入预估

| 渠道 | 保守（月） | 中等（月） | 乐观（月） |
|------|-----------|-----------|-----------|
| Fiverr Python 单 | $150 | $500 | $1,500 |
| Fiverr AI 单 | $100 | $300 | $1,000 |
| Fiverr 文档单 | $75 | $250 | $750 |
| Gumroad 产品 | $50 | $200 | $500 |
| **小计** | **$375** | **$1,250** | **$3,750** |

---

## ⚡ 今天就能做的事（30 分钟）

1. ⬜ 打开 Fiverr，完善个人资料
2. ⬜ 创建第一个 Gig（Python 自动化）—— 文案在 `fiverr-gigs.md`
3. ⬜ 上传封面图 `gig-python-automation.png`
4. ⬜ 注册 Gumroad 账号
5. ⬜ 上传 200+ AI Prompts 产品

---

有问题随时问我！需要我帮你更新网站链接、优化描述、做更多封面图，直接说。
