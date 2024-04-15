import random

class Person:

    def __init__(self, id : int, skills : set, skill_count : int) -> None:
        self.id = id
        self.skills = skills
        self.skill_count = skill_count

    def __str__(self) -> str:
        return(f"ID: {self.id}\n Skills: {self.skills}\n--------")   

    def __repr__(self) -> str:
        return self.__str__()
    
class People:
    def __init__(self) -> None:
        self.people

def greedy_set_cover(universe, sets):
    covered = set()
    cover = []

    while covered != universe:
        max_set = max(sets, key=lambda s: len(s - covered))
        cover.append(max_set)
        covered |= max_set

    return cover

def local_search_set_cover(universe, sets):
    solution = greedy_set_cover(universe, sets)
    uncovered = universe - set().union(*solution)

    while uncovered:
        best_improvement = 0
        best_set = None

        for s in sets:
            if s not in solution:
                improvement = len(uncovered & s)
                if improvement > best_improvement:
                    best_improvement = improvement
                    best_set = s

        if best_set:
            solution.append(best_set)
            uncovered -= best_set
        else:
            break

    return solution

# Example usage:
universe = {1, 2, 3, 4, 5}
sets = [{1, 2, 3}, {2, 3, 4}, {4, 5}]

N, K = map(int, input().split())
people = []
total_skills = set(range(K))
for i in range(N):
    skill_count = int(input())
    skills = set(map(int, input().split()))    
    person = Person(i, skills, skill_count)

    people.append(person)

print(people, total_skills)



print("Greedy set cover solution:", greedy_set_cover(universe, sets))
print("Local search set cover solution:", local_search_set_cover(universe, sets))
