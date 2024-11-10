import numpy as np
from pathlib import Path
class output:
    """Create an output object for writing to file
        
        Args:
            N_samps (int): num of sample frames
            letter(string): letter of input data i.e. PA3-A
            d_k(list[list[float]]): d_k values
            s_k(list[list[float]]): s_k values
        """
    def __init__(self, N_samps, letter, d_k, s_k):

        self.N_samps = N_samps
        self.name = "pa3-"+letter+"Output.txt"
        self.d_k = d_k
        self.s_k = d_k
    def write_to_file(self):
        file_path = Path(f"../outputs/{self.name}")
        with open(file_path, mode='w') as fp:
            fp.write(str(self.N_samps)+" "+self.name+"\n")
            for i in self.N_samps:
                fp.write(self.d_k[i]+"\t"+self.s_k[i])