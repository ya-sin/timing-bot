from PIL import Image, ImageDraw, ImageFont
import re

def containenglish(str0):
    return bool(re.search('[a-z]', str0))
def f(x):
    return {
        'party': "#F2A073",
        'battle': "#ACE2D9",
        'workshop': '#DB8A88',
        'dance camp': '#DA9DD8',
        'lecture': '#B1B5F4',
        'showcase': '#7AA0D7',
        'audition': '#99CBA6',
    }[x]
def makepost(gets,count):
    classification = gets['class']
    date = [gets['month'],gets['date']]
    title = gets['title']#'不羈夜-circle tonight 青創開幕夜'
    time = gets['time']
    location = gets['location']

    if containenglish(title):
        n = 17
    else:
        n = 10
    title_list = [title[i:i + n] for i in range(0, len(title), n)]

    # source img
    img = './img/%s.jpg' % classification
    new_img = 'event(%d).jpg' % count
    compress_img = 'compress.jpg'

    # font
    # font_type = '/System/Library/Fonts/STHeiti Light.ttc'
    font_medium_type = '/System/Library/Fonts/STHeiti Medium.ttc'
    font = ImageFont.truetype(font_medium_type, 28)
    title_font = ImageFont.truetype(font_medium_type, 60)
    mon_font = ImageFont.truetype(font_medium_type, 45)
    date_font = ImageFont.truetype(font_medium_type, 130)
    color_W = "#ffffff"
    color = f(classification.lower())

    # open img
    image = Image.open(img)
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # date
    month_x2 = 50
    month_y2 = 740
    month_x1 = 65
    month_y1 = 740
    if date[0] >= 10 :
        draw.text((month_x2, height - month_y2), u'%d' % date[0], color, mon_font)
    else :
        draw.text((month_x1, height - month_y1), u'%d' % date[0], color, mon_font)
    date_x2 = 90
    date_y2 = 680
    date_x1 = 120
    date_y1 = 680
    if date[1] >= 10 :
        draw.text((date_x2, height - date_y2), u'%d' % date[1], color_W, date_font)
    else :
        draw.text((date_x1, height - date_y1), u'%d' % date[1], color_W, date_font)

    # title
    title_x = 110
    title_y = 450
    summary_line = 70
    for num, title in enumerate(title_list):
        y = title_y - num * summary_line
        draw.text((title_x, height - y), u'%s' % title, color_W, title_font)

    # time
    cur_time_x = 120
    cur_time_y = 180
    draw.text((cur_time_x, height - cur_time_y), u'%s' % time, color_W, font)

    # location
    loc_x = 120
    loc_y = 90
    draw.text((loc_x, height - loc_y), u'%s' % location, color_W, font)

    # save img
    image.save(new_img, 'png')

    # compress img
    sImg = Image.open(new_img)
    w, h = sImg.size
    width = int(w / 2)
    height = int(h / 2)
    dImg = sImg.resize((width, height), Image.ANTIALIAS)
    dImg.save(compress_img)
# def updateURL(doc_ref,count):
