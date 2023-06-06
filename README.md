# Inner Product Scheme Based on the DDH Assumption

As part of my diploma thesis titled "Funkcijsko šifriranje in shema za računanje skalarnih produktov" in Slovenian or "Functional Encrpytion and a Scheme for Computing Inner Products" in English, I implemented the Inner Product scheme based on the DDH assumption from Abdalla, Bourse, De Caro and Pointcheval in Python. I also performed two tests to measure the execution time of the implemented functions and another test to measure the time needed for generating a safe prime and a generator of the quadratic residues group modulo a safe prime. The source code for the scheme can be found in the file **Scheme.py**, while the source code for the tests is available in the files **SchemeTesting_RandomGrades.ipynb**, **SchemeTesting_LargerNumbers.ipynb** and **SchemeTesting_Generators**.

The operations are performed in the group of quadratic residues modulo a safe prime. It is believed that the DDH assumption holds in these groups.

For the computation of the final discrete logarithm, I implemented the Baby-step giant-step algorithm and its source code can also be found in the file **Scheme.py**. 

In **SchemeTesting_Grades.ipynb** I computed a weighted mean of the grades of some student, where the weight of each grade is the amount of ECTS of the corresponding subject. The grades are fictional, but the ECTS credits assigned to each subject represent the ECTS of the subjects I had to complete to finish my bachelor's program, excluding the diploma seminar.

In **SchemeTesting_RadnomGrades.ipynb** I computed a weighted sum of randomly chosen grades of some student, where the weight of each grade is the amount of ECTS of the corresponding subject. The grades are randomly chosen, but the ECTS credits assigned to each subject represent the ECTS of the subjects I had to complete to finish my bachelor's program, excluding the diploma seminar. 
The length of the vectors is 30, since I completed 30 subjects on my undergraduate program, while the individual components of the vectors are less than 11, since the maximum possible grade is 10 and no subject was worth more than 10 ECTS. 

In **SchemeTesting_LargerNumbers.ipynb** I computed the inner products between random vectors of dimension 100 with individual components less than 10 000. The goal was to demonstrate that the scheme can be useful in a more realistic environment, where the vectors have higher dimensions and the individual components of the vectors are significantly larger compared to the previous test. 

The measured time results can be found in the image "measured_time.jpg".
