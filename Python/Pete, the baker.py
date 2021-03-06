Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000}


————————————————————————————————————————————————————————————————————————————————————————————————————
Solution:
def cakes(recipe, available):
    # TODO: insert code
    
————————————————————————————————————————————————————————————————————————————————————————————————————
Example Tests:

test.describe('Testing Pete, the Baker')
test.it('gives us the right number of cakes')

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
test.assert_equals(cakes(recipe, available), 2, 'Wrong result for example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
test.assert_equals(cakes(recipe, available), 0, 'Wrong result for example #2')
    
    
————————————————————————————————————————————————————————————————————————————————————————————————————

Solution:

自己做的
def cakes(recipe, available):
    shuzu = []
    for x, y in recipe.items():
        try:
            shuzu.append(available[x]/y)
        except:
            return 0
    return min(shuzu)
    # TODO: insert code
    
    
    破费
    
————————————————————————————————————————————————————————————————————————————————————————————————————    
下面附上两个答案 比较不错的

def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)
  
  
def cakes(recipe, available):
  return min(available.get(k, 0) // v for k,v in recipe.iteritems())
  
  
要好好用get（key，0）  这个命令
