from fake_useragent import UserAgent      # fake_useragent模块 user-agent的获取 


ua = UserAgent()        # 实例化，实例化时需要联网但是网站不太稳定 

print(ua.ie)      # 随机打印一个 ie 浏览器的头 

print(ua.opera)

print(ua.chrome)

print(ua.google)

print(ua.firefox)

print(ua.safari)

print(ua.random)      # 随机打印 User-Agent 

