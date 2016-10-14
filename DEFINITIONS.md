## Definition

To run on this simulator a nondeterministic finite automata must be defined as a json object with the following keys (left) and values (right):

1. Q: Array os states,
2. sigma: Array of characters composing the alphabet,
3. delta: A json object, representing the transition function as follows:
	- Every key in delta represents an state S in Q. Every value is a json object representing the possible transitions from the state S, as follows:
		- Every key in delta[S] represents a character "char" that must be read from input, or "epsilon" meaning the empty string;
		- The value is an Array of the states that are reached being on state S and reading "char" or "epsilon"
4. q0: String representing the start state
5. F: Array of Strings, representing the accept states

## Computation

A **formal definition** of computation on this simulator is very similar to the formal definition of computation on a nondeterministic finite automata, being:

Let N be an NFA defined as described above and *w* be a string over the alphabet "sigma". We say that N accepts *w* if we can write *w* as *w* = *y1y2y3...ym* where each *yi* is a member of "sigma" or "epsilon" and a sequence of states *r0,r1,r2...rm* exists in *Q* with three conditions:

1. *r0* = *q0*
2. *ri+1* ∈ "delta"["*ri*"]["*yi+1*"], for *i=0,...,m-1*, or *ri+1* ∈ "delta"["*rn*"]["*yi+1*"] for some *n* such that *rj+1* ∈ "delta"["*rj*"]["epsilon"], for *j=0...n-1*
3. *rm* ∈ "F" or ∃ *rn* ∈ "F" such thath *rm+1* ∈ "delta"["*rm*"]["epsilon"], for *j=rm...rn*


## Pergunta do professor 

Para que o meu simulador aceitasse o autômato descrito tive que alterar duas coisas nele e na descrição da computação acima - isso para que as epsilon transições pudessem ser levadas em conta mesmo sem nenhum caracter ter sido lido:

1ª: Além de verificar se o estado em que se está ao terminar de ler a string é final, considerar também se qualquer estado atingível apenas por epsilon-transições a partir de tal estado é final. Em qualquer um dos casos o autômato deve aceitar a String.

2º: Depois de verificar que nenhuma das transições a partir de um estado lendo caracteres resultou em uma aceitação (não se chegou ao final da string em estado final ou estado que pode alcançar estado final a partir apenas de epsilon-transições), realizar as epsilon-transições desse estado e realizá-las, enviando a mesma string (sem ler nada) para o teste a partir de cada estado alcançável usando apenas uma epsilon-transição. Nesse caso, porém, a epsilon-transição usada é "salva" (enviada como parâmetro na recursão) para que a mesma não possa mais ser usada até que um caracter seja lido. Isso é feito para evitar que a computação entre em loop.
