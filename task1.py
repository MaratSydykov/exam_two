
def country_information(name, **kwargs):
    print(f'{name}')
    for i in kwargs:
        print(f'{i} - {kwargs[i]}')

country_information(name='USA', population='330 million', is_democratic=True)
country_information(name='Kyrgyzstan', area='200 km2', have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])








