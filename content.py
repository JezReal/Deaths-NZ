from data.data import get_total_deaths_yearly, get_total_female_deaths, \
    get_total_deaths_by_year, get_total_male_deaths, get_total_deaths_by_age_group
import numpy
import matplotlib.pyplot as plot


# Main functionality
def cli():
    print('Deaths data of New Zealand from 2010-2021')
    print('Select the data you wish to see: ')
    print('[a] Total deaths from 2010-2021')
    print('[b] Total male deaths from 2010-2021')
    print('[c] Total female deaths from 2010-2021')
    print('[d] Total deaths by year')
    print('[e] Total deaths by age group')
    print('[f] Total male and female deaths by year')
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

            plot.plot(years, deaths_count)
            plot.title('Total deaths by year')
            plot.xlabel('Year')
            plot.ylabel('Deaths')
            plot.show()

        case 'b':
            deaths = get_total_male_deaths()
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

            plot.plot(years, deaths_count)
            plot.title('Total male deaths by year')
            plot.xlabel('Year')
            plot.ylabel('Deaths')
            plot.show()

        case 'c':
            deaths = get_total_female_deaths()
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

            plot.plot(years, deaths_count)
            plot.title('Total FEmale deaths by year')
            plot.xlabel('Year')
            plot.ylabel('Deaths')
            plot.show()

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

        case 'f':
            years = []
            total_male_deaths = []
            total_female_deaths = []

            male_deaths_sum = 0
            female_deaths_sum = 0
            male_deaths = get_total_male_deaths()
            female_deaths = get_total_female_deaths()

            for death in male_deaths:
                current_year = death['Period']
                current_death_count = death['Count']

                try:
                    if current_year != years[-1]:
                        years.append(current_year)
                        total_male_deaths.append(male_deaths_sum)
                        male_deaths_sum = int(current_death_count)
                    elif current_year == '2021':
                        male_deaths_sum += int(current_death_count)
                    else:
                        male_deaths_sum += int(current_death_count)
                except IndexError:
                    years.append(current_year)
                    male_deaths_sum = int(current_death_count)

            total_male_deaths.append(male_deaths_sum)

            years = []
            for death in female_deaths:
                current_year = death['Period']
                current_death_count = death['Count']

                try:
                    if current_year != years[-1]:
                        years.append(current_year)
                        total_female_deaths.append(female_deaths_sum)
                        female_deaths_sum = int(current_death_count)
                    elif current_year == '2021':
                        female_deaths_sum += int(current_death_count)
                    else:
                        female_deaths_sum += int(current_death_count)
                except IndexError:
                    years.append(current_year)
                    female_deaths_sum = int(current_death_count)

            total_female_deaths.append(female_deaths_sum)

            x_axis = numpy.arange(len(years))
            plot.figure(figsize=(10, 5))
            plot.bar(x_axis - 0.2, total_male_deaths, width=0.4, label='Male')
            plot.bar(x_axis + 0.2, total_female_deaths, width=0.4, label='Female')

            plot.title('Deaths of male and female per year')
            plot.xticks(x_axis, years)
            plot.legend()
            plot.show()

# cli()
