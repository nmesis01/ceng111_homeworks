def check_month(month_calendar):
    breached_rules = []
    cost = 0
    #Rule 1(m)
    days_index = [x for x in range(0,len(month_calendar)) if month_calendar[x] == "m"]
    weeks = [month_calendar[0:5],month_calendar[5:10],month_calendar[15:20],month_calendar[20:]]
    count_week = [x.count("m")<2 for x in weeks]
    mod_days = [x%5 for x in days_index]
    if False in count_week:
        breached_rules.append(1)
    elif len(mod_days) and mod_days.count(mod_days[0]) != len(mod_days):
        breached_rules.append(1)
    else:
        cost += 10*month_calendar.count("m")
    #Rule2(f)
    days_index = [x for x in range(0,len(month_calendar)) if month_calendar[x] == "f"]
    if len(days_index) > 2:
        breached_rules.append(2)
    elif len(days_index) == 2 and abs(days_index[0]-days_index[1])==1 and days_index[0]%5 != 4:
        breached_rules.append(2)
    else:
        cost += 20*month_calendar.count("f")
    #Rule3(b)
    days_index = [x for x in range(0,len(month_calendar)) if month_calendar[x] == "b"]
    intervening_days = [2 for x in range(0,len(month_calendar)-1) if month_calendar[x] == "b" and month_calendar[x+1] == "b" and x%5==4 and (x+1)%5==0] + [days_index[x+1]-days_index[x]-1 for x in range(0,len(days_index)-1) if days_index[x+1]%5>days_index[x]%5 and (days_index[x+1]-days_index[x]-1)<3]
    cost += 30*(month_calendar.count("b")+sum(intervening_days))
    #Rule4(g)
    days_index = [x for x in range(0,len(month_calendar)) if month_calendar[x] == "g"]
    mod_days = [x%5 for x in days_index]
    if mod_days.count(2) > 1:
        breached_rules.append(4)
    else:
        cost += 50*month_calendar.count("g")
    #Rule5(a1)
    days_index = [x for x in range(0,len(month_calendar)) if month_calendar[x] == "a1"]
    mod_days = [x%5 for x in days_index]
    if 0 in mod_days or 2 in mod_days or 3 in mod_days:
        breached_rules.append(5)
    else:
        cost += 32*month_calendar.count("a1")
    #Rule6(a2)
    days_index = [x for x in range(0,len(month_calendar)) if month_calendar[x] == "a2"]
    breached_days = [x for x in days_index if month_calendar[x-1] == "a1" and x%5 != 0]
    if len(breached_days) > 0:
        breached_rules.append(6)
    else:
        cost += 27*month_calendar.count("a2")
    #Rule7(n)
    days_index = [x for x in range(0,len(month_calendar)) if month_calendar[x] == "n"]
    mod_days = [x%5 for x in days_index]
    if 3 in mod_days or 4 in mod_days:
        breached_rules.append(7)
    else:
        cost_list = [5**x for x in range(1,len(days_index))]
        cost += sum(cost_list)
    if len(breached_rules) > 0:
        return breached_rules
    else:
        return cost
    