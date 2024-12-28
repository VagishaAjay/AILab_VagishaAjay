from collections import defaultdict

# Define the knowledge base
knowledge_base = [
    # Rules
    {
        "if": [
            "American(x)",
            "Hostile(y)",
            "Sells(x, z, y)"
        ],
        "then": "Criminal(x)"
    },
    # Facts
    {"fact": "Hostile(CountryA)"},
    {"fact": "Owns(CountryA, Missile)"},
    {"fact": "Sells(Robert, Missile, CountryA)"},
    {"fact": "American(Robert)"}
]

# Unify function to check if two literals match
def unify(query, fact):
    substitutions = {}
    query_parts = query.split("(")
    fact_parts = fact.split("(")
    
    if query_parts[0] != fact_parts[0]:  # Predicate names must match
        return False, {}
    
    query_args = query_parts[1][:-1].split(",")  # Remove closing parenthesis and split args
    fact_args = fact_parts[1][:-1].split(",")
    
    if len(query_args) != len(fact_args):  # Argument lengths must match
        return False, {}
    
    for q, f in zip(query_args, fact_args):
        if q == f:  # Same constant
            continue
        elif q.islower():  # q is a variable
            substitutions[q] = f
        elif f.islower():  # f is a variable
            substitutions[f] = q
        else:  # Conflict
            return False, {}
    
    return True, substitutions

# Forward chaining algorithm
def forward_chain(kb, goal):
    facts = set()
    rules = []
    
    for item in kb:
        if "fact" in item:
            facts.add(item["fact"])
        elif "if" in item:
            rules.append(item)
    
    inferred = set()
    
    while True:
        new_inferred = set()
        
        for rule in rules:
            conditions = rule["if"]
            consequent = rule["then"]
            all_matched = True
            substitutions = defaultdict(list)
            
            # Check if all conditions are satisfied
            for condition in conditions:
                condition_matched = False
                for fact in facts:
                    is_match, sub = unify(condition, fact)
                    if is_match:
                        condition_matched = True
                        for k, v in sub.items():
                            substitutions[k].append(v)
                
                if not condition_matched:
                    all_matched = False
                    break
            
            # If all conditions are satisfied, infer the consequent
            if all_matched:
                for var, values in substitutions.items():
                    if len(set(values)) > 1:  # Conflict in substitutions
                        all_matched = False
                        break
                
                if all_matched:
                    for var, value in substitutions.items():
                        consequent = consequent.replace(var, value[0])
                    
                    if consequent not in facts and consequent not in inferred:
                        new_inferred.add(consequent)
        
        # Add new inferences to the facts
        if not new_inferred:
            break
        facts.update(new_inferred)
        inferred.update(new_inferred)
    
    # Check if the goal is in the facts
    return goal in facts

# Prove the goal
goal = "Criminal(Robert)"
result = forward_chain(knowledge_base, goal)
print(f"Is '{goal}' provable? {result}")
