from data.data import import_data_to_database, get_total_deaths_yearly, get_total_female_deaths, \
    get_total_deaths_by_year, get_total_male_deaths, get_total_deaths_by_age_group
import matplotlib.pyplot as plot
from ui import ui

import_data_to_database()
ui.run()


# Main functionality
def cli():
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
            deaths = get_total_deaths_yearly()
            deaths_sum = 0
            years = []
            deaths_count = []

            for data in deaths:
                current_year = data['Period']
                current_death_count = data['Count']

                try:
                    if current_year != years[-1]:
                        years.append(current_year)
                        deaths_count.append(deaths_sum)
                        deaths_sum = int(current_death_count)
                    elif current_year == '2021':
                        deaths_sum += int(current_death_count)
                    else:
                        deaths_sum += int(current_death_count)
                except IndexError:
                    years.append(current_year)
                    deaths_sum = int(current_death_count)

            deaths_count.append(deaths_sum)

            print(years)
            print(deaths_count)

            print(len(years))
            print(len(deaths_count))

            plot.plot(years, deaths_count)
            plot.title('Total deaths by year')
            plot.xlabel('Year')
            plot.ylabel('Deaths')
            plot.show()

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
