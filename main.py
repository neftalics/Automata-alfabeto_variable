import csv
class Automata:
    Q=" "
    alfabet = list()
    transitions = dict()
    finalStates = list()

    def __init__(self, Q, alfabet, transitions, finalStates ):
        self.Q=Q
        self.alfabet=alfabet
        self.transitions=transitions
        self.finalStates=finalStates
    
    def __init__(self):
        self.Q,self.alfabet,self.transitions,self.finalStates = csvRead("E2.csv")

    def validate(self):
        print("insert chain")
        chain= str(input())

        currentState = self.Q
        for i in chain:
            nextState=self.transitions[currentState][self.alfabet.index(i)]
            currentState=nextState
        
        return currentState in self.finalStates

def csvRead(Filename):
    
    Q=" "
    alfabet= list()
    automata = dict()
    finalStates = list()

    file = open(Filename)
    data = csv.reader(file)

    for row in data:
        if not row:
            continue

        if row[0] == "estado inicial":
            continue
        
        if row[0] == "alfabeto":
            break

        Q=row[0]

    for row in data:

        if not row:
            continue 

        if row[0] == "alfabeto":
            continue

        if row[0] == "matriz":
            break

        for i in row:
            alfabet.append(i)
    
    for row in data:
        if not row:
            continue

        if row[0] == "matriz":
            continue

        if row[0] == "estados finales":
            break
            
        transitions = list()
        for i in range(len(row)):
            if i != 0 :
                transitions.append(row[i])

        automata[str(row[0])]=transitions
    
    for row in data:
        if not row:
            continue

        if row == "estados finales":
            continue

        for finalState in row:
            finalStates.append(str(finalState))  

    return Q,alfabet,automata,finalStates 

if __name__ == "__main__":

    automata = Automata()
    print(automata.Q)
    print(automata.alfabet)
    print(automata.transitions)
    print(automata.finalStates)
    print("la cadena es",automata.validate())


    