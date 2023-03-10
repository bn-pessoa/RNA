import numpy as np
from sklearn import datasets

class RNA:  # implementação simples de RNA, rede neural com matriz supervionada
  
  def __init__(self, inputs, labels):
 
        n_examples = np.shape(inputs)[0]
        self.inputs = self.add_bias(inputs, n_examples)
        self.labels = labels       
        n_inputs = np.shape(self.inputs)[1]
        n_outputs = np.shape(labels)[1]       
        self.weights = np.random.rand(n_inputs, n_outputs)

        
  def add_bias(self, inputs, n_examples): # uma entrada a mais (bias) contendo o valor -1 garantindo que haverá algum valor na atualização da rede
        shape = (n_examples, 1) 
        # multiplica todos por -1       
        bias = -np.ones(shape)
        return np.concatenate((inputs, bias), axis=1)

  def forward(self, inputs): # função de ativação (forward) que limita a saída do neurônio
        # calculo de ativação: h        
        activations = np.dot(inputs, self.weights)
        # limitar as ativações (>0 ativa, <0 não ativa)
        saida = np.where(activations > 0, 1, 0)
        return saida
    
  def train(self, eta, n_iterations): # função de treinamento da rede neural (Para treinar uma rede devemos passar os dados de entrada diversas vezes)
        # training
        for n in range(n_iterations):
            print("iteração" + str(n))
            # executa a rede
            activations = self.forward(self.inputs)
            # calcula o erro: y - t
            erro = activations - self.labels
            # transpoe a matriz de entrada para fazer a multiplicacao
            transposed_in = np.transpose(self.inputs)
            # atualiza os pesos: wi = wi * -n * erro * xi
            self.weights -= eta * np.dot(transposed_in, erro)

            print(self.weights)
            print("----------------------------------------------------")

print("Iniciando a rede neural")

# entrada AND
inputs_training = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print(inputs_training)

# resultado esperado depois do treinamento
output_labels = np.array([[0], [0], [0], [1]])
print(output_labels)

rna = RNA(inputs_training, output_labels)

print( rna.add_bias(inputs_training, np.shape(inputs_training)[0]))

input_tests = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

input_tests = rna.add_bias(input_tests, np.shape(inputs_training)[0])

print("Antes de treinar...")
print(rna.forward(input_tests))

# treinamento
rna.train(0.25, 10)

print("Depois training...")
print(rna.forward(input_tests))
