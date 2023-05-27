# Inner Product Scheme based on the DDHS assumption

As part of my diploma thesis titled "Funkcijsko šifriranje in shema za računanje skalarnih produktov" in Slovenian or "Functional Encrpytion and a Scheme for Computing Inner Products" in English, I implemented in Python the Inner Product scheme based on the DDH assumption from Abdalla, Bourse, De Caro and Pointcheval. I also perfomed two tests to see how much time is needed for the execution of the implemented functions. One can find the source code of the scheme in the file **Scheme.py** and the source code of the tests in the files **SchemeTesting_Grades.ipynb** and **SchemeTesting_LargerNumbers.ipynb**. 

The operations are performed in the group of quadratic residues modulo a safe prime. It is believed that in these groups the DDH assumption holds. 

For the computation of the final discrete logarithm I implemented the Baby-step giant-step algorithm, for which the source code can also be found in the file  **Scheme.py**. 

In **SchemeTesting_Grades.ipynb** I computed a weighted mean of the grades of some student, where the weight of each grade is the amount of ECTS of the underlying subject. The grades are made up but the amount of ECTS per subject are the ECTS of the subjects that I had to pass in order to finish my bachelors program, excluding the diploma seminar.

In **SchemeTesting_LargerNumbers.ipynb** I computed an inner product between random vectors of length 100 with individual components less than $10^4$. The goal was to show that the scheme can also be useful in a more realistic environment, where the vectors are of a higher dimension and the components are significantly larger then in the previous test. 

One can find the measured time results in the image **measured_time.jpg**. 
