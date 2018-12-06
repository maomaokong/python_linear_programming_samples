#!/usr/bin/python

"""
Import packages / libraries
"""
from pulp import *


def factory_product_problem():
    """
    Use Case:

    1.  A factory can produce 2 products: screws and nails
    2.  Profit $20/ton for screws and $30/ton for nails
    3.  Maximum market demand/day: 400 tons for screws and 300 tons for nails
    4.  Production rate: 60 tons/hour for screws and 50 tons/hour for nails
    5.  Working days has 8 hours

    Question: How many tons of each product should be factory produce per day to maximise profit?

    Modeling the problem:
    1. Variables                : x, y = number of tons/day for screws and nails.
    2. Maximise profit          : (profit for screws * no of tons/day for screws)
                                    + (profit for nails * no of tons/day for nails)
                                    = (20 * x) + (30 * y)
    2. Screws constraint        : (maximum market demand for screws)
                                    = 0 <= x <= 400
    3. Nails constraint         : (maximum market demand for nails)
                                    = 0 <= y <= 300
    4. Working Hour constraint  : [(screws production tons/day) / (screws production rate)]
                                    + [(nails production tons/day) / (nails production rate)] <= working hour/day
                                    = (x/60) + (y/50) <= 8

    """
    # Create the 'prob' variable to contain the problem data
    prob = pulp.LpProblem(name='Factory Products Profit', sense=LpMaximize)

    # Create problem variables, lowBound=0 and upBound=None will fulfill the 'Screws' and 'Nails' constraints
    x = pulp.LpVariable(name='screws_tons_per_day', lowBound=0, upBound=400, cat=LpInteger)
    # Default upBound=300, assignment 1 changed the upBound to 200
    y = pulp.LpVariable(name='nails_tons_per_day', lowBound=0, upBound=300, cat=LpInteger)

    # The objective function is added to 'prob' first
    prob += (20 * x) + (30 * y), "Tons of each product; profit to be maximised per day"
    # The constrain are entered
    prob += (x * (1 / 60)) + (y * (1 / 50)) <= 8, "Working Hour constraint"

    # The problem data is written to an .lp file
    prob.writeLP('MaximisedProfit.lp')

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    print()
    print("Problem Name >> {pn}".format(pn=prob.name))
    print("Status >> {lp}".format(lp=LpStatus[prob.status]))
    # Output >>
    # Status: Optimal

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        print("{vn} = {vv}".format(vn=v.name, vv=v.varValue))
    # Output >>
    # nails_tons_per_day = 300.0
    # screws_tons_per_day = 120.0

    # The optimised objective function value is printed to the screen
    print("Ton for each product per day to maximise profit = {ob}".format(ob=value(prob.objective)))
    # Output >>
    # Ton for each product per day to maximise profit = 11400.0


def advertising_campaign_problem():
    """
    Use Case:

    1. An advertising agency wants to run a campaign for a new product on print media and TV.
    2. A print advertisement cost $20,000 and can reach 1 million people
    3. A TV advertisement costs $50,000 and can reach 2 million people
    4. Assume for simplicity that different advertisements reach different people
    5. There can be at most 40 advertisements on print and 15 advertisements on TV
    6. The agency has a budget of $1 million for the campaign

    Question: What is the best campaign that will reach the maximum number of people?

    Modeling the problem:
    1. Variables                : x = Print Media, y = TV
    2. Reach how many people?   : (Print Media can reach 1 million people)
                                    + (TV Media can reach 2 million people)
                                    = (1,000,000 * x) + (2,000,000 * y)
    3. Cost for each Media      : ($20,000 * x) + ($50,000 * y) <= $1,000,000
    4. Print Media constraint   : (most 40 advertisement on print)
                                    = 0 <= x <= 40
    5. TV Media constraint       : (most 15 advertisement on TV)
                                    = 0 <= y <= 15
    """
    # Create the 'prob' variable to contain the problem data
    prob = pulp.LpProblem(name='Advertisement Campaign', sense=LpMaximize)

    # Create problem variables, lowBound=0 and upBound=None will fulfill the 'Print' and 'TV' constraints
    x = pulp.LpVariable(name='run_no_of_print_media', lowBound=0, upBound=40, cat=LpInteger)
    y = pulp.LpVariable(name='run_no_of_tv_media', lowBound=0, upBound=15, cat=LpInteger)

    # The objective function is added to 'prob' first
    prob += (1000000 * x) + (2000000 * y), "Number of maximum people reach with both media"
    # The constrain are entered
    prob += (20000
             * x) + (50000 * y) <= 1000000, "Cost constraint"

    # The problem data is written to an .lp file
    prob.writeLP('AdvertisementCampaign.lp')

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    print()
    print("Problem Name >> {pn}".format(pn=prob.name))
    print("Status >> {lp}".format(lp=LpStatus[prob.status]))
    # Output >>
    # Status: Optimal

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        print("{vn} = {vv}".format(vn=v.name, vv=v.varValue))
    # Output >>
    # run_no_of_print_media = 40.0
    # run_no_of_tv_media = 4.0

    # The optimised objective function value is printed to the screen
    print("Maximum people reach by using both media = {ob}".format(ob=value(prob.objective)))
    # Output >>
    # Maximum people reach by using both media = 48000000.0


def main():
    #pulp.pulpTestAll()

    factory_product_problem()

    advertising_campaign_problem()


if __name__ == '__main__':
    main()
