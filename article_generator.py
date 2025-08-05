import random
import datetime

# 範例標題和內容模板
TITLES = [
    "最新熱門新聞：{}",
    "你知道嗎？{}",
    "快訊！{}",
    "每日頭條：{}",
    "今日焦點：{}"
]

CONTENTS = [
    "根據最新報導，{} 事件引發了廣泛關注，專家表示這將對社會產生深遠影響。",
    "有消息指出，{} 的情況正在迅速變化，相關部門已經採取措施應對。",
    "許多網友熱議 {}，認為這是今年最值得關注的新聞之一。",
    "針對 {} 的發展，不少分析師給出了專業意見，建議持續關注。",
    "{} 事件在社交媒體上掀起熱潮，引發網友廣泛討論。"
]

def generate_article():
    """隨機生成一篇文章"""
    keyword = random.choice(["金融", "科技", "娛樂", "體育", "國際", "房地產", "旅遊"])
    title = random.choice(TITLES).format(keyword)
    content = random.choice(CONTENTS).format(keyword)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    article = {
        "title": title,
        "content": f"{content}\n\n發布時間：{date}",
        "tags": [keyword, "自動發文", "新聞"]
    }
    return article

if __name__ == "__main__":
    # 測試輸出
    test_article = generate_article()
    print("標題：", test_article["title"])
    print("內容：", test_article["content"])