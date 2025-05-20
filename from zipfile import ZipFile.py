from zipfile import ZipFile

# Create sample content for the zip file
assets_folder = "/mnt/data/UMP_Content_Files"
os.makedirs(assets_folder, exist_ok=True)

# Sample content for the project
files_content = {
    "Intro_Script_Hindi.txt": """नमस्कार और स्वागत है आपका 'Stock Market with UMP' में —
जहाँ हम समझते हैं शेयर बाजार की हर छोटी-बड़ी बात को सरल और भरोसेमंद तरीके से।
इस चैनल पर आपको मिलेंगी Beginners से लेकर Advanced तक की पूरी जानकारी — बिल्कुल हिंदी में।
तो जुड़िए हमारे साथ और कीजिए अपने वित्तीय भविष्य को मजबूत।

शुरुआत करते हैं...""",

    "Channel_About_Section.txt": """Stock Market with UMP — एक हिंदी यूट्यूब चैनल जो शेयर बाजार की जटिलताओं को आसान भाषा में समझाता है।
हमारा लक्ष्य है हर विद्यार्थी और निवेशक को सही दिशा देना।
यहाँ आपको मिलेगा:
✅ शेयर बाजार की बुनियादी से लेकर एडवांस जानकारी
✅ ट्रेडिंग स्ट्रैटेजीज़
✅ नियमित अपडेट और शॉर्ट्स

'शेयर बाजार की दुनिया को आसान बनाएं — हमारे साथ'""",

    "Weekly_Posting_Calendar.txt": """🗓️ Weekly Content Calendar (Stock Market with UMP)

Monday – Educational Shorts (60 sec)
Tuesday – Beginner Guide (4-5 mins)
Wednesday – Reels (Trending Tips)
Thursday – Live Stock Market QnA (if possible)
Friday – Technical Concept (Chart, Indicators)
Saturday – Inspirational Investor Story
Sunday – Weekly Recap or Market Outlook
""",

    "5_Reels_Scripts.txt": """🎬 5 Reels Scripts:

1. Topic: Demat Account क्या होता है?
Script: "Demat का मतलब है — shares को digital रूप में रखना। बिल्कुल बैंक अकाउंट की तरह। बिना Demat, आप trading नहीं कर सकते।"

2. Topic: Intraday vs Delivery Trading
Script: "Intraday — उसी दिन खरीदो और बेचो। Delivery — आज खरीदो, बाद में बेचो। Risk और Reward दोनों अलग-अलग!"

3. Topic: Sensex क्या है?
Script: "Sensex = Top 30 companies का index। अगर ये बढ़ रहा है, मतलब बाजार में तेजी है!"

4. Topic: सबसे बड़ी गलती नए निवेशकों की
Script: "जल्दी पैसा कमाने की कोशिश! सीखिए पहले — समझदारी से निवेश कीजिए।"

5. Topic: Stop Loss क्यों जरूरी है?
Script: "Stop loss आपका सुरक्षा कवच है। ये नुकसान को लिमिट करता है और आपको discipline में रखता है।"
""",

    "Content_Ideas_List.txt": """📌 Content Ideas:

- Candlestick Basics (Explained in Hindi)
- Top 5 Mistakes by Beginner Traders
- Difference between Stock & Mutual Fund
- RSI, MACD Indicators
- Budget Planning for Traders
- IPO kya hota hai?
- Live Market Chart Reading
- Goga Maharaj's Wisdom + Stock Discipline (spiritual connect)"""
}

# Save each text file
for filename, content in files_content.items():
    with open(os.path.join(assets_folder, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Zip the content folder
zip_output = "/mnt/data/Stock_Market_with_UMP_Content_Pack.zip"
with ZipFile(zip_output, 'w') as zipf:
    for file_name in os.listdir(assets_folder):
        full_path = os.path.join(assets_folder, file_name)
        zipf.write(full_path, file_name)

zip_output
