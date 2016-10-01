import sys
import json

class NondeterministicFiniteAutomata(object):

	def __init__(self, definition):
		self.definition = definition

	def compute(self, string):
		return self.accept(self.definition['q0'], string)

	def epsilon_transition(self, state):
		return self.definition['delta'].get(state, dict()).get('epsilon', [])

	def transition(self, state, char):
		next_states = self.definition['delta'].get(state, dict()).get(char, [])
		epsilon_next_states = []
		for next_state in next_states:
			epsilon_next_states.extend(self.epsilon_transition(next_state))

		next_states.extend(epsilon_next_states)
		return next_states

	def accept(self, state, string):
		if(len(string) == 0):
			return state in self.definition['f']

		char = string[0]
		next_states = self.transition(state, char)
		for next_state in next_states:
			if self.accept(next_state, string[1:]):
				return True

		return False

def parse_definition(definition_file_path):
	return json.loads(open(definition_file_path, 'r').read())

if __name__ == '__main__':
	nfa_definition = parse_definition(sys.argv[1])
	string = sys.argv[2]

	nfa = NondeterministicFiniteAutomata(nfa_definition)
	print(nfa.compute(string))
