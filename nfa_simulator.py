import sys
import json

class NondeterministicFiniteAutomata(object):

	def __init__(self, definition):
		self.definition = definition

	def compute(self, string):
		return self.accept(self.start_state(), string)

	def accept(self, state, string):
		if(len(string) == 0):
			return self.is_final_state(state)

		char = string[0]
		remaining_string = string[1:]

		for next_state in self.possible_next_states(state, char):
			if self.accept(next_state, remaining_string):
				return True

		return False

	def possible_next_states(self, state, char):
		next_states = []
		
		for next_state in self.transition(state, char):
			next_states.append(next_state)
			next_states.extend(self.transition(next_state, 'epsilon'))

		return next_states

	# Auxiliar methods

	def start_state(self):
		return self.definition['q0']

	def is_final_state(self, state):
		return state in self.definition['f']

	def transition(self, state, char):
		return self.definition['delta'].get(state, dict()).get(char, [])

if __name__ == '__main__':
	definition = json.loads(open(sys.argv[1], 'r').read())
	string = sys.argv[2]

	nfa = NondeterministicFiniteAutomata(definition)
	print(nfa.compute(string))
