import requests

def get_sitename()->list[str]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print('e')
    else:
        sitenames = set()
        for items in data['records']:
            sitenames.add(items['sitename'])

        sitenames = list(sitenames)
        return sitenames

def get_selected_data(sitename)->list[list]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print('e')
    else:
        outer_list = []
        
        for i in data['records']:
            inner_list = []
            if i['sitename'] == sitename:
                inner_list.append(i['datacreationdate'])
                inner_list.append(i['county'])
                inner_list.append(i['aqi'])
                inner_list.append(i['pm2.5'])
                inner_list.append(i['status'])
                inner_list.append(i['latitude'])
                inner_list.append(i['longitude'])
                outer_list.append(inner_list)

        
        return outer_list