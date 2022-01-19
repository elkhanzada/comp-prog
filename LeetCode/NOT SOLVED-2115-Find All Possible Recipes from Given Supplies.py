from typing import List
import ast


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        created_recipes = []
        for i, x in enumerate(recipes):
            spec = ingredients[i]
            for ing in spec:
                if ing not in supplies:
                    break
            else:
                created_recipes.append(x)
                supplies.append(x)
        return created_recipes


if __name__ == '__main__':
    s = Solution()
    print(s.findAllRecipes(ast.literal_eval(input("recipes = ")), ast.literal_eval(input("ingredients = ")),
                           ast.literal_eval(input("supplies = "))))
