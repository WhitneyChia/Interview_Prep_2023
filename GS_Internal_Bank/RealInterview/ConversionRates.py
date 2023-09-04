"""
Given several from unit, to unit, and a conversion rate.
Write a function that takes the two units and returns the conversion rate.

Example 1:
[[inch, foot, 12]
[foot, yard, 3]]

get_conversion_rate(inch, yard) -> 36
get_conversion_rate(yard, inch) -> 0.0277778

Example 2:
[[inch, centimeter, 2.54]
[inch, meter, 0.0254]]

get_conversion_rate(meter, centimeter) -> 100
"""


class Solution:

    def __init__(self, conversions: list):
        self.weights = {}
        self.graph = self.create_graph(conversions)
        self.visited = set()

    def create_graph(self, conversions:list):
        adj_list = {}
        for from_unit, to_unit, conversion_rate in conversions:
            if from_unit in adj_list:
                adj_list[from_unit].append(to_unit)
            else:
                adj_list[from_unit] = [to_unit]

            if to_unit in adj_list:
                adj_list[to_unit].append(from_unit)
            else:
                adj_list[to_unit] = [from_unit]

            self.weights[from_unit + to_unit] = conversion_rate
            self.weights[to_unit + from_unit] = 1/conversion_rate

        return adj_list

    def get_conversion_rate(self, from_unit: str, to_unit: str):
        for neighbor in self.graph[from_unit]:
            self.dfs(from_unit, from_unit, neighbor, to_unit)

        if from_unit + to_unit not in self.weights:
            return -1
        self.visited = set()
        return self.weights[from_unit + to_unit]

    def dfs(self, original_source: str, from_unit: str, to_unit: str, target: str):

        if original_source + to_unit not in self.weights:
            self.weights[original_source + to_unit] = self.weights[original_source + from_unit] * self.weights[from_unit + to_unit]

        self.visited.add(to_unit)
        if to_unit == target:
            return

        for neighbor in self.graph[to_unit]:
            if neighbor not in self.visited:
                self.dfs(original_source, to_unit, neighbor, target)


if __name__ == "__main__":

    # Example 1:
    conversions = [["inch", "foot", 12],  ["foot", "yard", 3]]
    sol = Solution(conversions)
    # get_conversion_rate(inch, yard) -> 36
    print("inch to yards -> 36")
    print(sol.get_conversion_rate("inch", "yard"))
    # get_conversion_rate(yard, inch) -> 0.0277778
    print("yard to inches -> 0.0277778")
    print(sol.get_conversion_rate("yard", "inch"))

    # Example
    # 2:
    conversions2 = [["inch", "centimeter", 2.54], ["inch", "meter", 0.0254]]
    sol2 = Solution(conversions2)
    # get_conversion_rate(meter, centimeter) -> 100
    print("meter to centimeter -> 100")
    print(sol2.get_conversion_rate("meter", "centimeter"))

    # Example
    # 3:
    conversions3 = [["ounces", "pounds", 0.0625], ["pounds", "kilograms", 0.453592], ["kilograms", "grams", 1000], ["tons", "pounds", 2000]]
    sol3 = Solution(conversions3)
    # get_conversion_rate(ounces, kilograms) -> 0.0283495
    print("ounce to kilogram -> 0.0283495")
    print(sol3.get_conversion_rate("ounces", "kilograms"))
    print("ton to gram -> 907185")
    print(sol3.get_conversion_rate("tons", "grams"))
