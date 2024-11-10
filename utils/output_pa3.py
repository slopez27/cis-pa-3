import numpy as np
from pathlib import Path
class output:
    """Create an output object for writing to file
        
        Args:
            N_samps (int): num of sample frames
            name(string): name of input data i.e. PA3-A
            d_k(list[list[float]]): d_k values
            s_k(list[list[float]]): s_k values
        """
    def __init__(self, N_samps, name, d_k, s_k):

        self.N_samps = N_samps
        self.name = name+"-Output.txt"
        self.d_k = d_k
        self.s_k = d_k
    def write_to_file(self):
        file_path = Path(f"../outputs/{self.name}")
        with open(file_path, "w") as fp:
            fp.write(str(self.N_samps)+" "+self.name+"\n")
            for i in range(self.N_samps):
                mag_diff = np.linalg.norm(np.subtract(self.d_k[i],self.s_k[i]))
                remove = str.maketrans("","",'[],')
                d_k = str(self.d_k[i]).translate(remove)
                s_k = str(self.s_k[i]).translate(remove)
                fp.write(d_k + "\t" + s_k + "\t" + str(mag_diff)+"\n")

N_samps = 2
letter = 'pa3-a'
d_k = [[1,2,3],[4,5,6]]
s_k = [[0,0,0],[0,0,0]]
test = output(N_samps, letter, d_k, s_k)
test.write_to_file()