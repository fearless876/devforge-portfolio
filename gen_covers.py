from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.dirname(__file__)

gigs = [
    {
        "filename": "gig-python-automation.png",
        "title": "Python Automation",
        "subtitle": "Scripts, Scraping & Data Processing",
        "tagline": "Fast delivery · Source code included",
        "color1": (108, 92, 231),
        "color2": (0, 212, 170),
        "emoji": "\U0001f40d"
    },
    {
        "filename": "gig-ai-chatbot.png",
        "title": "AI Chatbot & Agent",
        "subtitle": "Custom GPT · RAG · Workflow Automation",
        "tagline": "ChatGPT & Claude API integration",
        "color1": (255, 107, 157),
        "color2": (108, 92, 231),
        "emoji": "\U0001f916"
    },
    {
        "filename": "gig-doc-automation.png",
        "title": "PPT & Doc Automation",
        "subtitle": "PowerPoint · Word · PDF Generation",
        "tagline": "Branded templates · Batch processing",
        "color1": (0, 172, 238),
        "color2": (108, 92, 231),
        "emoji": "\U0001f4ca"
    },
]

W, H = 550, 370

for gig in gigs:
    img = Image.new('RGB', (W, H), (10, 10, 18))
    draw = ImageDraw.Draw(img)
    
    # Gradient background (approximate with horizontal stripes)
    for i in range(H):
        r = int(gig["color1"][0] + (gig["color2"][0] - gig["color1"][0]) * i / H)
        g = int(gig["color1"][1] + (gig["color2"][1] - gig["color1"][1]) * i / H)
        b = int(gig["color1"][2] + (gig["color2"][2] - gig["color1"][2]) * i / H)
        draw.line([(0, i), (W, i)], fill=(r, g, b))
    
    # Dark overlay
    overlay = Image.new('RGBA', (W, H), (10, 10, 18, 160))
    img.paste(overlay, (0, 0), overlay)
    
    # Try to use a nice font
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 38)
        font_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
        font_tag = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 13)
    except:
        try:
            font_title = ImageFont.truetype("/Library/Fonts/Arial Bold.ttf", 38)
            font_sub = ImageFont.truetype("/Library/Fonts/Arial.ttf", 18)
            font_tag = ImageFont.truetype("/Library/Fonts/Arial.ttf", 13)
        except:
            font_title = ImageFont.load_default()
            font_sub = font_title
            font_tag = font_title
    
    draw = ImageDraw.Draw(img)
    
    # Emoji
    draw.text((30, 25), gig["emoji"], fill=(255, 255, 255), font=font_title)
    
    # Title
    draw.text((30, 110), gig["title"], fill=(255, 255, 255), font=font_title)
    
    # Subtitle
    draw.text((30, 165), gig["subtitle"], fill=(200, 200, 220), font=font_sub)
    
    # Tagline
    draw.text((30, 210), gig["tagline"], fill=(130, 130, 160), font=font_tag)
    
    # Divider line
    draw.line([(30, 250), (250, 250)], fill=(108, 92, 231), width=2)
    
    # Bottom tags
    bottom_tags = ["Source Code", "Documentation", "30-Day Support"]
    x = 30
    for tag in bottom_tags:
        tw = draw.textlength(tag, font=font_tag) if hasattr(draw, 'textlength') else len(tag) * 8
        draw.rounded_rectangle([x, 280, x + tw + 20, 310], radius=10, fill=(30, 30, 50))
        draw.text((x + 10, 285), tag, fill=(180, 180, 200), font=font_tag)
        x += int(tw) + 32
    
    filepath = os.path.join(OUT, "gumroad-product", gig["filename"])
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    img.save(filepath, "PNG")
    print(f"Created: {filepath}")

print("All 3 Gig covers created!")
