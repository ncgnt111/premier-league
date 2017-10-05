import random

# Список команд
teams_list = ["Лестер Сити", "Арсенал", "Тоттенхэм Хотспур", "Манчестер Сити", "Манчестер Юнайтед", "Саутгемптон",
              "Вест Хэм Юнайтед", "Ливерпуль", "Сток Сити", "Челси", "Эвертон", "Суонси Сити", "Уотфорд",
              "Вест Бромвич Альбион", "Кристал Пэлас", "Борнмут", "Сандерленд", "Ньюкасл Юнайтед", "Норвич Сити",
              "Астон Вилла"]

# Структура, хранящая всю статистику по командам - словарь all_stat_dict
# В качестве ключа - название команды
all_stat_dict = {}

for team in teams_list:
    all_stat_dict[team] = {"Wins":0, "Loses":0, "Draws":0, "Goals":0, "Misses":0, "Scores":0, "Place":0}

# Структура, хранящая результаты матчей - словарь result_match_dict
# В качестве ключа - кортеж (team1, team2)
result_match_dict = {}

# Заполнение словаря result_match_dict, хранящего результаты матчей, случайно сгенерированными числами
for team_i in teams_list:
    for team_j in teams_list:
        if (team_i == team_j):
               continue    
        result_match_dict[(team_i, team_j)] = (random.randint(0, 3), random.randint(0, 3))

# Функция вывода результата отдельного матча
def print_match_result(team_x, team_y):
        print("{:^20} - {:^20} {:>}:{:>}".format(team_x, team_y,
        result_match_dict[(team_x, team_y)][0], result_match_dict[(team_x, team_y)][1]))
    
# Вывод результатов всех матчей
for (team_i, team_j) in result_match_dict:
        print_match_result(team_i, team_j)
        
print("\n")

# Теперь, основываясь на данных в result_match_dict, нужно заполнить all_stat_dict
for (team_i, team_j) in result_match_dict:
    # Занесение забитых и пропущенных мячей
    all_stat_dict[team_i]["Goals"] += result_match_dict[(team_i, team_j)][0]
    all_stat_dict[team_i]["Misses"] += result_match_dict[(team_i, team_j)][1]
    
    all_stat_dict[team_j]["Goals"] += result_match_dict[(team_i, team_j)][1]
    all_stat_dict[team_j]["Misses"] += result_match_dict[(team_i, team_j)][0]   
    
    # Занесение побед, поражений, ничьих и очков
    if result_match_dict[(team_i, team_j)][0] > result_match_dict[(team_i, team_j)][1]:
        all_stat_dict[team_i]["Wins"] += 1
        all_stat_dict[team_i]["Scores"] += 3
           
        all_stat_dict[team_j]["Loses"] += 1
    if result_match_dict[(team_i, team_j)][0] < result_match_dict[(team_i, team_j)][1]:
        all_stat_dict[team_j]["Wins"] += 1
        all_stat_dict[team_j]["Scores"] += 3
        
        all_stat_dict[team_i]["Loses"] += 1
    if result_match_dict[(team_i, team_j)][0] == result_match_dict[(team_i, team_j)][1]:
        all_stat_dict[team_i]["Draws"] += 1
        all_stat_dict[team_i]["Scores"] += 1
        
        all_stat_dict[team_j]["Draws"] += 1
        all_stat_dict[team_j]["Scores"] += 1

        
# Клуб, набравший больше всех очков, получает чемпионский титул.
# В случае равенства очков место определяется по разнице мячей.
# В случае равенства разницы мячей место определяется по забитым голам.
# Если и после этого определить приоритет не удаётся,
# команды занимают одну и ту же строчку турнирной таблицы.
        

# Поскольку Python гарантирует стабильную сортировку, сделаем следующее.
# Вначале сортировка по количеству забитых мячей
sorted_list = sorted(all_stat_dict.items(), key = lambda x: x[1]["Goals"], reverse = True)

# Затем повторная сортировка по разнице забитых и пропущенных мячей
sorted_list = sorted(sorted_list, key = lambda x: x[1]["Goals"] - x[1]["Misses"], reverse = True)

# В последнюю очередь сортировка по количеству очков
sorted_list = sorted(sorted_list, key = lambda x: x[1]["Scores"], reverse = True)


# После сортировки необходимо присвоить командам соответствующие места в турнирной таблице
sorted_list[0][1]["Place"] = 1

for i in range(1, len(sorted_list)):
    if sorted_list[i][1]["Scores"] == sorted_list[i - 1][1]["Scores"]:
        if ((sorted_list[i][1]["Goals"] - sorted_list[i][1]["Misses"]) < (sorted_list[i-1][1]["Goals"] - sorted_list[i-1][1]["Misses"])):      
            sorted_list[i][1]["Place"] = sorted_list[i - 1][1]["Place"] + 1
        elif ((sorted_list[i][1]["Goals"] - sorted_list[i][1]["Misses"]) == (sorted_list[i-1][1]["Goals"] - sorted_list[i-1][1]["Misses"])):
            if ((sorted_list[i][1]["Goals"]) < (sorted_list[i-1][1]["Goals"])):
                sorted_list[i][1]["Place"] = sorted_list[i - 1][1]["Place"] + 1
            elif ((sorted_list[i][1]["Goals"]) == (sorted_list[i-1][1]["Goals"])):
                sorted_list[i][1]["Place"] = sorted_list[i - 1][1]["Place"]          
    else:
        sorted_list[i][1]["Place"] = sorted_list[i - 1][1]["Place"] + 1

# Вывод итоговой таблицы чемпионата
print("{:^10} | {:^20} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10}".format
      ("Place", "Team", "Wins", "Draws", "Loses", "Goals", "Misses", "Scores"))
print("{0:^10}  {1:^20}  {0:^10}  {0:^10}  {0:^10}  {0:^10}  {0:^10}  {0:^10}".format
      ("-----------","---------------------"))

for i in range(0, len(sorted_list)):
    print("{:^10} | {:^20} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10}".format
          (sorted_list[i][1]["Place"], sorted_list[i][0], sorted_list[i][1]["Wins"],
           sorted_list[i][1]["Draws"], sorted_list[i][1]["Loses"], sorted_list[i][1]["Goals"],
           sorted_list[i][1]["Misses"], sorted_list[i][1]["Scores"]))
    
print("\n")

# Вывод результата матча
print_match_result("Кристал Пэлас","Борнмут")

