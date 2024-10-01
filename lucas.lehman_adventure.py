def main():
    currentNode = "start"
    game = getGame()
    keepGoing = True
    while keepGoing:
        currentNode = playNode(game, currentNode)
        if currentNode == "quit":
            keepGoing = False


def getGame():
    game = {
      "start": ["You stumble across a sleeping dragon in the woods ", "Run away ", "run", "Try to fight it ", "fight"], 
      "run": ["The dragon wakes up from your loud footsteps and eats you", "Start over", "start", "Quit", "quit"], 
      "fight": ["You have a sword and a bow", "Use sword", "sword", "Use bow", "bow"], 
      "sword": ["You take out your sword and charge", "Stab it's eyes", "eyes", "Stab it's chest", "chest"], 
      "bow": ["You take out the bow and aim ", "Shoot it's eyes", "eyes2", "Shoot it's chest", "chest2"], 
      "eyes": ["You blind the dragon and it cries out in anger ", "Run away ", "run2", "Stab again", "stab"], 
      "chest": ["The sword ricochets back and the dragon eats you", "Start over", "start", "Quit", "quit"], 
      "eyes2": ["You blind the dragon and it cries out in anger ", "Run away ", "run2", "Shoot again ", "shoot"], 
      "chest2": ["The arrow bounces off, waking the dragon and it eats you", "Start over ", "start", "Quit", "quit"], 
      "run2": ["You successfully run away and continue on your journey", "Start over ", "start", "Quit", "quit"], 
      "stab": ["The sword ricochets back and the dragon eats you", "Start over ", "start", "Quit", "quit"], 
      "shoot": ["The arrow bounces off, waking the dragon and it eats you", "Start over ", "start", "Quit", "quit"], 
 }
    return game

def playNode(game, currentNode):
    nodeData = game[currentNode]
    print(nodeData[0])
    print(f"1) {nodeData[1]}")
    print(f"2) {nodeData[3]}")
    choice = input("Your choice: (1 or 2)")
    print()
    
    if choice == "1":
        return nodeData[2]
    if choice == "2":
        return nodeData[4]
    else:
        print("please enter a valid choice")
        return currentNode
main()
    
    


