#dna base pair game Generated by Vishwesh and ATharva
import time

# Generating a random sequence of 6 nucleotides
import random
nucleotides = ['A', 'C', 'G', 'T']
sequence = ''.join(random.choices(nucleotides, k=6))
print(f"Sequence: {sequence}")

# Get the complementary sequence for checking user is right or not
def get_complementary_sequence(sequence):
    complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complementary_sequence = ''.join([complements[nucleotide] for nucleotide in sequence])
    return complementary_sequence

complementary_sequence = get_complementary_sequence(sequence)

#asking user for complimentry sequence
start_time = time.time()
time_limit = 10
while time.time() - start_time < time_limit:
    time_remaining = int(time_limit - (time.time() - start_time))
    user_input = input(f"Enter the complementary sequence ({time_remaining} seconds remaining): ")
    if user_input == complementary_sequence:
        print("You are a scientist, my man!")
        break
else:
    print("You tried so hard and got so far, but in the end it doesn't matter.")
    print("Time's up!")
