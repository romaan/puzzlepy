
def subset(aList: list[int], branch: list, sol: list) -> None:
    if len(aList) == 0:
        sol.append(branch)
        return None
    element: int = aList[0]
    included_set: list[int] = branch.copy()
    included_set.append(element)
    # Include the element
    subset(aList[1:], included_set, sol)
    # Exclude the element
    excluded_set: list[int] = branch.copy()
    subset(aList[1:], excluded_set, sol)


answer = []
subset([1, 2, 3, 4], [], answer)
print(answer)
