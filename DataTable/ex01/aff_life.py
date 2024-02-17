from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from typing import List


def main():
    country: str = 'Germany'
    df: pd.DataFrame | None = load('../data/life_expectancy_years.csv')
    if df is None:
        return None
    if country not in df.index:
        return None

    germany: pd.Series = df.loc[country]
    try:
        years: List[int] = [int(i) for i in germany.index]
        age: List[int] = [int(i) for i in germany.values]
    except (ValueError, Exception):
        return None

    fig, ax = plt.subplots()
    ax.set_title(f'{country} Life expectancy Projections')
    ax.set_ylabel('Life expectancy')
    ax.set_xlabel('Year')
    ax.plot(years, age)
    plt.show()


if __name__ == '__main__':
    main()
