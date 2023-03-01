import sqlite3
import requests
from db import GroupsDB
import time

groupsdb = GroupsDB()
class Parse():
    def __init__(self) -> None:
        self.token="vk1.a.T-ozBbcjySzs6clINRssn3h_9O2bssCapUb_9x_Fn8YIciqbcj5D9bbLKuaEL_2YND99bEXiFHRQ9SLER9YFxOAGq0JbS5EqwyzYkJB59Up93o3tr61U68sPkQD9cfh49Tkv2P5mde9yHoU8QU_axA1fI_3swyB9sSjEK2R2bk_ggMAPolQACY187nYYkOSAqW-Z4qIaT364fY4DHnm7aw"
    
    def cities(self,offset):
        method = 'database.getCities'
        params = f'countryId=0&need_all=0&count=1000&offset={offset}'
        version ='5.131'
        request = "https://api.vk.com/method/{}?{}&access_token={}&v={}".format(method,params,self.token,version)
        result = requests.get(request)
        result = result.json()
        return result


    def search(self,city_id,q):
        method = 'groups.search'
        params = f'city_id={city_id}&q={q}&sort=2&count=1000'
        version ='5.131'
        request = "https://api.vk.com/method/{}?{}&access_token={}&v={}".format(method,params,self.token,version)
        result = requests.get(request)
        result = result.json()
        return result

    def get_info(self,gid):
        method = 'groups.getById'
        params = f'fields=members_count,is_closed,can_post&group_id={gid}'
        version ='5.131'
        request = "https://api.vk.com/method/{}?{}&access_token={}&v={}".format(method,params,self.token,version)
        result = requests.get(request)
        result = result.json()
        url = f'https://vk.com/{result["response"][0]["screen_name"]}'
        name = result["response"][0]["name"]
        subs = result["response"][0]["members_count"]
        if(result["response"][0]["can_post"] == 1):
            if(result["response"][0]["is_closed"] == 0):
                groupsdb.add_group(url=url,title=name,subs=subs)

    def main(self):
        cities = [
            1, 2, 10, 37, 42, 49, 60, 61, 72, 73, 95, 99, 104, 110, 119, 123, 151, 153, 158, 185, 627
            ]
        keywords = [
            "Тайный покупатель",
            "Работа тайным покупателем",
            "Проверка тайный покупатель",
            "работа для мам",
            "подработка для студентов",
            "подработка без вложений",
            "работа онлайн",
            "подработка в сети",
            "работа в сети",
            "подработка дома",
            "подработка не выходя из дома",
            "работа не выходя из дома",
        ]
        for city in cities:
            for keyword in keywords:
                print(city)
                groups = self.search(city_id=city,q=keyword)
                for group in groups["response"]["items"]:
                    try:
                        print(group["id"])
                        gid = group["id"]
                        self.get_info(gid)
                    except Exception as ex:
                        print(ex)
                    time.sleep(0.5)
                time.sleep(5)
            time.sleep(5)


# x = 0
# for city in cities["response"]["items"]:
#     name = city["name"]
#     url = f"https://vk.com/{city['screen_name']}"
#     print(city)
#     x += 1
Parse().main()