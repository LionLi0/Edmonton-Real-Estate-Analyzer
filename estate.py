def readfile():
    property = []
    with open('properties.txt') as properties:
        for line in properties.readlines():
            each_property = line.strip().split('/n')
            property.append(each_property[0].split(','))
    return property

price = {
    'Strathcona' : 380,
    'Southgate' : 368.55,
    'Clareview' : 368,
    'Century Park' : 340,
    'Mill Woods' : 332.42,
    'Bonnie Doon' : 342.88,
    'Downtown' : 408.44,
    'McKernan' : 410
}

ownership = {
    '1' : ['Nest Properties',1999],
    '2' : ['Mountberry Inc.',1914],
    '3' : ['Robert and Co.',1989],
    '4' : ['Shang Group',2010],
    '5' : ['Singh Association',2005]
}

def Average_Area(property):
    count_Strathcona = 0
    totalarea_Strathcona = 0
    count_Southgate = 0
    totalarea_Southgate = 0
    count_Clareview = 0
    totalarea_Clareview = 0
    count_CenturyPark =0
    totalarea_CenturyPark = 0
    count_MillWoods = 0
    totalarea_MillWoods = 0
    count_BonnieDoon = 0
    totalarea_BonnieDoon = 0
    count_Downtown = 0
    totalarea_Downtown = 0
    count_McKernan = 0
    totalarea_McKernan = 0
    for index in range(len(property)):
        if property[index][0] == 'Strathcona':
            totalarea_Strathcona += float(property[index][2])
            count_Strathcona += 1 
        
        if property[index][0] == 'Southgate':
            totalarea_Southgate += float(property[index][2])
            count_Southgate += 1
        
        if property[index][0] == 'Clareview':
            totalarea_Clareview += float(property[index][2])
            count_Clareview += 1
        
        if property[index][0] == 'Century Park':
            totalarea_CenturyPark += float(property[index][2])
            count_CenturyPark += 1
        
        if property[index][0] == 'Mill Woods':
            totalarea_MillWoods += float(property[index][2])
            count_MillWoods += 1
        
        if property[index][0] == 'Bonnie Doon':
            totalarea_BonnieDoon += float(property[index][2])
            count_BonnieDoon += 1
        
        if property[index][0] == 'Downtown':
            totalarea_Downtown += float(property[index][2])
            count_Downtown += 1
        
        if property[index][0] == 'McKernan':
            totalarea_McKernan += float(property[index][2])
            count_McKernan += 1
    
    stats = {
        "Strathcona": {"count": count_Strathcona, "area": totalarea_Strathcona, "Avg_area":totalarea_Strathcona/count_Strathcona},
        "Southgate" :{"count": count_Southgate, "area": totalarea_Southgate, "Avg_area":totalarea_Southgate/count_Southgate},
        "Clareview" :{"count": count_Clareview, "area": totalarea_Clareview, "Avg_area":totalarea_Clareview/count_Clareview},
        "Century Park" :{"count": count_CenturyPark, "area": totalarea_CenturyPark, "Avg_area":totalarea_CenturyPark/count_CenturyPark},
        "Mill Woods" : {"count": count_MillWoods, "area": totalarea_MillWoods, "Avg_area": totalarea_MillWoods/count_MillWoods},
        "Bonnie Doon" : {"count": count_BonnieDoon, "area": totalarea_BonnieDoon, "Avg_area": totalarea_BonnieDoon/count_BonnieDoon},
        "Downtown" : {"count": count_Downtown, "area": totalarea_Downtown, "Avg_area": totalarea_Downtown/count_Downtown},
        "McKernan": {"count": count_McKernan, "area": totalarea_McKernan, "Avg_area": totalarea_McKernan/count_McKernan},
        }
    
    # check count stats['name']['count']
    # check total stats['name']['area']
    # check average area stats['name']['Avg_area']
    return stats

def Average_Price(stats):
    Avg_Strathcona = stats['Strathcona']['area']* price['Strathcona'] /stats['Strathcona']['count']
    Avg_Southgate = stats['Southgate']['area']* price['Southgate'] /stats['Southgate']['count']
    Avg_Clareview = stats['Clareview']['area']* price['Clareview'] /stats['Clareview']['count']
    Avg_CenturyPark = stats['Century Park']['area']* price['Century Park'] /stats['Century Park']['count']
    Avg_MillWoods = stats['Mill Woods']['area']* price['Mill Woods'] /stats['Mill Woods']['count']
    Avg_BonnieDoon = stats['Bonnie Doon']['area']* price['Bonnie Doon'] /stats['Bonnie Doon']['count']
    Avg_Downtown = stats['Downtown']['area']* price['Downtown'] /stats['Downtown']['count']
    Avg_McKernan = stats['McKernan']['area']* price['McKernan'] /stats['McKernan']['count']

    Avg_price = {
        "Strathcona": {"Avg_Price":Avg_Strathcona },
        "Southgate" :{"Avg_Price":Avg_Southgate },
        "Clareview" :{"Avg_Price":Avg_Clareview  },
        "Century Park" :{"Avg_Price":Avg_CenturyPark },
        "Mill Woods" : {"Avg_Price":Avg_MillWoods  },
        "Bonnie Doon" : {"Avg_Price": Avg_BonnieDoon},
        "Downtown" : {"Avg_Price": Avg_Downtown},
        "McKernan": {"Avg_Price": Avg_McKernan}
    }

    # print(Avg_price['McKernan']['Avg_Price']) check the average price formate
    return Avg_price

def Number_of_Available_Properties(property):
    Ava_Strathcona = 0
    Ava_Southgate = 0
    Ava_Clareview = 0
    Ava_CenturyPark =0
    Ava_MillWoods = 0
    Ava_BonnieDoon = 0
    Ava_Downtown = 0
    Ava_McKernan = 0
    for index in range(len(property)):
        if property[index][0] == 'Strathcona':
            if property[index][3] == '0':
                Ava_Strathcona += 1
        
        if property[index][0] == 'Southgate':
            if property[index][3] == '0':
                Ava_Southgate += 1
        
        if property[index][0] == 'Clareview':
            if property[index][3] == '0':
                Ava_Clareview += 1
        
        if property[index][0] == 'Century Park':
            if property[index][3] == '0':
                Ava_CenturyPark += 1
        
        if property[index][0] == 'Mill Woods':
            if property[index][3] == '0':
                Ava_MillWoods += 1
        
        if property[index][0] == 'Bonnie Doon':
            if property[index][3] == '0':
                Ava_BonnieDoon += 1
        
        if property[index][0] == 'Downtown':
            if property[index][3] == '0':
                Ava_Downtown += 1
        
        if property[index][0] == 'McKernan':
            if property[index][3] == '0':
                Ava_McKernan += 1

    number_of_available_properties  = {
        "Strathcona": {"number": Ava_Strathcona},
        "Southgate" :{"number": Ava_Southgate},
        "Clareview" :{"number": Ava_Clareview},
        "Century Park" :{"number": Ava_CenturyPark},
        "Mill Woods" : {"number":  Ava_MillWoods},
        "Bonnie Doon" : {"number": Ava_BonnieDoon},
        "Downtown" : {"number": Ava_Downtown},
        "McKernan": {"number": Ava_McKernan},
        }
    # check the number of available properties :print(number_of_available_properties['CenturyPark']['number'])
    return number_of_available_properties

  

def main():
    property = readfile()
    stats = Average_Area(property)
    Avg_price = Average_Price(stats)
    number_of_available_properties = Number_of_Available_Properties(property)
    sorted_data = sorted(number_of_available_properties.items(),key=lambda x:x[1]['number'],reverse=True)
    print(f'+{'-' * 15}+{'-'*15}+{'-'*14}+{'-'*11}+')
    print(f'| Location      | Average Area  | Average Price| Available |')
    print(f'+{'-' * 15}+{'-'*15}+{'-'*14}+{'-'*11}+')
    print(f'| {sorted_data[0][0]:<14}| {stats[sorted_data[0][0]]['Avg_area']:,.2f} sqft | $  {Avg_price[sorted_data[0][0]]['Avg_Price']:,.2f}|{number_of_available_properties[sorted_data[0][0]]['number']:>10} |')
    print(f'| {sorted_data[1][0]:<14}| {stats[sorted_data[1][0]]['Avg_area']:,.2f} sqft | $  {Avg_price[sorted_data[1][0]]['Avg_Price']:,.2f}|{number_of_available_properties[sorted_data[1][0]]['number']:>10} |')
    print(f'| {sorted_data[2][0]:<14}| {stats[sorted_data[2][0]]['Avg_area']:,.2f} sqft | $  {Avg_price[sorted_data[2][0]]['Avg_Price']:,.2f}|{number_of_available_properties[sorted_data[2][0]]['number']:>10} |')
    print(f'| {sorted_data[3][0]:<14}| {stats[sorted_data[3][0]]['Avg_area']:,.2f} sqft | $  {Avg_price[sorted_data[3][0]]['Avg_Price']:,.2f}|{number_of_available_properties[sorted_data[3][0]]['number']:>10} |')
    print(f'| {sorted_data[4][0]:<14}| {stats[sorted_data[4][0]]['Avg_area']:,.2f} sqft | $  {Avg_price[sorted_data[4][0]]['Avg_Price']:,.2f}|{number_of_available_properties[sorted_data[4][0]]['number']:>10} |')
    print(f'| {sorted_data[5][0]:<14}| {stats[sorted_data[5][0]]['Avg_area']:,.2f} sqft | $  {Avg_price[sorted_data[5][0]]['Avg_Price']:,.2f}|{number_of_available_properties[sorted_data[5][0]]['number']:>10} |')
    print(f'| {sorted_data[6][0]:<14}| {stats[sorted_data[6][0]]['Avg_area']:,.2f} sqft | $  {Avg_price[sorted_data[6][0]]['Avg_Price']:,.2f}|{number_of_available_properties[sorted_data[6][0]]['number']:>10} |')
    print(f'| {sorted_data[7][0]:<14}| {stats[sorted_data[7][0]]['Avg_area']:,.2f} sqft | $  {Avg_price[sorted_data[7][0]]['Avg_Price']:,.2f}|{number_of_available_properties[sorted_data[7][0]]['number']:>10} |')
    print(f'+{'-' * 15}+{'-'*15}+{'-'*14}+{'-'*11}+')
main()