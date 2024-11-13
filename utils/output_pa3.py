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
        self.s_k = s_k
    def write_to_file(self):
        file_path = Path(f"../outputs/{self.name}")
        with open(file_path, "w") as fp:
            # Write the header line
            fp.write(f"{self.N_samps} {self.name}\n")

            # Write each sample frame
            for i in range(self.N_samps):
                mag_diff = np.linalg.norm(np.subtract(self.d_k[i], self.s_k[i]))
                
                # Format d_k and s_k to 2 decimal places
                d_k_str = " ".join(f"{value:.2f}\t" for value in self.d_k[i])
                s_k_str = " ".join(f"{value:.2f}\t" for value in self.s_k[i])
                
                # Write the formatted values
                fp.write(f"{d_k_str}\t\t{s_k_str}\t{mag_diff:.3f}\n")

