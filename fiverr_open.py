#!/usr/bin/env python3
import asyncio, os, signal
from playwright.async_api import async_playwright

USER_DATA = os.path.expanduser("~/Desktop/fiverr-profile")

async def main():
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            USER_DATA, headless=False,
            viewport={"width": 1280, "height": 900},
        )
        page = await ctx.new_page()
        
        # 先去 Fiverr 首页看看登录状态
        await page.goto("https://www.fiverr.com", wait_until="domcontentloaded")
        await asyncio.sleep(3)
        
        # 看看当前 URL（可能被重定向到登录页）
        url = page.url
        print(f"Current URL: {url}")
        
        if "login" in url.lower():
            print("Need login. Login in the browser window, then script will continue...")
            # Wait until URL changes (user logged in)
            while "login" in page.url.lower():
                await asyncio.sleep(1)
            print("Login detected!")
        
        # Now go to selling
        await page.goto("https://www.fiverr.com/users/fungchun/selling/gigs/new", wait_until="domcontentloaded")
        await asyncio.sleep(3)
        print(f"Gig page: {page.url}")
        
        print()
        print("=" * 60)
        print(" ✅ 浏览器已打开 Gig 创建页面")
        print("=" * 60)
        print()
        print("📋 现在请在浏览器中手动填写 Gig：")
        print()
        print("   1. 标题已准备好（桌面 → fiverr-gigs.md → Gig 1）")
        print("   2. 分类选: Programming & Tech → Support & IT")
        print("   3. 标签填: python, automation, web scraping, data processing, api")
        print("   4. 定价: 三档模式，Basic $15, Standard $50, Premium $150")
        print("   5. 描述/FAQ: 从 fiverr-gigs.md 复制")
        print("   6. 封面图: portfolio-site/gumroad-product/gig-python-automation.png")
        print()
        print("🖐  浏览器会保持打开，填完告诉我！")
        
        # Keep browser open
        await asyncio.Event().wait()

asyncio.run(main())
