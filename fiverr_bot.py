#!/usr/bin/env python3
"""
Fiverr Gig 自动上架脚本
用 Playwright 控制浏览器，自动填写并发布 Gig
"""

import asyncio, os, sys, json, time
from pathlib import Path
from playwright.async_api import async_playwright

# 数据目录：保存登录态
USER_DATA = os.path.expanduser("~/Desktop/fiverr-profile")

# Gig 数据
GIGS = [
    {
        "title": "I will automate any task with python scripts, web scraping, and data processing",
        "category_path": ["Programming & Tech", "Support & IT", "Other"],
        "search_tags": ["python", "automation", "web scraping", "data processing", "python script", "api integration", "data extraction"],
        "packages": [
            {"name": "Basic", "desc": "Single script or task", "price": 15, "delivery_days": 3, "revisions": 1,
             "includes": ["Source code delivered", "Basic documentation"]},
            {"name": "Standard", "desc": "Full automation pipeline", "price": 50, "delivery_days": 5, "revisions": 3,
             "includes": ["Complete source code + docs", "Deployment guide", "API integration support"]},
            {"name": "Premium", "desc": "Multi-system integration", "price": 150, "delivery_days": 7, "revisions": "unlimited",
             "includes": ["Multi-system integration", "Cloud deployment", "CI/CD setup", "Priority support"]},
        ],
        "description": """Need to save hours on repetitive work? I build production-ready Python scripts that automate your workflow — from web scraping and data processing to API integrations and file management.

💻 WHAT I CAN AUTOMATE:
• Web scraping & data extraction (e-commerce, social media, directories)
• Excel / CSV / JSON data cleaning and transformation
• API integrations (REST, GraphQL, webhooks)
• Telegram / Discord / Slack notification bots
• File batch processing (rename, convert, organize thousands of files)
• PDF generation and report automation
• Database operations (PostgreSQL, MySQL, MongoDB)

✅ EVERY ORDER INCLUDES:
• Clean, commented Python source code
• Step-by-step setup documentation
• 30-day bug-fix support
• Fast delivery (1-3 days typical)

🎯 I work with: Python, Selenium, BeautifulSoup, Scrapy, Pandas, OpenPyXL, Requests, FastAPI, and more.

📩 Message me before ordering so I can understand your exact needs!""",
    },
]

async def main():
    print("🚀 启动 Fiverr Gig 自动上架...")
    print()
    
    async with async_playwright() as p:
        # 使用持久化上下文保存登录态
        ctx = await p.chromium.launch_persistent_context(
            USER_DATA,
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
            viewport={"width": 1280, "height": 900},
        )
        
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        
        # 打开 Fiverr 首页
        await page.goto("https://www.fiverr.com", wait_until="domcontentloaded")
        await asyncio.sleep(2)
        
        # 检查是否已登录
        try:
            await page.wait_for_selector('a[href*="/selling"]', timeout=5000)
            print("✅ 检测到已登录 Fiverr")
        except:
            print("⚠️  请先在浏览器中登录 Fiverr...")
            print("   登录完成后按 Enter 继续...")
            input()
        
        # 切换到 Selling 模式
        await page.goto("https://www.fiverr.com/users/fungchun/selling/gigs/new", wait_until="domcontentloaded")
        await asyncio.sleep(3)
        
        current_url = page.url
        print(f"📍 当前页面: {current_url}")
        
        if "/selling/gigs/new" in current_url:
            print("✅ 已进入 Gig 创建页面")
        elif "/login" in current_url or "/signin" in current_url:
            print("⚠️  需要登录，请在浏览器中登录后按 Enter...")
            input()
            await page.goto("https://www.fiverr.com/users/fungchun/selling/gigs/new")
            await asyncio.sleep(3)
        
        print()
        print("=" * 50)
        print("📝 开始创建 Gig 1: Python Automation")
        print("=" * 50)
        
        # 截图看看当前页面
        await page.screenshot(path=os.path.expanduser("~/Desktop/fiverr-step1.png"))
        print("📸 截图保存到: ~/Desktop/fiverr-step1.png")
        
        # 填写标题
        try:
            title_input = page.locator('input[placeholder*="title"], input[name*="title"], #gig-title, [data-testid="gig-title"]').first
            await title_input.wait_for(state="visible", timeout=5000)
            await title_input.fill(GIGS[0]["title"])
            print("✅ 已填写标题")
        except Exception as e:
            print(f"⚠️  填写标题失败: {e}")
            print("   请在浏览器中手动填写...")
        
        await asyncio.sleep(1)
        
        # 填写搜索标签
        try:
            tag_input = page.locator('input[placeholder*="tag"], [data-testid*="tag"], input[placeholder*="search tag"]').first
            if await tag_input.count() > 0:
                for tag in GIGS[0]["search_tags"][:5]:
                    await tag_input.fill(tag)
                    await tag_input.press("Enter")
                    await asyncio.sleep(0.3)
                print("✅ 已填写搜索标签")
        except Exception as e:
            print(f"⚠️  填写标签失败，请手动填写: {e}")
        
        print()
        print("🖐  浏览器的 Gig 创建页面已打开")
        print("   我已经帮你填了标题和标签")
        print("   剩下的步骤（分类、定价、描述、FAQ、图片）请手动完成")
        print()
        print("   📋 提示：打开桌面的 fiverr-gigs.md 复制文案")
        print("   💰 定价: Basic $15 · Standard $50 · Premium $150")
        print("   🖼️  封面图在: portfolio-site/gumroad-product/")
        print()
        print("   完成后告诉我，我继续下一个 Gig")
        
        # 等待用户
        input("按 Enter 确认完成第一个 Gig...")
        
        print()
        print("🎉 Gig 1 处理完成！")
        print("如需继续创建 Gig 2 和 Gig 3，请再次运行脚本")
        
        await ctx.close()

if __name__ == "__main__":
    asyncio.run(main())
