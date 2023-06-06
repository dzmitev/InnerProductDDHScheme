# Inner Product Scheme Based on the DDH Assumption

As part of my diploma thesis titled "Funkcijsko šifriranje in shema za računanje skalarnih produktov" in Slovenian or "Functional Encrpytion and a Scheme for Computing Inner Products" in English, I implemented the Inner Product scheme based on the DDH assumption from Abdalla, Bourse, De Caro and Pointcheval in Python. I also performed two tests to measure the execution time of the implemented functions and another test to measure the time needed for generating a safe prime and a generator of the quadratic residues group modulo a safe prime. The source code for the scheme can be found in the file **Scheme.py**, while the source code for the tests is available in the files **SchemeTesting_RandomGrades.ipynb**, **SchemeTesting_LargerNumbers.ipynb** and **SchemeTesting_Generators**.

The operations are performed in the group of quadratic residues modulo a safe prime. It is believed that the DDH assumption holds in these groups. The parameter $l$ indicates the dimension of the vectors while the parameter $B$ indicates the upper bound on the individual components of the vectors.

For the computation of the final discrete logarithm, I implemented the Baby-step giant-step algorithm and its source code can also be found in the file **Scheme.py**. 

Since the generation of safe primes and generators of the quadartic residue group is indedependant on $l$ and $B$, I also measured the time needed for that. This is sensible, because in practice once we generate a safe prime and a generator of the quadratic residues group we can use them multiple times.
The generated safe primes are 1024-bits. The source code is in **Testing_SafePrime_Generator.ipynb**.

In **SchemeTesting_RadnomGrades.ipynb** I computed a weighted sum of randomly chosen grades of some student, where the weight of each grade is the amount of ECTS of the corresponding subject. The grades are randomly chosen, but the ECTS credits assigned to each subject represent the ECTS of the subjects I had to complete to finish my bachelor's program, excluding the diploma seminar. 
The parameter $l$ in this example is 30, since I completed 30 subjects on my undergraduate program, while $B$ is equal to 11, since the maximum possible grade is 10 and no subject was worth more than 10 ECTS. 

In **SchemeTesting_LargerNumbers.ipynb** I computed the inner products between random vectors of dimension 100 with individual components less than 10 000 (so $l$ = 100 and $B$ = 10 000). The goal was to demonstrate that the scheme can also be useful in a more realistic environment, where the vectors are of higher dimensions and the individual components of the vectors are significantly larger compared to the previous test. 

In both tests we used 1024-bit safe primes. The measured time results can be found in the image **measured__time.jpg**.
