# -*- coding: utf-8 -*-
import telegram # pip install python-telegram-bot==13.14
from datetime import datetime

# def PrepareMessage(SKU, CATEGORY, PRODUCT, LIST_PRICE, ALERT_PRICE, PRICE, URL, IMAGE):
#     try:
#         DISCOUNT = str(ToLocalizedFormat(Decimal("%.2f" % ((LIST_PRICE-PRICE)*100/LIST_PRICE))))
#         PRICE = str(ToLocalizedFormat(Decimal("%.2f" % PRICE)))
#         ALERT_PRICE = str(ToLocalizedFormat(Decimal("%.2f" % ALERT_PRICE)))
#         LIST_PRICE = str(ToLocalizedFormat(Decimal("%.2f" % LIST_PRICE)))
#         msg = """<a href='""" + IMAGE + """'>\U0001F303</a> (""" + PRICE + """₺) <b><a href='""" + URL + """'>""" + PRODUCT + """</a></b>\n\n"""
#         msg += '\U0001F4CB'""" Liste Fiyatı: """ + LIST_PRICE + """ ₺\n"""
#         msg += '\U0001F3AF'""" Hedef Fiyat: """ + ALERT_PRICE + """ ₺\n"""
#         msg += '\U0001F4B0'""" Güncel Fiyat: <b><u>""" + PRICE + """</u> ₺</b>\n"""
#         msg += '\U0001F4C9'""" İndirim Oranı: %""" + DISCOUNT + """\n"""
#         try:
#             details = HELPERS.GetAkakceLowestPrice(PRODUCT)
#             fiyat = details[1] if(".." in details[1]) else details[1] + " ₺"
#             url = details[0] 
#         except:
#             fiyat = "Pasif"
#             params = {'q': PRODUCT}
#             url = "https://www.akakce.com/arama/?" + urllib.parse.urlencode(params)

#         msg += '\U0001F576'""" <a href='""" + url + """'><b>Akakce.com:</b></a> <i>""" + fiyat + """</i>\n"""            
#         msg += '\U0001F50E'""" <a href='https://www.google.com/search?q=""" + PRODUCT.replace('\'', '+').replace('"','+').replace(' ','+') + """'><b>Google</b></a>  /  <a href='https://www.amazon.com.tr/s?k=""" + SKU + """'><b>Amazon</b></a>\n\n"""
#         msg += """ <b>Kategori: </b>#""" + CATEGORY[:20] + """ (%""" + str(discount) + """)\n"""
#         msg += """ <b>Ürün: </b>#""" + SKU + """\n"""
#         TELEGRAM.send_message(msg)
#     except:
#         print("Mesaj gönderilirken hata oluştu...")

channel_id = -1002113620836
BOT_TOKEN = "7144099326:AAHa2zHgkaFmwLORg5aqs4K31uNawTYt-Sg"
bot = telegram.Bot(token = BOT_TOKEN)
msg = '\U000023F0 <b>' + str(datetime.now().strftime("%H:%M:%S")) + "</b>\n"
msg += '\U0001F482 <i>'" Uğur TURHAL</i>"
msg += "\n<a href='https://www.amazon.com.tr/Samsung-HW-Q800C-TK-Soundbar/dp/B0C4PYPRLL?ref_=Oct_DLandingS_D_a6babb00_0&th=1'> ÜRÜNE GİTMEK İÇİN TIKLA </a>" 
try:
    
    buttons = {
          "inline_keyboard": 
              [
                  [
                    {
                      "text": "\U0001F6D2 " + "Deneme",
                      "url": "https://www.amazon.com.tr/Samsung-HW-Q800C-TK-Soundbar/dp/B0C4PYPRLL?ref_=Oct_DLandingS_D_a6babb00_0&th=1"
                    }
                  ],
                  [
                    {
                      "text": "\U0001F6D2 " + "Deneme",
                      "url": "https://www.amazon.com.tr/Samsung-HW-Q800C-TK-Soundbar/dp/B0C4PYPRLL?ref_=Oct_DLandingS_D_a6babb00_0&th=1"
                    },
                    {
                      "text": "\U0001F6D2 " + "Deneme",
                      "url": "https://www.amazon.com.tr/Samsung-HW-Q800C-TK-Soundbar/dp/B0C4PYPRLL?ref_=Oct_DLandingS_D_a6babb00_0&th=1"
                    }
                  ]
              ]
              
        }
    
    bot.sendPhoto(chat_id=channel_id, caption=msg, 
                  parse_mode = telegram.ParseMode.HTML,
                  reply_markup=buttons,
                  photo="https://m.media-amazon.com/images/I/51pVcxmJgkL._AC_SX679_.jpg")
    
    
    
    # bot.sendMessage(chat_id = channel_id, text = msg, 
    #                 parse_mode = telegram.ParseMode.HTML, 
    #                 disable_web_page_preview = False)
    
except Exception as e:
    print("Bildirim mesajı hatası: " + str(e))