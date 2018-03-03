from functions import find_all_restaurants_in_neighbourhood as farin, \
                        find_restaurant_coordinates as frc
    
def find_restaurants_to_shut(distance, list_of_epicentres):
    '''
    function find_restaurants_to_shut takes a float as distance and a list of
    points in the form of a list of lists and returns name of restaurants which
    have distances less than distance in a form of list of lists
    '''
    result = []
    
    # taking the points as x_cenre and y_centre
    for (x_centre, y_centre) in list_of_epicentres:
        restaurants = []
        
        # taking the highest and lowest coordinates that are possibly result
        xmax, xmin = int(x_centre+distance), int(x_centre-distance)
        ymax, ymin = int(y_centre+distance), int(y_centre-distance)
        
        # finding the possible restaurants from the possible coordinates
        for poss_x in range(xmin, xmax+1):
            for poss_y in range(ymin, ymax+1):
                poss_restaurants = farin(poss_x, poss_y)
                
                # checking the possible restaurants from a neighbourhood
                for restaurant in poss_restaurants:
                    x, y = frc(restaurant)
                    
                    # using the circle equation, if the condition is met
                    # the restaurant will be added to the result
                    if (x-x_centre)**2 + (y-y_centre)**2 < (distance)**2:
                        restaurants.append(restaurant)
                
                # sort the restaurants
                restaurants = sorted(restaurants)
                
        # adding the list of the restaurants into the result
        result.append(restaurants)

    return result


if __name__ == '__main__':
    # Run the sample inputs.
    print(find_restaurants_to_shut(1.0, [[3.0, 3.0]]))
    print(find_restaurants_to_shut(0.4, [[1.0, 1.0], [2.0, 2.0]]))
