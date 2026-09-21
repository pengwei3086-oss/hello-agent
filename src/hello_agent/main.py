import requests

def get_weather(city_name):
    # 拼接url，wttr.in接口，format=j1返回json
    url = f"https://wttr.in/{city_name}?format=j1"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status() # 请求失败直接抛出异常
        data = resp.json()

        # 解析json里面的字段
        city = data["nearest_area"][0]["areaName"][0]["value"]
        temp = data["current_condition"][0]["temp_C"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]

        result = f"城市：{city}，当前温度：{temp}℃，天气：{desc}"
        return result
    except Exception as e:
        return f"获取天气失败：{e}"

if __name__ == "__main__":
    # 查询北京，你也可以改成Shanghai、Guangzhou
    weather_info = get_weather("Beijing")
    print(weather_info)
