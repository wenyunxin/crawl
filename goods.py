
cookie = '_s_tentry=baike.baidu.com; Apache=65950291079.23978.1506864073043; SINAGLOBAL=65950291079.23978.1506864073043; login_sid_t=602519341472d0806e7b53928b64910d; cross_origin_proto=SSL; YF-V5-G0=f59276155f879836eb028d7dcd01d03c; _ga=GA1.2.641690142.1533883667; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; TC-V5-G0=866fef700b11606a930f0b3297300d95; TC-Page-G0=6fdca7ba258605061f331acb73120318; YF-Ugrow-G0=ea90f703b7694b74b62d38420b5273df; ULV=1538100673163:1:1:1:65950291079.23978.1506864073043:; SSOLoginState=1542014218; lang=zh-tw; Hm_lvt_50f34491c9065a59f87d0d334df29fa4=1542103540; Hm_lpvt_50f34491c9065a59f87d0d334df29fa4=1542103540; YF-Page-G0=d0adfff33b42523753dc3806dc660aa7; UOR=,,tingshen.court.gov.cn; wvr=6; wb_cmtLike_6079839057=1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whwacu2TuLnnymYo8OU_TVl5JpX5KMhUgL.Foq7S0.Re0.7SKM2dJLoI05LxK-L12BL1K2LxK.L1hBL1K.LxKML1-2L1hBLxKqL1hnL1K829PS7IgSyqJpLKg-t; ALF=1574927049; SCF=AgjEuGgjW4TmTvKonCnJOpMvrlQRLgKsrdJDwptKWmFmVYrYw4wWGhqKwq3TSSr5xylbFRpfQ4H8JMq4fkrfZNs.; SUB=_2A252-jcaDeRhGeBO7FsZ8yfMzjuIHXVVji_SrDV8PUNbmtBeLWvTkW9NRakATTn75gDVdHtZNJkLR24mAKCblC2k; SUHB=0JvgL_JpocfrDg; wb_view_log_6079839057=1440*9002'

cookie_list = []
for c in cookie.split('; '):
    key, value = c.split('=', 1)
    cookie_list.append({'name': key, 'value': value})
    print(cookie_list)
