import sys, re, platform
if '3.' not in platform.python_version():
	raise Exception('This version of python is not supported')

fasta  = sys.argv[1]
def main(fasta):
	outfasta = open(sys.argv[1].replace('.fasta','_PARSED.fasta'), 'w')
	line_n = 0
	line_buffer = 0
	seq_read = False
	fasta_rec = 0
	with open(fasta) as f:
		for line in f:
			line_n += 1
			if line_n == 100:
				line_n = 0
				line_buffer += 100
				print('Processed {} lines '.format(line_buffer))
			if '>' not in line: ## id the fasta header
				if seq_read is True:
					seqrecord = line.strip('\n')
					outfasta.write(seqrecord)
			else:
				fasta_rec += 1
				seq_read = True	
				if line_n == 1:
					outfasta.write(line)
				else:
					outfasta.write('\n'+line)
	outfasta.close()
	print('Processed {} fasta records and wrote to file {} '.format(fasta_rec, str(sys.argv[1].replace('.fasta','_PARSED.fasta'))))
if __name__ == '__main__':
	main(fasta)
