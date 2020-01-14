def main():
    menuDictionary = {'breakfast':[],'lunch':[], 'dinner':[]}
    print(menuDictionary)
    choiceOfMenu = ''
    while choiceOfMenu != 'q':
        choiceOfMenu = input('Enter the category (enter q to exit) ')
        if choiceOfMenu in menuDictionary:
            addOrDelete= input('Do you want to list, add or delete ')
            if addOrDelete =='add':

                addItem = input('Enter the item you want to add ')
                if addItem not in menuDictionary[choiceOfMenu]:

                    menuDictionary[choiceOfMenu].append(addItem)
                    print("Item added sucessfully")
                else:
                    print('Item already added in list')
                
            elif addOrDelete =='delete':
                deleteItem = input('Enter the item you want to delete ')
                if deleteItem in menuDictionary[choiceOfMenu]:

                    menuDictionary[choiceOfMenu].remove(deleteItem)
                    print(menuDictionary)
                else:
                    print('Item is not in list')
            else:
                print('entered choice is not available, try again')
        else:
            print('entered category is not available, try again')

if __name__ == "__main__":
    main()