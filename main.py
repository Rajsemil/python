import pickle
def pickle_data():
    data = {
                'name': 'Prashant',
                'profession': 'Software Engineer',
                'country': 'India'
        }
    filename = 'PersonalInfo'
    outfile = open('file.txt', 'wb')
    pickle.dump(data,outfile)
    outfile.close()
pickle_data()