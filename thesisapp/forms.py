from django import forms

SUBJECT_CHOICES= [
    ('Electronics', 'Electronics'),
    ('Power & Energy Systems', 'Power & Energy Systems'),
    ('Communication', 'Communication'),
    ('Digital Signal Processing', 'Digital Signal Processing'),
    ('Renewable Energy', 'Renewable Energy'),
    ('Wireless Communication', 'Wireless Communication'),
    ('Biomedical Signal & Image Processing', 'Biomedical Signal & Image Processing',),
    ('Optical Fiber Communication', 'Optical Fiber Communication',),
    ('Machine Learning & Data Science', 'Machine Learning & Data Science',),
    ('Internet of Things', 'Internet of Things',),
    ]

class RegisterForm(forms.Form):
    leader_name    = forms.CharField(label = "Group Leader's Name:", max_length=20)
    leader_id      = forms.IntegerField(label = "Group Leader's ID:")
    leader_cgpa    = forms.DecimalField(label = "Group Leader's CGPA (Till 3.1):", decimal_places=2, max_digits=4)
    co_leader_id   = forms.IntegerField(label = "Co Leader's ID:")
    co_leader_cgpa = forms.DecimalField(label = "Co Leader's CGPA (Till 3.1):" ,decimal_places=2, max_digits=4)
    contact_mail = forms.EmailField(label="Enter your email address:")


    choice1  = forms.CharField(label='Choice 01 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice2  = forms.CharField(label='Choice 02 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice3  = forms.CharField(label='Choice 03 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice4  = forms.CharField(label='Choice 04 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice5  = forms.CharField(label='Choice 05 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice6  = forms.CharField(label='Choice 06 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice7  = forms.CharField(label='Choice 07 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice8  = forms.CharField(label='Choice 08 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice9  = forms.CharField(label='Choice 09 :', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)
    choice10 = forms.CharField(label='Choice 010:', widget=forms.Select(choices=SUBJECT_CHOICES), max_length=50)