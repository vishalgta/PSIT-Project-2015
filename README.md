# American-Death-Probabilities
Create Visualize of the American Death Probabilities data.
since 1900 - 2011

##Requirement
- python3
      - numpy
      - matplotlib

###main.py

```
overall_death_probability_graph()
```
- [X] Create Overall death probability graph male and female.
blue represent as male and red represent as female.

---

```
death_probability_graph_in_bar_graph()
```
- [X] Create Death probability of each generation in bar graph, a graph points about death probability in each age.
- 0 - 3 baby
- 4 - 6 early childhood
- 7 - 12 middle childhood
- 13 -19 teenager
- 21 - 39 early adulthood
- 41 - 59 middle adulthood
- 61 - 119 old age

###data_tool.py
```
data_tool(sex)
```
load all data to dict form. ex. >>> {year: [death prob]}

by sex 1 == male, 2 == female and index of death prob list is age.
