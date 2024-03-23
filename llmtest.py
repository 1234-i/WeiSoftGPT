import openai
openai.api_base="http://home.pqdly.com:1234/v1"
openai.api_key="none"
reponse=openai.ChatCompletion.create(model='chatglm3',messages=[{"role":"user","content":"有以下99元/月 300分钟 20GB，129元/月 500分钟 30GB，159元/月 500分钟 40GB，199元/月 1000分钟 60GB ，239元/月 1000分钟 80GB，299元/月  1500分钟 100GB，399元/月 2000分钟 150GB，599元/月 3000分钟  300GB移动运营商的套餐。客户每月需要的服务是30分钟的通话时间和50GB的流量。请确定在提供的移动运营商套餐中，哪个是最合适的？请一步一步把你的结论推导过程说出来"}])
print(reponse["choices"][0]["message"]["content"])