master = []
p1_lead, p2_lead = [], []
p1total, p2total = 0, 0

for _ in range(int(input())):
    p1, p2 = map(int, input().split())

    p1total += p1
    p2total += p2

    if p1total > p2total:
        p1_lead.append(p1total-p2total)
        p2_lead.append(p2total-p1total)
    else:
        p2_lead.append(p2total - p1total)
        p1_lead.append(p1total - p2total)
    print(p1_lead, p1total, p2_lead, p2total)

if max(p1_lead) > max(p2_lead):
    print(1, f'{max(p1_lead)}')
else:
    print(2, f'{max(p2_lead)}')

print(p1_lead, p1total, p2_lead, p2total)
