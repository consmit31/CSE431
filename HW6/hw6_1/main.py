class Person:

    def __init__(self, id : int, skills : set, skill_count : int) -> None:
        self.id = id
        self.skills = skills
        self.skill_count = skill_count

    def __str__(self) -> str:
        return(f"ID: {self.id}\n Skills: {self.skills}\n--------\n")   

    def __repr__(self) -> str:
        return self.__str__()

def greedy_set_cover(skills, people):
    covered = set()
    cover = []

    while covered != skills:
        max_person = max(people, key=lambda p: len(p.skills - covered)) 
        cover.append(max_person)
        covered |= (max_person.skills)

    return cover

def main():
    N, K = map(int, input().split())
    people = []
    total_skills = set(range(K))
    for i in range(N):
        skill_count = int(input())
        skills = set(map(int, input().split()))    
        person = Person(i, skills, skill_count)

        people.append(person)

    selected = greedy_set_cover(total_skills, people)
    print(len(selected))

    ids = []
    for p in selected:
        ids.append(str(p.id))
    print(" ".join(ids))


main()


