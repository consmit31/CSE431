import heapq

N, K = map(int, input().split())
agents = []
for i in range(N):
    skills_count = int(input())
    skills = list(map(int, input().split()))
    agents.append((i, skills))

covered_skills = set()

selected_agents = []

agents.sort(key=lambda x: len(x[1]))

for person_id, skills in agents:
    if len(covered_skills) == K:
        break
    for skill in skills:
        if skill not in covered_skills:
            covered_skills.add(skill)
    selected_agents.append(person_id)

print(len(selected_agents))
print(' '.join(map(str, selected_agents)))
