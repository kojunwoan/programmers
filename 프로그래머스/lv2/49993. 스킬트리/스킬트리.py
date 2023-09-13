def solution(skill, skill_trees):
    return sum(skill.startswith(''.join(s for s in skill_tree if s in skill)) for skill_tree in skill_trees)