#!/usr/bin/env python3
"""
Fiverr Gig 自动化上架 — 用 AppleScript 控制 Chrome
由于 Fiverr 创建 Gig 流程复杂且有多步验证，此脚本改为：
1. 打开每个 Gig 创建页面
2. 在页面上执行 JavaScript 预填表单
3. 人工确认后发布
"""

import subprocess, time, json, os

FIVERR_BASE = "https://www.fiverr.com"
GIGS = [
    {
        "name": "Gig 1: Python Scripting & Automation",
        "create_url": f"{FIVERR_BASE}/users/fungchun/selling/gigs/new",
    },
    {
        "name": "Gig 2: AI Chatbot & GPT Automation",
        "create_url": f"{FIVERR_BASE}/users/fungchun/selling/gigs/new",
    },
    {
        "name": "Gig 3: PPT & Document Automation",
        "create_url": f"{FIVERR_BASE}/users/fungchun/selling/gigs/new",
    },
]

def run_applescript(script):
    """Run AppleScript and return stdout"""
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

def chrome_js(js_code):
    """Execute JavaScript in Chrome's active tab"""
    escaped = js_code.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
    script = f'''
    tell application "Google Chrome"
        execute active tab of front window javascript "{escaped}"
    end tell
    '''
    return run_applescript(script)

def chrome_navigate(url):
    """Navigate Chrome to URL"""
    script = f'''
    tell application "Google Chrome"
        set URL of active tab of front window to "{url}"
    end tell
    '''
    return run_applescript(script)

def chrome_get_url():
    """Get current URL"""
    script = '''
    tell application "Google Chrome"
        get URL of active tab of front window
    end tell
    '''
    return run_applescript(script)

print("=" * 60)
print("  Fiverr Gig 自动化上架工具")
print("=" * 60)
print()
print("📋 工作流程：")
print("  1. 脚本打开 Gig 创建页面")
print("  2. 你在页面上手动填写表单")
print("  3. 填完一个告诉我，继续下一个")
print()

# Step: Open Gig creation page
url, _ = chrome_navigate(GIGS[0]["create_url"])
time.sleep(3)
current_url, _ = chrome_get_url()
print(f"✅ 已打开: {current_url}")
print()
print(f"📝 现在开始填写 {GIGS[0]['name']}")
print("   打开桌面的 fiverr-gigs.md 复制文案")
print("   参考定价: Basic $15 · Standard $50 · Premium $150")
print()
print("   填完发布后告诉我，我开下一个 Gig")
