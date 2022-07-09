class TuringMachine:
    def __init__(self, d: dict[tuple, tuple], init_state: str, final_states: set[str], tape: list[str]) -> None:
        self.Tape = tape
        self.trans_fn = d
        self.final_states = final_states
        self.state = init_state
        self.head_pos = len(tape) // 2 # start at middle of tape
        self.halted = False

        assert(self.state not in final_states)
        assert(self.final_states) # Ensure that the Machine has some halt condition
    def read_tape(self) -> str:
        ''' Read the tape at the current head position ''' 
        return self.Tape[self.head_pos]
    def write(self, symbol: str) -> None:
        ''' Write the symbol to the current head position '''
        self.Tape[self.head_pos] = symbol
    def step(self) -> None:
        ''' Single iteration of the Machine '''
        if self.halted:
            return
        tape_symbol = self.read_tape()
        curr_state = (self.state, tape_symbol)
        trans_state = self.trans_fn[curr_state] # [new state, write symbol, direction to move head
        self.state = trans_state[0]
        if self.state in self.final_states:
            self.halted = True
            return

        self.write(trans_state[1])
        self.head_pos += trans_state[2] # Left or Right

if __name__ == "__main__":
    left, right = -1, 1
    
    tape = ['0']*100
    Final_States = {'HALT'}
    init_state = 'A'
    trans = {
                ('A', '0') : ('B', '1', right), 
                ('A', '1') : ('C', '1', left),
                ('B', '0') : ('A', '1', left), 
                ('B', '1') : ('B', '1', right),
                ('C', '0') : ('B', '1', left), 
                ('C', '1') : ('HALT', '1', right),
            }
    Machine = TuringMachine(trans, init_state, Final_States, tape)
    # Machine.Tape[Machine.head_pos] = '1'
    while not Machine.halted:
        Machine.step()
        print(' '.join([x if x=='1' else ' ' for x in Machine.Tape]))
