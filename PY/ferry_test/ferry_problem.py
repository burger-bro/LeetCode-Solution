from itertools import combinations

class Person:
    def __init__(self, gender, limit, char):
        self.gender = gender
        self.limit = limit
        self.char = char

    def have_sex(self, other):
        pass
        
class SexWithSis(Person):
    def have_sex(self, other):
        return True if other.limit == "sister" else False

class SexWithMale(Person):
    def have_sex(self, other):
        return True if other.gender == "male" else False

class SexWithBro(Person):
    def have_sex(self, other):
        return True if other.limit == "brother" else False

class Carrier:
    def __init__(self, entity: Person):
        self.entity = entity

    def have_sex(self):
        if len(self.entity) > 2: return False
        c = combinations(self.entity, r=2)
        for i in c:
            if i[0].have_sex(i[1]):
                return True
        return False

    def join(self, crew):
        self.entity |= crew

    def leave(self, crew):
        self.entity -= crew

    def clear(self):
        self.entity = set()

    def __str__(self):
        return ','.join([c.char for c in self.entity])

mother = SexWithMale('female', 'none', "mother")
father = SexWithSis('male', 'none', "father")
brother = SexWithSis('male', 'brother', "brother")
sister = SexWithBro('male', 'sister', "sister")
stranger = SexWithBro('male', 'none', "stranger")

source = Carrier({mother, father, brother, sister, stranger})
# source = Carrier({mother, brother, sister})
ferry = Carrier(set())
dest = Carrier(set())

ans_list = []

import copy

def dfs(ans):
    p = source.entity
    c = combinations(p, r=2)
    for s1, s2 in c:
        crew = {s1, s2}
        ferry.join(crew), source.leave(crew), dest.join(crew)
        
        if not source.have_sex() and not ferry.have_sex() and not dest.have_sex():
            if not source.entity:
                print("why?")
                ans_list.append(copy.deepcopy(ans))
                return
            # print("yes?")
            for cr in dest.entity.copy():
                if cr is sister: continue
                cr = {cr}
                tmp = str(source)+'->'+str(dest)
                # print(source.entity)
                # print("tmp", tmp)
                ferry.clear(), ferry.join(cr), dest.leave(cr), source.join(cr)
                if not source.have_sex() and not ferry.have_sex() and not dest.have_sex():
                    # print("yes?")
                    # ans.append([source, dest])
                    tmp = tmp+'<-'+str(ferry)
                    # print(tmp)
                    # print(source.entity)
                    ans.append([tmp])
                    dfs(ans)
                dest.join(cr), source.leave(cr)
        ferry.clear(), source.join(crew), dest.leave(crew)


dfs([])
print(ans_list)
print(len(ans_list))
# print("len", len(ans_list))
# print("len", ans_list[0])
# print(ans_list[1])
