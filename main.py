from data.data import import_data_to_database, get_total_deaths, get_total_female_deaths, \
    get_total_deaths_by_year, get_total_male_deaths, get_total_deaths_by_age_group

import_data_to_database()

print('Deaths data of New Zealand from 2010-2021')
print('Select the data you wish to see: ')
print('[a] Total deaths from 2010-2021')
print('[b] Total male deaths from 2010-2021')
print('[c] Total female deaths from 2010-2021')
print('[d] Total deaths by year')
print('[e] Total deaths by age group')
data = input()

match data:
    case 'a':
        deaths = get_total_deaths()
        deaths_sum = 0

        for data in deaths:
            deaths_sum += int(data['Count'])

        print(f'Total deaths from 2010-2021: {deaths_sum}')
    case 'b':
        deaths = get_total_male_deaths()
        deaths_sum = 0

        for data in deaths:
            deaths_sum += int(data['Count'])

        print(f'Total male deaths from 2010-2021: {deaths_sum}')
    case 'c':
        deaths = get_total_female_deaths()
        deaths_sum = 0

        for data in deaths:
            deaths_sum += int(data['Count'])

        print(f'Total female deaths from 2010-2021: {deaths_sum}')
    case 'd':
        input_year = input('Enter year: ')

        deaths = get_total_deaths_by_year(input_year)
        deaths_sum = 0

        for data in deaths:
            deaths_sum += int(data['Count'])

        print(f'Total deaths in {input_year}: {deaths_sum}')
    case 'e':
        input_age_group = input('Enter age group: ')

        deaths = get_total_deaths_by_age_group(input_age_group)
        deaths_sum = 0

        for data in deaths:
            deaths_sum += int(data['Count'])

        print(f'Total deaths in {input_age_group}: {deaths_sum}')
