# Asking user to enter DNA sequence
sequence <- readline(prompt="Enter a DNA sequence: ")

# Convert the sequence object into a character vector
sequence <- as.character(sequence)

# calculating lenght of sequence
sequence_length <- nchar(sequence)

# calculating G'S and c's
num_Gs <- nchar(gsub("[^G]", "", sequence))
num_Cs <- nchar(gsub("[^C]", "", sequence))

# Compute the GC content of the sequence
gc_content <- (num_Gs + num_Cs) / sequence_length

# Print the GC content
print(paste("GC content:", round(gc_content * 100, 2), "%"))

