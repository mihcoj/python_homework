class FastaParser(object):
	def __init__(self, in_file):
		self.in_file = in_file

		try: (".fasta" in in_file) == True
		except ValueError:
			raise Exception("%s is not a .fasta file." % (in_file))

		try:  os.path.exists(in_file) == True
		except IOError:
			raise Exception("%s can not be found." % (in_file)) 
